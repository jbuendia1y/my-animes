
import math

from models.Paginated import MetaPage


MAX_ITEMS = 25


def get_paginated_of_table(cursor, table: str, page: int = None):
    if not page:
        page = 1
    page *= MAX_ITEMS

    cursor.execute("SELECT COUNT(*) FROM %s", table)
    count_tuple = cursor.fetchone()
    total_pages = math.ceil(count_tuple[0] / MAX_ITEMS)

    return MetaPage(
        total_pages=total_pages,
        current_page=page,
        max_items=MAX_ITEMS
    )
