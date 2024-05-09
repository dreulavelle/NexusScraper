import pytest

from Nexus.models import NexusSettings, ScrapeResult
from Nexus.scrapers import jackett


@pytest.fixture
def p():
    settings = NexusSettings()
    return jackett.Jackett(settings)

def test_jackett(p):
    assert isinstance(p.base_url, str)
    assert isinstance(p.api_key, str)

def test_scrape(p):
    data = p.scrape("game of thrones", "show")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))
