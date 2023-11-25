from math import ceil


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        if len(self.photos) == self.pages and len(self.photos[-1]) == 4:
            return "No more free slots"
        find_free_space = 0
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                find_free_space = i
                break
        self.photos[find_free_space].append(label)
        return f"{label} photo added successfully on page {find_free_space + 1} slot {len(self.photos[find_free_space])}"

    def display(self):
        result = ['-----------']
        for page in self.photos:
            photos_on_page = []
            for pic in page:
                photos_on_page.append('[]')
            result.append(' '.join(photos_on_page))
            result.append("-----------")
        return '\n'.join(result)
