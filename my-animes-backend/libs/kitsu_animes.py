import math
import requests
from models.Anime import Anime
from models.Paginated import Paginated, create_paginated

BASE_URL = "https://kitsu.io/api"


def create_kitsu_formatted(ed) -> Anime:
    return Anime(
        image=ed["attributes"]["posterImage"]["original"],
        title=ed["attributes"]["canonicalTitle"],
        slug=ed["attributes"]["slug"],
        synopsis=ed["attributes"]["synopsis"],
        total_chapters=ed["attributes"]["episodeCount"]
    )


def fetch_animes(page: int = None, limit: int = None) -> Paginated[Anime]:
    if not limit:
        limit = 10
    if not page:
        page = 0

    page *= 10

    url = BASE_URL + \
        f"/edge/anime?page%5Blimit%5D={limit}&page%5Boffset%5D={page}"

    req = requests.get(url)
    req_data = req.json()
    data = [create_kitsu_formatted(e) for e in req_data["data"]]

    p = create_paginated(
        data,
        total_pages=math.ceil(req_data["meta"]["count"] / 10),
        current_page=page
    )

    return p


def fetch_anime(slug: str):
    url = BASE_URL + f"/edge/anime?filter[text]={slug}"
    req = requests.get(url)
    data = req.json()
    if data["meta"]["count"] == 0:
        raise Exception(f"Cannot find {slug}")

    req_anime = data["data"][0]
    anime = {
        "image": req_anime["attributes"]["poster_image"]["original"],
        "title": req_anime["attributes"]["canonicalTitle"],
        "slug": req_anime["attributes"]["slug"],
        "synopsis": req_anime["attributes"]["synopsis"],
        "total_chapters": req_anime["attributes"]["episodeCount"]
    }
    return anime
