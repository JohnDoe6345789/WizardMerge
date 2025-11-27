"""Built-in light theme."""
from wizardmerge.themes.base import Theme


palette = {
    "background": "#f5f5f5",
    "surface": "#ffffff",
    "text": "#1f2933",
    "accent": "#0f7ada",
    "border": "#d8d8d8",
}

theme = Theme(name="Light", palette=palette)
