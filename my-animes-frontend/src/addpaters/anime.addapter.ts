import { Anime } from "../repositories/animes.repository";

export interface IAnimeEndpoint {
  id: number;
  image: string;
  slug: string;
  title: string;
  synopsis: string;

  total_chapters: number;

  chapters?: any[];
  prequel?: string;
  sequel?: string;

  user_id: number;
}

export function createAnimeAddapted(ed: IAnimeEndpoint) {
  const formatted: Anime = {
    id: ed.id,
    title: ed.title,
    image: ed.image,
    slug: ed.slug,
    synopsis: ed.synopsis,
    sequel: ed.sequel,
    prequel: ed.prequel,
    totalChapters: ed.total_chapters,
    userId: ed.user_id,
    chapters: ed.chapters,
  };

  return formatted;
}
