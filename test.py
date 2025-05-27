from utils.sofascore_scraper import get_season_ids

url = "https://www.sofascore.com/tournament/football/england/premier-league/17"
season_dict = get_season_ids(url)

print("Available seasons:")
for name, sid in season_dict.items():
    print(f"{name}: {sid}")
