from typing import List

import pytest

from Nexus.exceptions import ProwlarrException
from Nexus.models import NexusSettings, ScrapeResult
from Nexus.scrapers import prowlarr


@pytest.fixture
def settings():
    return NexusSettings()

@pytest.fixture
def p(settings):
    return prowlarr.Prowlarr(settings)

def test_prowlarr(p):
    assert isinstance(p.api_key, str)
    assert isinstance(p.base_url, str)
    assert p.api_key != "" or p.api_key is not None
    assert p.base_url != "" or p.base_url is not None

def test_invalid_prowlarr():
    with pytest.raises(ProwlarrException):
        settings = NexusSettings(
            prowlarr_url="",
            prowlarr_apikey="",
        )
        prowlarr.Prowlarr(settings)

def test_scrape(p):
    results: List[ScrapeResult] = p.scrape("game of thrones", 50)
    assert len(results) > 0
    assert len(results) <= 50

def test_ping(p):
    data = p.ping()
    assert isinstance(data, dict)
