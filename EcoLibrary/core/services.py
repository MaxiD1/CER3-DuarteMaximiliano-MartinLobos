import requests

BASE_URL = "https://openlibrary.org/"

def fetch_json(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

def get_book_extra_data(isbn):
    book = fetch_json(f"{BASE_URL}/isbn/{isbn}.json")
    if not book:
        return None

    # Work ID
    work_key = book["works"][0]["key"]
    work = fetch_json(f"{BASE_URL}{work_key}.json")

    # Autores
    authors = []
    for a in work.get("authors", []):
        data = fetch_json(f"{BASE_URL}{a['author']['key']}.json")
        if data:
            authors.append(data.get("name"))

    # Descripción
    desc = work.get("description")
    if isinstance(desc, dict):
        desc = desc.get("value")

    # Año
    year = None
    if work.get("created"):
        year = work["created"]["value"][:4]

    # Categorías
    categories = work.get("subjects", [])

    # Portada
    cover_id = work.get("covers", [None])[0]
    cover_url = ""
    if cover_id:
        cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"


    return {
        "title": work.get("title"),
        "authors": authors,
        "description": desc,
        "year": year,
        "categories": categories,
        "cover_url": cover_url,
    }