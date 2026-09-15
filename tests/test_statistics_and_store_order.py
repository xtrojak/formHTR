from __future__ import annotations

from formhtr.libs.processing.store_results import order_results
from formhtr.libs.statistics import compute_stats, format_stats


def test_order_results_follows_expected_priority():
    values = {"azure": "az", "inferred": "inf", "google": "gg"}
    assert order_results(values) == ["inf", "gg", "az"]


def test_compute_stats_handles_zero_artefacts():
    stats = compute_stats(
        contents=[["a", {}, None], ["b", {}, None]],
        artefacts={"google": [], "amazon": [], "azure": []},
    )
    assert stats["matches"] == 2
    assert stats["artefacts"] == 0
    assert stats["ratio"] == 2.0
    assert format_stats(stats) == "2.000 (2:0)"


def test_format_stats_includes_ratio_and_counts():
    assert format_stats({"matches": 7, "artefacts": 8, "ratio": 0.875}) == "0.875 (7:8)"
