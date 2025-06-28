from abc import ABC, abstractmethod
import csv

class LibraryItem(ABC): 
    def __init__(self, title: str , item_id: int ):
        if not title:
            raise (ValueError, "El titulo no debe estar vacio.") 
        if item_id <= 0:
            raise (ValueError, "El ID debe ser positivo.")
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout (self, user:str) -> str:
        pass

class Book (LibraryItem):
    def __init__(self, title, item_id, author:str, pages: int):
        super().__init__(title,item_id)
        if not author or isinstance(author,str):
            raise (ValueError, "El autor no debe estar vacio.")
        if pages <= 0 or isinstance(pages,int):
            raise(ValueError, "El numero de paginas debe ser postivo.")
        self.author = author
        self.pages = pages

    def checkout(self, user):
        return f"Libro'{self.title}'  fue prestado a {user}."
    
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number: int ):
        super().__init__(title,item_id)
        if issue_number <= 0 or isinstance(issue_number,int):
            raise (ValueError, "El numero de emision debe ser positivo.")
        self.issue_number = issue_number

    def checkout(self, user):
        return f"Revista '{self.title}' con '{self.issue_number}'  fue prestada a {user}."
    
    