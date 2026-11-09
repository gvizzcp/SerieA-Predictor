import requests
from pathlib import Path

out = Path("data/raw")
out.mkdir(parents=True, exist_ok=True)

for start in range(16, 27):
       season = f"{start}{start+1}"
       url = f"https://www.football-data.co.uk/mmz4281/{season}/I1.csv"
       r = requests.get(url)
       if r.ok:
           (out / f"seriea_{season}.csv").write_bytes(r.content)
           print("Scaricato", season)