import json
from pathlib import Path

def load_report():
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json was not created"
    with report_path.open() as f:
        return json.load(f)

def test_total_requests():
    report = load_report()
    assert report["total_requests"] == 6

def test_unique_clients():
    report = load_report()
    assert report["unique_ips"] == 3

def test_top_page():
    report = load_report()
    assert report["top_path"] == "/index.html"