import requests
from bs4 import BeautifulSoup
import re

def scrape_wikipedia(url:str):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    } 
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Title
    title = soup.find('h1', id='firstHeading').text.strip()
    
    # Summary (first paragraph)
    summary = soup.find('p').text.strip()
    text = soup.get_text()
    people = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', text)[:5]  # Simple name extraction
    organizations = re.findall(r'\b[A-Z][a-z]+ (University|Park|Institute)\b', text)[:5]
    locations = re.findall(r'\b[A-Z][a-z]+ (Kingdom|States|City)\b', text)[:5]
    key_entities = {"people": list(set(people)), "organizations": list(set(organizations)), "locations": list(set(locations))}
    
    # Sections
    sections = [h.text.strip() for h in soup.find_all(['h2', 'h3']) if h.text.strip()]
    
    return {
        "title": title,
        "summary": summary,
        "key_entities": key_entities,
        "sections": sections,
        "full_text": text  # For LLM
    }