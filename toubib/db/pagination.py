import math


class Page(object):
    """Pagination for listing patient records"""

    def __init__(self):
        self.pages = None
        self.next_page = None
        self.has_next_page = None
        self.previous_items = None
        self.previous_page = None
        self.has_previous_page = None
        self.page_size = None
        self.total_pages = None
        self.items = None

    def setPageInfo(self, items, page, page_size, total_pages):
        self.items = items
        self.total_pages = total_pages
        self.page_size = len(items)
        self.next_page = None
        self.has_previous_page = page > 1
        self.previous_page = page - 1 if self.has_previous_page else None
        self.previous_items = (page - 1) * page_size
        self.has_next_page = self.previous_items + len(items) < total_pages
        self.next_page = page + 1 if self.has_next_page else None
        self.pages = int(math.ceil(total_pages / float(page_size)))

    def paginate(self, query, page, page_size):
        if page <= 0:
            raise AttributeError("Page needs to be greater than 1")
        if page_size <= 0:
            raise AttributeError("Page size needs to be greater than 1")
        records = query.limit(page_size).offset((page - 1) * page_size).all()
        total = query.count()
        pape = Page()
        page.setPageInfo(records, page, page_size, total)
