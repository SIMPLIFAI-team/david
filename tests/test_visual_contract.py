import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "www"
EXPECTED = {
    "assets/css/styles.css": "ce3ce5581ee69dea9f44ddceaf0249481eeb3de97d7d695e7fdae10a8eb092ac",
    "assets/css/case-study.css": "2775e4e02a6bca269e77ae41b931cb5aa6b031deb1b9508b3e0bc8f39953f497",
    "assets/css/cookie-consent-overrides.css": "71d92e8c9a363d5872544dc15636467e3bf1deab0013d35614c1ac4e4c702bc3",
}


class VisualContractTests(unittest.TestCase):
    def test_existing_stylesheets_are_byte_identical(self):
        for relative, expected in EXPECTED.items():
            digest = hashlib.sha256((SITE / relative).read_bytes()).hexdigest()
            self.assertEqual(expected, digest, relative)

    def test_existing_case_study_pages_are_present(self):
        self.assertEqual(5, len(list((SITE / "case-studies").glob("*.html"))))

    def test_2026_palette_is_preserved(self):
        for relative in ("assets/css/styles.css", "assets/css/case-study.css"):
            css = (SITE / relative).read_text(encoding="utf-8")
            for token in (
                "--bg:#57504c",
                "--bg2:#435155",
                "--text:#eeece1",
                "--accent:#a7b3aa",
                "--accent2:#e8decf",
            ):
                self.assertIn(token, css, f"{relative}: {token}")

    def test_root_compatibility_styles_match_www_source(self):
        for relative in EXPECTED:
            self.assertEqual(
                (ROOT / relative).read_bytes(),
                (SITE / relative).read_bytes(),
                relative,
            )


if __name__ == "__main__":
    unittest.main()
