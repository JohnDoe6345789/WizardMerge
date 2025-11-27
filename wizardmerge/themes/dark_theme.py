"""Built-in dark theme."""
from wizardmerge.themes.base import Theme


palette = {
    "background": "#0d1117",
    "surface": "#161b22",
    "text": "#e6edf3",
    "accent": "#7c9aff",
    "border": "#30363d",
}

theme = Theme(name="Dark", palette=palette)
