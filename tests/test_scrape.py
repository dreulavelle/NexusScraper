import pytest

from Nexus.models import NexusSettings
from Nexus.scraper import NexusScrapers
from Nexus.scrapers.torrentio import Torrentio


@pytest.fixture
def p():
    settings = NexusSettings()
    return NexusScrapers(settings)

def test_scrape(p):
    data = p.scrape("torrentio", "tt0113497", media_type="movie")
    assert len(data) > 0
    assert isinstance(data, list)

def test_scrape_all(p):
    data = p.scrape_all("tt0113497", media_type="movie")
    sources = set([item.source for item in data])
    assert len(sources) > 1
    assert len(data) > 50
    assert isinstance(data, list)

def test_get_sources(p):
    sources = p.get_sources()
    assert len(sources) == 6
    assert isinstance(sources, list)

def test_get_scraper(p):
    torrentio = p.get_scraper("torrentio")
    assert isinstance(torrentio, Torrentio)

    results = torrentio.scrape("tt0113497", media_type="movie")
    assert len(results) > 0
    assert isinstance(results, list)