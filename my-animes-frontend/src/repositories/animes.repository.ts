import axios from "axios";
import {
  createAnimeAddapted,
  IAnimeEndpoint,
} from "../addpaters/anime.addapter";
import { createPageAddapted } from "../addpaters/page.addapter";
import { baseURL } from "../constants";
import { EndpointPage, Page } from "../interfaces";

export interface Anime {
  id: number;
  image: string;
  slug: string;
  title: string;
  synopsis: string;

  totalChapters: number;

  chapters?: any[];
  prequel?: string;
  sequel?: string;

  userId: number;
}

const url = baseURL + "/animes";

export const getAnimes = async (): Promise<Page<Anime>> => {
  const res = await axios.get<EndpointPage<Anime>>(url).then((v) => ({
    ...v,
    data: createPageAddapted<Anime>(v.data),
  }));
  return res.data;
};

export const getAnime = async (slug: string): Promise<Anime> => {
  const res = await axios.get<IAnimeEndpoint>(url + "/" + slug).then((v) => ({
    ...v,
    data: createAnimeAddapted(v.data),
  }));
  return res.data;
};
