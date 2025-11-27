"""Theme loading and plugin discovery helpers."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path
from pkgutil import iter_modules
from typing import Iterable, List, Sequence

from wizardmerge.themes.base import Theme


class ThemeManager:
    """Manage built-in and plugin-based themes."""

    def __init__(self, extra_plugin_paths: Sequence[Path] | None = None) -> None:
        self._builtin_modules = self._discover_builtin_modules()
        self._plugin_modules = self._discover_plugin_modules(extra_plugin_paths)

    @staticmethod
    def _discover_builtin_modules() -> List[str]:
        """Return module names for bundled themes."""
        module_path = Path(__file__).parent
        modules = []
        for module in iter_modules([str(module_path)]):
            if module.name.endswith("_theme"):
                modules.append(f"{__package__}.{module.name}")
        return modules

    @staticmethod
    def _discover_plugin_modules(extra_paths: Sequence[Path] | None) -> List[str]:
        """Return module names for shipped plugin examples and user-defined themes."""
        modules: List[str] = []
        plugin_package = f"{__package__}.plugins"
        plugin_path = Path(__file__).parent / "plugins"
        modules.extend(
            f"{plugin_package}.{module.name}" for module in iter_modules([str(plugin_path)]) if module.ispkg is False
        )

        if extra_paths:
            for path in extra_paths:
                if not path.exists():
                    continue
                sys.path.append(str(path))
                modules.extend(module.name for module in iter_modules([str(path)]))

        return modules

    def _load_theme_from_module(self, module_name: str) -> Theme | None:
        module = importlib.import_module(module_name)
        theme = getattr(module, "theme", None) or getattr(module, "warm_theme", None)
        if isinstance(theme, Theme):
            return theme
        return None

    def available_themes(self) -> List[Theme]:
        """Return a list of all themes that could be loaded."""
        themes: List[Theme] = []
        for module in [*self._builtin_modules, *self._plugin_modules]:
            theme = self._load_theme_from_module(module)
            if theme:
                themes.append(theme)
        return themes

    def select_theme(self, preferred_name: str | None = None) -> Theme:
        """Return the preferred theme or fall back to the first available one."""
        themes = self.available_themes()
        if not themes:
            raise RuntimeError("No themes could be loaded.")

        if preferred_name:
            for theme in themes:
                if theme.name.lower() == preferred_name.lower():
                    return theme

        return themes[0]
