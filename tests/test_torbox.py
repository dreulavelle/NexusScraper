import pytest

from Nexus.models import ScrapeResult
from Nexus.scrapers import torbox


@pytest.fixture
def p():
    return torbox.TorBox()

def test_scrape(p):
    data = p.scrape("game of thrones", "show")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_invalid_scrape():
    results = torbox.TorBox().scrape("")
    assert results == []
