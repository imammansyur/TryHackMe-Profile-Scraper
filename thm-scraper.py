import requests
from datetime import date
import json

# scrape Tryhackme profile, change to your own profile
url = "https://tryhackme.com/api/v2/public-profile/completed-rooms?user=[YOUR USERNAME FROM INSPECT ELEMENTS-NETWORK]&limit=16&page=1"
response = requests.get(url).text
data = json.loads(response)

# Build markdown
lines = [
    "# TryHackMe Progress",
    f"Last updated: {date.today()} using [TryHackMe-Profile-Scraper](https://github.com/imammansyur/TryHackMe-Profile-Scraper)",
    "",
    "| Room | Difficulty |",
    "|------|------------|",
]

# Extract completed rooms
rooms = data["data"]["docs"]
for room in rooms[::-1]: # Reversed to show the latest first
    lines.append(f"| {room['title']} | {room['difficulty'].title()} |")

md = "\n".join(lines)

# write to TryHackMe/README.md
with open("TryHackMe/README.md", "w", encoding="utf-8") as f:
    f.write(md)
