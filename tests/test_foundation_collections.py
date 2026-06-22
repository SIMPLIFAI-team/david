import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "www"


class FoundationCollectionsTests(unittest.TestCase):
    def load(self, collection_id):
        base = SITE / "collections" / collection_id
        manifest = json.loads((base / "collection.json").read_text(encoding="utf-8"))
        items = json.loads((base / manifest["dataFile"]).read_text(encoding="utf-8"))
        return manifest, items

    @staticmethod
    def visible(items):
        return [item for item in items if item["status"] == "published"]

    def test_case_studies_use_shared_catalog_contract(self):
        manifest, items = self.load("case-studies")
        self.assertEqual("catalog", manifest["mode"])
        self.assertEqual("card-grid", manifest["layout"])
        self.assertFalse(manifest["interactive"])
        self.assertEqual(3, len(self.visible(items)))
        self.assertEqual(5, len(items))
        for item in items:
            self.assertTrue((SITE / item["primaryAction"]["href"]).is_file(), item["primaryAction"]["href"])

    def test_resume_registry_covers_all_files_without_expanding_page(self):
        manifest, items = self.load("resumes")
        self.assertEqual("catalog", manifest["mode"])
        self.assertEqual("card-grid", manifest["layout"])
        self.assertFalse(manifest["interactive"])
        self.assertEqual(3, len(self.visible(items)))
        self.assertEqual(6, len(items))
        for item in items:
            self.assertTrue((SITE / item["primaryAction"]["href"]).is_file(), item["primaryAction"]["href"])
            self.assertTrue((SITE / item["secondaryAction"]["href"]).is_file(), item["secondaryAction"]["href"])

    def test_rendered_index_uses_collection_regions(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertIn("<!-- PM:COLLECTION-CASE-STUDIES -->", html)
        self.assertIn("<!-- PM:COLLECTION-RESUMES -->", html)
        self.assertIn("<!-- PM:COLLECTION-SCRIPTS -->", html)
        self.assertIn('data-collection-id="case-studies"', html)
        self.assertIn('data-collection-id="resumes"', html)
        self.assertNotIn("fallbackCaseStudies", html)
        self.assertNotIn('fetch(source, { cache: "no-store" })', html)

    def test_visible_inventory_is_unchanged(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        visible_case_titles = [
            "Multi-tenant QA auditing and mobile data collection",
            "Replayable vendor API ingestion and reporting layer",
            "Corporate website and Portmason platform experience",
        ]
        visible_resume_titles = [
            "SaaS/Platform Engineer",
            "SQL Server/Data Platform",
            "IT/Network Administrator",
        ]
        for title in visible_case_titles + visible_resume_titles:
            self.assertEqual(1, html.count(title), title)
        self.assertNotIn("<h3>Cloud Architect</h3>", html)
        self.assertNotIn("<h3>Middleware/Integration</h3>", html)


if __name__ == "__main__":
    unittest.main()
