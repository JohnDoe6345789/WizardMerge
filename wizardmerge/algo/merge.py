"""Toy merge utilities to accompany the GUI."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence


@dataclass
class MergeResult:
    """Hold the combined payload and an audit trail of sources."""

    merged: str
    sources: List[str]


def merge_pairs(lines_a: Sequence[str], lines_b: Sequence[str]) -> MergeResult:
    """Return interleaved lines and capture their origin.

    This function is intentionally simple, providing a deterministic merge
    strategy useful for demonstration in the GUI layer.
    """

    merged_lines: List[str] = []
    sources: List[str] = []

    for index, (line_a, line_b) in enumerate(zip(lines_a, lines_b)):
        merged_lines.append(line_a)
        merged_lines.append(line_b)
        sources.append(f"A{index}")
        sources.append(f"B{index}")

    if len(lines_a) > len(lines_b):
        for tail_index, line in enumerate(lines_a[len(lines_b) :], start=len(lines_b)):
            merged_lines.append(line)
            sources.append(f"A{tail_index}")
    elif len(lines_b) > len(lines_a):
        for tail_index, line in enumerate(lines_b[len(lines_a) :], start=len(lines_a)):
            merged_lines.append(line)
            sources.append(f"B{tail_index}")

    return MergeResult(merged="\n".join(merged_lines), sources=sources)
