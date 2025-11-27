"""Core theme definitions."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class Theme:
    """Simple theme container for color palette values."""

    name: str
    palette: Dict[str, str]

    def as_dict(self) -> Dict[str, str]:
        """Return a dictionary representation usable by QML contexts."""
        return {"name": self.name, **self.palette}
