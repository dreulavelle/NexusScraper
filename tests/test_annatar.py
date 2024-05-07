import pytest

from Nexus.exceptions import AnnatarException
from Nexus.models import NexusSettings, ScrapeResult
from Nexus.scrapers import annatar


@pytest.fixture
def p():
    settings = NexusSettings()
    return annatar.Annatar(settings)

def test_annatar_movie(p):
    assert isinstance(p.base_url, str)
    data = p.scrape("tt0113497", "movie")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_annatar_episode(p):
    data = p.scrape("tt0944947", "show", 2, 4)
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_annatar_invalid(p):
    with pytest.raises(AnnatarException):
        p.scrape("game of thrones")
