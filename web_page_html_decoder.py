import requests
from bs4 import BeautifulSoup

# URL of the NY Times website we want to parse
base_url = 'https://www.nytimes.com'

# Adding headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# Request the webpage
r = requests.get(base_url, headers=headers)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Find and loop through all elements that look like article headings
# Updated to a more generic selector since "story-heading" may no longer exist
for story_heading in soup.find_all(['h2', 'h3', 'h4'], class_=lambda c: c and 'story' in c):
    # For story headings that are links, print the text nicely
    if story_heading.a:
        print(story_heading.a.get_text(strip=True))
    else:
        print(story_heading.get_text(strip=True))
