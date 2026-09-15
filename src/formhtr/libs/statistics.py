def compute_stats(contents, artefacts):
    """Count ROI matches versus OCR artefacts and their ratio.

    The ratio is ``matches / artefacts`` (artefacts of 0 treated as 1 so the
    value is defined).

    Args:
        contents (list): Identified regions that matched ROI locations.
        artefacts (dict): Extra OCR hits per service.

    Returns:
        Dict with keys ``matches`` (int), ``artefacts`` (int), ``ratio`` (float).
    """
    matches = len(contents)
    artefact_count = max(len(items) for items in artefacts.values())
    ratio = matches / max(artefact_count, 1)  # avoid division by zero
    return {"matches": matches, "artefacts": artefact_count, "ratio": ratio}


def format_stats(stats):
    """Format as ``ratio (matches:artefacts)``."""
    return f"{stats['ratio']:.3f} ({stats['matches']}:{stats['artefacts']})"
