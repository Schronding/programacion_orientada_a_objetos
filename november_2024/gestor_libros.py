class BookAdministrator:
    def __init__(self):
        self.libros = []

    def addBooks(self, libro):
        self.libros.append(libro)
        print(f"Libro {libro} agregado.")

    def deleteBooks(self, libro):
        self.libros.remove(libro)
        print(f"Libro {libro} eliminado.")

class DisplayBooks:
    def show_media(self, books):
        for book in books:
            print(book)

class BookDataBase:
    def __init__(self, db):
        self.db = db

    def store_books(self):
        output = "libros.txt"
        with open(output, 'w') as file:
            for libro in self.db:
                file.write(f"{libro}\n")
            print(f"Books saved in {output}")
        

biblioteca_ENES = BookAdministrator()

biblioteca_ENES.addBooks("The 48 Laws of Power")
biblioteca_ENES.addBooks("Emperor's New Mind")

exposicion = DisplayBooks()

exposicion.show_media(biblioteca_ENES.libros)

hileras = BookDataBase(biblioteca_ENES.libros)

hileras.store_books()

