import pytest

from Nexus.models import NexusSettings, ScrapeResult
from Nexus.scrapers import orionoid


@pytest.fixture
def p():
    settings = NexusSettings()
    return orionoid.Orionoid(settings)

def test_orionoid(p):
    assert isinstance(p.api_key, str)
    assert isinstance(p.base_url, str)
    assert p.api_key != "" or p.api_key is not None
    assert p.base_url != "" or p.base_url is not None

def test_orionoid_scrape_imdb(p):
    data = p.scrape("tt0113497", "movie")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_orionoid_scrape_raw(p):
    data = p.scrape("game of thrones", "show")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))
