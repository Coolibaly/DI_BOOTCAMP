# Pagination System

import math


class Pagination:

    def __init__(self, items=None, page_size=10):

        # If no items provided, use empty list
        if items is None:
            items = []

        self.items = items
        self.page_size = page_size
        self.current_idx = 0  # internal page index (starts at 0)

        # total pages using ceiling division
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    # Get items on current page
    def get_visible_items(self):

        start = self.current_idx * self.page_size
        end = start + self.page_size

        return self.items[start:end]

    # Go to specific page (1-based)
    def go_to_page(self, page_num):

        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range")

        self.current_idx = page_num - 1
        return self

    # First page
    def first_page(self):

        self.current_idx = 0
        return self

    # Last page
    def last_page(self):

        self.current_idx = self.total_pages - 1
        return self

    # Next page
    def next_page(self):

        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1

        return self

    # Previous page
    def previous_page(self):

        if self.current_idx > 0:
            self.current_idx -= 1

        return self

    # String representation (bonus)
    def __str__(self):

        page_items = self.get_visible_items()

        return "\n".join(page_items)


# TESTS

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print("ValueError:", e)

try:
    p.go_to_page(0)
except ValueError as e:
    print("ValueError:", e)




print(
    p.first_page()
     .next_page()
     .next_page()
     .next_page()
     .get_visible_items()
)