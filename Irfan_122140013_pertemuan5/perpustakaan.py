from abc import ABC, abstractmethod

# Abstract base class
class LibraryItem(ABC):
    def __init__(self, item_id, title, publisher):
        self._item_id = item_id
        self._title = title
        self._publisher = publisher

    @abstractmethod
    def display_info(self):
        pass

    @property
    def title(self):
        return self._title

    @property
    def item_id(self):
        return self._item_id

# Subclass Book
class Book(LibraryItem):
    def __init__(self, item_id, title, publisher, author, pages):
        super().__init__(item_id, title, publisher)
        self.__author = author  # private
        self.__pages = pages    # private

    def display_info(self):
        print(f"[Book] ID: {self._item_id}, Title: {self._title}, Publisher: {self._publisher}, Author: {self.__author}, Pages: {self.__pages}")

# Subclass Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, publisher, issue_number):
        super().__init__(item_id, title, publisher)
        self.__issue_number = issue_number

    def display_info(self):
        print(f"[Magazine] ID: {self._item_id}, Title: {self._title}, Publisher: {self._publisher}, Issue: {self.__issue_number}")

# Library class
class Library:
    def __init__(self):
        self.__items = []  # private list of items

    def add_item(self, item: LibraryItem):
        self.__items.append(item)
        print(f"Item '{item.title}' berhasil ditambahkan.")

    def display_all_items(self):
        if not self.__items:
            print("Tidak ada item dalam perpustakaan.")
        else:
            print("\nDaftar Item di Perpustakaan:")
            for item in self.__items:
                item.display_info()

    def search_by_title(self, keyword):
        print(f"\nHasil pencarian untuk judul yang mengandung '{keyword}':")
        found = False
        for item in self.__items:
            if keyword.lower() in item.title.lower():
                item.display_info()
                found = True
        if not found:
            print("Tidak ditemukan item dengan judul tersebut.")

    def search_by_id(self, item_id):
        print(f"\nMencari item dengan ID: {item_id}")
        for item in self.__items:
            if item.item_id == item_id:
                item.display_info()
                return
        print("Item dengan ID tersebut tidak ditemukan.")

# --- Contoh penggunaan ---
if __name__ == "__main__":
    library = Library()

    book1 = Book("B001", "Python Programming", "Informatika", "John Doe", 320)
    magazine1 = Magazine("M001", "Tech Today", "TechMedia", 45)

    library.add_item(book1)
    library.add_item(magazine1)

    library.display_all_items()
    library.search_by_title("Python")
    library.search_by_id("M001")
    library.search_by_id("X999")
