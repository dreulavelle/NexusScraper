import pytest

from Nexus.exceptions import NexusException
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

def test_orionoid_scrape_movie(p):
    data = p.scrape("tt0113497", "movie")
    assert len(data) == 50
    assert isinstance(data, (list, ScrapeResult))

def test_orionoid_scrape_show(p):
    data = p.scrape("tt0944947", "show", 1, 1)
    assert len(data) == 50
    assert isinstance(data, (list, ScrapeResult))

def test_orionoid_invalid():
    with pytest.raises(NexusException):
        settings = NexusSettings(
            orionoid_client="",
            orionoid_apikey="",
        )
        orionoid.Orionoid(settings)

def test_orionoid_scrape_invalid(p):
    with pytest.raises(NexusException):
        p.scrape("invalid", "series", 1, 1)
