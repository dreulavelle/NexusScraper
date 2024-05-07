import pytest

from Nexus.exceptions import ProwlarrException
from Nexus.models import NexusSettings, ScrapeResult
from Nexus.scrapers import prowlarr


@pytest.fixture
def p():
    settings = NexusSettings()
    return prowlarr.Prowlarr(settings)

def test_prowlarr(p):
    assert isinstance(p.api_key, str)
    assert isinstance(p.base_url, str)
    assert p.api_key != "" or p.api_key is not None
    assert p.base_url != "" or p.base_url is not None

def test_scrape(p):
    data = p.scrape("game of thrones", "show")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_ping(p):
    data = p.ping()
    assert isinstance(data, dict)

def test_invalid_prowlarr():
    with pytest.raises(ProwlarrException):
        settings = NexusSettings(
            prowlarr_url="",
            prowlarr_apikey="",
        )
        prowlarr.Prowlarr(settings)
