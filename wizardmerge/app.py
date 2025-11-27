"""Application bootstrap for the WizardMerge PyQt6 + QML UI."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine

from wizardmerge.themes.loader import ThemeManager


def _resolve_qml_path() -> Path:
    """Return the absolute path to the main QML entry file."""
    qml_path = Path(__file__).parent / "qml" / "main.qml"
    if not qml_path.exists():
        raise FileNotFoundError("Unable to locate main.qml; ensure resources are installed.")
    return qml_path


def run(preferred_theme: Optional[str] = None) -> int:
    """Run the WizardMerge UI.

    Args:
        preferred_theme: Optional theme name to prioritize when loading themes.

    Returns:
        Exit code to propagate to the caller.
    """
    app = QGuiApplication(sys.argv)
    theme_manager = ThemeManager()
    theme = theme_manager.select_theme(preferred_theme)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("theme", theme.as_dict())

    qml_path = _resolve_qml_path()
    engine.load(QUrl.fromLocalFile(qml_path.as_posix()))

    if not engine.rootObjects():
        return 1

    return app.exec()


def main() -> None:
    """Entry-point wrapper for console scripts."""
    sys.exit(run())


if __name__ == "__main__":
    main()
