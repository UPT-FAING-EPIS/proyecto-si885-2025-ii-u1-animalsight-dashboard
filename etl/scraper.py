import requests
from bs4 import BeautifulSoup

SECTIONS = {
    "RPP": "https://rpp.pe/peru/tacna",
    "El Comercio": "https://elcomercio.pe/peru/tacna/",
    "La Republica": "https://larepublica.pe/tacna",
    "Peru21": "https://peru21.pe/peru/tacna/",
}

def get_links(section_url, limit=15):
    links = []
    try:
        r = requests.get(section_url, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "tacna" in href.lower():
                if not href.startswith("http"):
                    href = requests.compat.urljoin(section_url, href)
                if href not in links:
                    links.append(href)
            if len(links) >= limit:
                break
    except Exception as e:
        print(f"Error en {section_url}: {e}")
    return links

def extract_text(url):
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
        s = BeautifulSoup(r.text, "html.parser")
        parts = [p.get_text(" ", strip=True) for p in s.find_all("p")]
        return " ".join(parts)
    except:
        return ""
