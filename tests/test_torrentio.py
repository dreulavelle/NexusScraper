import pytest

from Nexus.exceptions import TorrentioException
from Nexus.models import NexusSettings, ScrapeResult
from Nexus.scrapers import torrentio


@pytest.fixture
def p():
    settings = NexusSettings()
    return torrentio.Torrentio(settings)

def test_torrentio_movie(p):
    assert isinstance(p.base_url, str)
    assert isinstance(p.filters, str)
    data = p.scrape("tt0113497", "movie")
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_torrentio_episode(p):
    data = p.scrape("tt0944947", "show", 2, 4)
    assert len(data) > 0
    assert isinstance(data, (list, ScrapeResult))

def test_torrentio_invalid(p):
    with pytest.raises(TorrentioException):
        p.scrape("", "")
