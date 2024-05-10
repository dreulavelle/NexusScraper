import pytest

from Nexus.models import ScrapeResult
from Nexus.scrapers.apibay import Apibay


@pytest.fixture
def p():
    return Apibay()

def test_apibay(p):
    data = p.scrape("game of thrones")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))
