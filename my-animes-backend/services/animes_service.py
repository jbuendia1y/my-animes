import os
from libs import kitsu_animes
from repositories import animes_repository as repository


def get_animes(user_id: int = None):
    if user_id:
        animes = repository.get_my_animes(user_id)
    else:
        animes = repository.get_animes()
    return animes


def get_anime(slug: str):
    anime = repository.get_anime(slug)
    return anime


def find_anime_dir(slug: str):
    project_dir = os.getcwd()
    animes_dir = os.path.join(project_dir, "animes")
    files = os.listdir(animes_dir)

    if slug in files:
        anime_dir = os.path.join(animes_dir, slug)
        return anime_dir

    return False


def create_anime(slug: str):
    data = kitsu_animes.fetch_anime(slug=slug)
    repository.create_anime(data)


def download(anime_slug: str, chapter: int, site: str = None, player: str = None):
    pass
