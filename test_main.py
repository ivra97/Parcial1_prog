import unittest
from library_item import load_library_items, checkout_item, count_items, find_by_title
from library_item import Book, Magazine
import os
import tempfile
import csv

class TestLibrary(unittest.TestCase):
    def test_constructor_book_valido(self):
        book = Book("El pepe", 1, "Rodrigo Ochoa", 7000)
        self.assertEqual(book.title, "El pepe")
        self.assertEqual(book.item_id, 1)
        self.assertEqual(book.author, "Rodrigo Ochoa")
        self.assertEqual(book.pages, 7000)

    def test_constructor_book_invalido(self):
        with self.assertRaises(ValueError):
            Book("El pepe", 1, "Rodrigo Ochoa", -10)
        with self.assertRaises(ValueError):
            Book("El pepe", 1, "Rodrigo Ochoa", 0)
        with self.assertRaises(ValueError):
            Book("El pepe", -1, "Rodrigo Ochoa", "cien")
        with self.assertRaises(ValueError):
            Book("El pepe", 1, "Rodrigo Ochoa", "cien")

    def test_constructor_magazine_valido(self):
        magazine = Magazine("National Geographic", 2, 5)
        self.assertEqual(magazine.title, "National Geographic")
        self.assertEqual(magazine.item_id, 2)
        self.assertEqual(magazine.issue_number, 5)

    def test_constructor_magazine_invalido(self):
        with self.assertRaises(ValueError):
            Magazine("National Geographic", 2, -1)
        with self.assertRaises(ValueError):
            Magazine("National Geographic", -2, 5)
        with self.assertRaises(ValueError):
            Magazine("National Geographic", 2, "cinco")

    def test_checkout_book(self):
        book = Book("El pepe", 1, "Rodrigo Ochoa", 7000)
        result = book.checkout("Juan")
        self.assertEqual(result, "Libro 'El pepe' fue prestado a Juan.")

    def test_checkout_magazine(self):
        magazine = Magazine("National Geographic", 2, 5)
        result = magazine.checkout("Maria")
        self.assertEqual(result, "Revista 'National Geographic' con 5 fue prestada a Maria.")

    
    def test_load_library_items(self):
        contiene = [
            ["book", "El pepe", "1", "Rodrigo Ochoa", "7000"],
            ["magazine", "National Geographic", "2", "5"],
            ["unknown", "Titulo desconocido", "3", "Autor Desconocido", "100"]
        ]

        with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8') as tmp:
            writer = csv.writer(tmp)
            writer.writerows(contiene)
            tmp_path = tmp.name

        items = load_library_items(tmp_path)
        os.unlink(tmp_path)

        self.assertEqual(len(items), 2)
        self.assertIsInstance(items[0], (Book, Magazine))
        self.assertIsInstance(items[1], (Book, Magazine))

    def test_checkout_item_funcion(self):
        book = Book("El pepe", 1, "Rodrigo Ochoa", 7000)
        mensaje = checkout_item(book, "Juan")
        self.assertIn("Libro 'El pepe' fue prestado a Juan", mensaje)

        magazine = Magazine("National Geographic", 2, 5)
        mensaje = checkout_item(magazine, "Maria")
        self.assertIn("Revista 'National Geographic' con 5 fue prestada a Maria", mensaje)

    def test_count_items_funcion(self):
        b = Book("El pepe", 1, "Rodrigo Ochoa", 7000)
        m = Magazine("National Geographic", 2, 5)
        total = count_items([b, m])
        self.assertEqual(total, 2)

    def test_find_by_title_funcion(self):
        b1 = Book("El pepe", 1, "Rodrigo Ochoa", 7000)
        b2 = Book("Python para todos", 2, "Romano Luis", 300)
        m1 = Magazine("National Geographic", 3, 5)

        encontrados = find_by_title([b1, b2, m1], "Python para todos")
        self.assertIn(b1, encontrados)
        self.assertIn(b2, encontrados)
        self.assertNotIn(m1, encontrados)

if __name__ == "__main__":
    unittest.main()