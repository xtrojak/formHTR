from __future__ import annotations

from pathlib import Path

from formhtr.deps import check_system_dependencies
from formhtr.libs.pdf_to_image import convert_pdf_to_image

TEMPLATE_PDF = Path(__file__).resolve().parent / "test-data" / "template" / "template_tara.pdf"


def test_poppler_is_installed_and_can_rasterize_pdf():
    missing = dict(check_system_dependencies())
    assert "poppler" not in missing, (
        "Poppler (pdfinfo) is required to convert PDFs. "
        f"Install hint: {missing['poppler']}"
    )
    image = convert_pdf_to_image(str(TEMPLATE_PDF), dpi=72)
    assert image.size[0] > 0 and image.size[1] > 0
