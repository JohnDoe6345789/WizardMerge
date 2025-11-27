"""Sample theme plugin distributed separately from the built-ins."""
from wizardmerge.themes.base import Theme


palette = {
    "background": "#fdf1e5",
    "surface": "#fde7d3",
    "text": "#3b2f2f",
    "accent": "#d67b4d",
    "border": "#f6c4a3",
}

warm_theme = Theme(name="Warm", palette=palette)
