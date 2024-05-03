from pydantic import BaseModel, field_validator


class NexusSettings(BaseModel):
    """
    NexusSettings class for storing Nexus settings.

    Attributes:
    - `prowlarr_url`: str
    - `prowlarr_apikey`: str
    - `jackett_url`: str
    - `jackett_apikey`: str
    """
    prowlarr_url: str
    prowlarr_apikey: str
    jackett_url: str
    jackett_apikey: str


class ScrapeResult(BaseModel):
    """
    ScrapeResult class for storing scrape results.

    Attributes:
    - `title`: str
    - `infohash`: str
    - `source`: str
    """
    title: str
    infohash: str
    source: str

    @field_validator("source")
    def validate_source(cls, source):
        sources = ["annatar", "jackett", "prowlarr", "torbox", "torrentio"]
        if source not in sources:
            return "torrentio"
        return source
    
    @field_validator("infohash")
    def validate_infohash(cls, infohash):
        if len(infohash) != 40:
            raise ValueError("Infohash must be 40 characters long.")
        return infohash
    
    @field_validator("title")
    def validate_title(cls, title):
        if len(title) > 255:
            raise ValueError("Title must be less than 256 characters long.")
        return title
    
    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.infohash == other.infohash
    
    def __hash__(self):
        return hash(self.infohash)
