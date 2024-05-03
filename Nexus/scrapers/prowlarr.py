import requests
from utils.exceptions import NexusException
from . import settings


class Prowlarr:
    """Prowlarr class for Prowlarr API operations."""

    def __init__(self):
        self.api_key = settings.prowlarr_apikey.get_secret_value()
        self.base_url = settings.prowlarr_url
        self.session = requests.Session()
        self.session.headers.update({"X-Api-Key": self.api_key})

    def _request(self, endpoint, method="GET", params=None, data=None):
        url = f"{self.base_url}/api/v1/{endpoint}"
        try:
            response = self.session.request(method, url, params=params, json=data)
            response.raise_for_status()  # Raises error for 4xx/5xx responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise NexusException(f"API request error: {e}")

    def scrape(self, query):
        """Scrape Prowlarr for a given query."""
        return self._request("indexer/search", params={"query": query})

    def get_indexers(self):
        """Retrieve a list of configured indexers."""
        return self._request("indexer")

    def get_system_status(self):
        """Get the system status."""
        return self._request("system/status")

    def get_indexer(self, indexer_id):
        """Retrieve a single indexer by ID."""
        return self._request(f"indexer/{indexer_id}")

    def test_indexer(self, indexer_id):
        """Test a single indexer by ID."""
        return self._request(f"indexer/test/{indexer_id}")

    def get_indexer_presets(self):
        """Get indexer presets."""
        return self._request("indexer/presets")

    def add_indexer(self, indexer_config):
        """Add a new indexer with the given configuration."""
        return self._request("indexer", method="POST", data=indexer_config)

    def delete_indexer(self, indexer_id):
        """Delete an indexer by ID."""
        return self._request(f"indexer/{indexer_id}", method="DELETE")
