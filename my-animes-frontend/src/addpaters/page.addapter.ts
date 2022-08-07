import { EndpointPage, Page } from "../interfaces";

export function createPageAddapted<T>(ed: EndpointPage<T>) {
  const formatted: Page<T> = {
    currentPage: ed.current_page,
    totalPages: ed.total_pages,
    data: ed.data,
  };
  return formatted;
}
