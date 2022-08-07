from typing import List
from db.connection import connection
from libs.paginated import get_paginated_of_table
from models.Anime import Anime
from libs import kitsu_animes
from models.Paginated import Paginated, create_paginated


def create_anime_formatted(data: tuple) -> Anime:
    # (ID, SLUG, IMAGE, TITLE, SYNOPSIS, TOTAL_CHAPTERS)
    return Anime(
        id=data[0],
        slug=data[1],
        image=data[2],
        title=data[3],
        synopsis=data[4],
        total_chapters=data[5]
    )


def get_animes() -> Paginated[Anime]:
    return kitsu_animes.fetch_animes()


def get_anime(slug: str):
    cursor = connection().cursor()
    cursor.execute("SELECT * FROM animes WHERE slug = %s", slug)
    data = create_anime_formatted(cursor.fetchone())
    return data


def get_my_animes(user_id: int, page: int = None) -> Paginated[Anime]:
    cursor = connection().cursor()
    meta = get_paginated_of_table(cursor, "my_animes", page)
    query = """
    SELECT * 
    FROM my_animes 
    WHERE user_id = %s 
    LIMIT %s,%s
    """
    cursor.execute(
        query,
        (user_id, meta.max_items, (meta.current_page * meta.max_items) - 1)
    )
    data = [create_anime_formatted(anime) for anime in cursor.fetchall()]
    p = create_paginated(data, meta.total_pages, meta.current_page)
    return p


def create_anime(data: dict):
    conn = connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO 
    animes(image,slug,title,synopsis,total_chapters) 
    VALUES(%s,%s,%s,%s,%s)
    """
    cursor.execute(query, (
        data["image"],
        data["slug"],
        data["title"],
        data["synopsis"],
        data["total_chapters"]
    ))
    slug = data["slug"]
    print(f"ANIME {slug} CREATED !")
    conn.commit()
