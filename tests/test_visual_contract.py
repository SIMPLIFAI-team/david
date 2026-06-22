import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "www"
EXPECTED = {
    "assets/css/styles.css": "213ddd942879e7e6d3cf5f6dacedf8e87806e4e92b5e280f7a80941e4f548f3b",
    "assets/css/case-study.css": "d61ff2af7eeceebac11d761114115c9c025a031a82f4b939eedba0d06313fab3",
    "assets/css/cookie-consent-overrides.css": "71d92e8c9a363d5872544dc15636467e3bf1deab0013d35614c1ac4e4c702bc3",
}


class VisualContractTests(unittest.TestCase):
    def test_existing_stylesheets_are_byte_identical(self):
        for relative, expected in EXPECTED.items():
            digest = hashlib.sha256((SITE / relative).read_bytes()).hexdigest()
            self.assertEqual(expected, digest, relative)

    def test_existing_case_study_pages_are_present(self):
        self.assertEqual(5, len(list((SITE / "case-studies").glob("*.html"))))


if __name__ == "__main__":
    unittest.main()
