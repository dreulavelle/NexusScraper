import time

import pytest

from Nexus.models import NexusSettings, ScrapeResult
from Nexus.scraper import NexusScrapers
from Nexus.scrapers.torrentio import Torrentio


@pytest.fixture
def p():
    settings = NexusSettings()
    return NexusScrapers(settings)

def test_scrape(p):
    time_start = time.time()
    data = p.scrape("torrentio", "tt0113497", media_type="movie")
    duration = time.time() - time_start
    print(f"Scrape duration: {duration:.3f} seconds")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_scrape_imdb(p):
    time_start = time.time()
    data = p.imdb_scrape("tt0113497", media_type="movie")
    duration = time.time() - time_start
    print(f"IMDb Scrape duration: {duration:.3f} seconds")
    assert len(data) > 200
    assert isinstance(data, (list, ScrapeResult))

def test_scrape_raw(p):
    time_start = time.time()
    data = p.scrape_raw("game of thrones", media_type="show")
    duration = time.time() - time_start
    print(f"Raw Scrape duration: {duration:.3f} seconds")
    assert len(data) > 200
    assert isinstance(data, (list, ScrapeResult))

def test_get_sources(p):
    sources = p.get_sources()
    assert len(sources) == 6
    assert isinstance(sources, list)

def test_get_scraper(p):
    time_start = time.time()
    torrentio: Torrentio = p.get_scraper("torrentio")
    data = torrentio.scrape("tt0113497", media_type="movie")
    duration = time.time() - time_start
    print(f"Torrentio scrape duration: {duration:.3f} seconds")
    assert len(data) > 0
    assert isinstance(data, list)
