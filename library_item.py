from abc import ABC, abstractmethod
import csv

class LibraryItem(ABC): 
    def __init__(self, title: str , item_id: int ):
        if not title or not isinstance(title, str):
            raise ValueError("El titulo no debe estar vacio y debe ser una cadena.")
        if item_id <= 0 or not isinstance(item_id, int):
            raise ValueError("El ID debe ser positivo y debe ser un entero.")
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout (self, user:str) -> str:
        pass

class Book (LibraryItem):
    def __init__(self, title, item_id, author:str, pages: int):
        super().__init__(title,item_id)
        if not author or not isinstance(author, str):
            raise ValueError("El autor no debe estar vacio y debe ser una cadena.")
        if pages <= 0 or not isinstance(pages, int):
            raise ValueError("El numero de paginas debe ser positivo y debe ser un entero.")
        self.author = author
        self.pages = pages

    def checkout(self, user):
        return f"Libro '{self.title}'  fue prestado a {user}."
    
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number: int ):
        super().__init__(title,item_id)
        if issue_number <= 0 or not isinstance(issue_number, int):
            raise ValueError("El numero de emision debe ser positivo y debe ser un entero.")
        self.issue_number = issue_number

    def checkout(self, user):
        return f"Revista '{self.title}' con {self.issue_number} fue prestada a {user}."
    

def load_library_items(path: str) -> list[LibraryItem]:
    items = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try: 
                tipo = row[0].strip().lower()
                titulo = row[1].strip()
                item_id = int(row[2].strip())

                if tipo == "book":
                    autor = row[3].strip()
                    paginas = int(row[4].strip())
                    items.append(Book(titulo, item_id, autor, paginas))
                elif tipo == "magazine":
                    issues_number = int(row[3].strip())
                    items.append(Magazine(titulo, item_id, issues_number))

                else:
                    raise ValueError(f"Tipo de item desconocido: {tipo}")
            except ValueError as e:
                print(f"Error al cargar el item: {e}. Fila: {row}")
    return items



def checkout_item(item: LibraryItem, user: str) -> str:
    if not isinstance(item, LibraryItem):
        raise TypeError("El item debe ser una instancia de LibraryItem.")
    return item.checkout(user)



def count_items(items: list[LibraryItem]) -> int:
    if not isinstance(items, list):
        raise TypeError("Los items deben ser una lista.")
    return len(items)



def find_by_title(items: list[LibraryItem], title: str) -> list[LibraryItem]:
    if not isinstance(items, list):
        raise TypeError("Los items deben ser una lista.")
    if not title:
        raise ValueError("El titulo no debe estar vacio.")
    
    return [item for item in items if item.title.lower() == title.lower()]

if __name__ == "__main__":

    b = Book("El pepe", 1, "Rodrigo Ochoa", 7000)
    m = Magazine("National Geographic", 2, 2023)

    print(b.checkout("Juan"))
    print(m.checkout("Maria"))      
    
    