#!/usr/bin/env python3
''' Simple pagination '''
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The data for the specified page.

        Raises:
            AssertionError: If `page` or `page_size` is not an integer,
            or if `page` or `page_size` is less than or equal to 0.

        """

        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        i = index_range(page, page_size)
        if i[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[i[0]:i[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves a dictionary containing hypermedia pagination information.
        Args:
            page (int): The current page number. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.
        Returns:
            Dict: A dictionary containing the following information:
                - "page": The current page number.
                - "page_size": The number of items per page. If the current
                   page is the last page, it will be set to 0.
                - "data": The data for the current page.
                - "next_page": The next page number. If the current page is
                   the last page, it will be set to None.
                - "prev_page": The previous page number. If the current page
                   is the first page, it will be set to None.
                - "total_pages": The total number of pages.
        """

        dataset_items = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(dataset_items / page_size)

        p = {
            "page": page,
            "page_size": page_size if page < total_pages else 0,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
            }
        return p


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and final index of a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and final
        index of the page.
    """

    final_index = page * page_size
    start_index = final_index - page_size

    return start_index, final_index
