export interface EndpointPage<T> {
  current_page: number;
  total_pages: number;
  data: T[];
}

export interface Page<T> {
  currentPage: number;
  totalPages: number;
  data: T[];
}
