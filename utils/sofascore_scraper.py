import requests
from bs4 import BeautifulSoup
import re

def get_season_ids(tournament_url):
    response = requests.get(tournament_url)
    if not response.ok:
        raise Exception("Could not fetch page. Check the URL.")

    soup = BeautifulSoup(response.text, "html.parser")
    season_links = soup.find_all("a", href=re.compile(r"/[^/]+/\d+$"))

    season_ids = {}
    for link in season_links:
        match = re.search(r"/(\d+)$", link["href"])
        if match:
            season_id = int(match.group(1))
            season_name = link.text.strip()
            if season_id and season_name and not season_name.startswith("Live"):
                season_ids[season_name] = season_id

    return season_ids
