from argparse import ArgumentParser
import argparse
from http.client import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.Anime import Anime, CreateAnime
from models.Paginated import Paginated

from services import animes_service

from sites.animefenix.AnimeFenix import AnimeFenix
from sites.yourupload.Yourupload import YourUpload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/animes", response_model=Paginated[Anime], response_model_exclude_defaults=True)
def get_animes():
    return animes_service.get_animes()


@app.get("/animes/:slug", response_model=Anime)
def get_anime(slug: str):
    return animes_service.get_anime(slug)


@app.post("/animes")
def create_anime(anime: CreateAnime):
    return animes_service.create_anime(anime.slug)


if __name__ == "__main__":
    parser = ArgumentParser(description="Anime downloader",
                            formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-n", "--name", dest="name", help="Anime name")
    parser.add_argument("-c", "--chapter", dest="chapter",
                        type=int, help="Chapter number")

    args = parser.parse_args()

    anime_slug = args.name
    chapter = args.chapter

    AnimeFenix(YourUpload(
        f"static/animes/{anime_slug}",
        f"cap-{chapter}.mp4")
    ).download_chapter(anime_slug, chapter)
