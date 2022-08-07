from typing import List
from pydantic import BaseModel

from models.Chapter import Chapter


class CreateAnime(BaseModel):
    slug: str


class Anime(BaseModel):
    id: int = None
    slug: str
    image: str
    title: str
    synopsis: str
    total_chapters: int

    sequel: str = None
    prequel: str = None
    chapters: List[Chapter] = None

    user_id: int = None
