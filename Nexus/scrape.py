from .utils.models import ScrapeResult
from scrapers import (
    annatar,
    jackett,
    prowlarr,
    torbox,
    torrentio
)


class NexusScrapers:
    def __init__(self):
        self.scrapers = {
            "annatar": annatar,
            "jackett": jackett,
            "prowlarr": prowlarr,
            "torbox": torbox,
            "torrentio": torrentio
        }

    def scrape(self, source = "torrentio", query = "", **kwargs):
        """Scrape a given source for a query."""
        results = self.scrapers[source].scrape(query, **kwargs)
        return [ScrapeResult(**result) for result in results]
    
    def get_sources(self):
        """Get a list of available sources."""
        return list(self.scrapers.keys())

    def get_scraper(self, source):
        """Get a scraper by source."""
        if source not in self.scrapers:
            return self.scrapers["torrentio"]
        return self.scrapers[source]
