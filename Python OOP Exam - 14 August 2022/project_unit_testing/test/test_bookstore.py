from project.bookstore import Bookstore
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.my_bookstore = Bookstore(5)

    def test___init__(self):
        self.assertEqual(self.my_bookstore.books_limit, 5)
        self.assertEqual(self.my_bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.my_bookstore.total_sold_books, 0)

    def test___book_limit_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.my_bookstore.books_limit = 0
        self.assertEqual(str(ve.exception), f"Books limit of 0 is not valid")

        with self.assertRaises(ValueError) as ve:
            self.my_bookstore.books_limit = -1
        self.assertEqual(str(ve.exception), f"Books limit of -1 is not valid")

    def test___len__(self):
        self.my_bookstore.availability_in_store_by_book_titles = {'Harry Potter': 3, 'Lord Of the Rings': 1}
        self.assertEqual(len(self.my_bookstore), 4)
        self.assertEqual(len(self.my_bookstore.availability_in_store_by_book_titles), 2)

        self.my_bookstore.availability_in_store_by_book_titles = {}
        self.assertEqual(len(self.my_bookstore), 0)
        self.assertEqual(len(self.my_bookstore.availability_in_store_by_book_titles), 0)

        self.my_bookstore.availability_in_store_by_book_titles = {'Harry Potter': 1, 'Lord Of the Rings': 1}
        self.assertEqual(len(self.my_bookstore), 2)
        self.assertEqual(len(self.my_bookstore.availability_in_store_by_book_titles), 2)

    def test___receive_book(self):
        self.my_bookstore.availability_in_store_by_book_titles = {'Harry Potter': 3, 'Lord Of the Rings': 1}

        with self.assertRaises(Exception) as ex:
            self.my_bookstore.receive_book('The green way', 2)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

        result = self.my_bookstore.receive_book('The green way', 1)
        self.assertEqual(result, f"1 copies of The green way are available in the bookstore.")
        self.assertEqual(self.my_bookstore.availability_in_store_by_book_titles, {'Harry Potter': 3,
                                                                                  'Lord Of the Rings': 1,
                                                                                  'The green way': 1})
        self.assertEqual(len(self.my_bookstore), 5)
        self.assertEqual(len(self.my_bookstore.availability_in_store_by_book_titles), 3)

        self.my_bookstore.books_limit = 10

        result = self.my_bookstore.receive_book('The green way', 1)
        self.assertEqual(result, f"2 copies of The green way are available in the bookstore.")
        self.assertEqual(self.my_bookstore.availability_in_store_by_book_titles, {'Harry Potter': 3,
                                                                                  'Lord Of the Rings': 1,
                                                                                  'The green way': 2})
        self.assertEqual(len(self.my_bookstore), 6)
        self.assertEqual(len(self.my_bookstore.availability_in_store_by_book_titles), 3)

        self.my_bookstore.receive_book('One night in Bulgaria', 2)
        self.assertEqual(self.my_bookstore.availability_in_store_by_book_titles, {'Harry Potter': 3,
                                                                                  'Lord Of the Rings': 1,
                                                                                  'The green way': 2,
                                                                                  'One night in Bulgaria': 2})

    def test___sell_book(self):
        self.my_bookstore.availability_in_store_by_book_titles = {'Harry Potter': 3, 'Lord Of the Rings': 1}

        with self.assertRaises(Exception) as ex:
            self.my_bookstore.sell_book('The green way', 1)
        self.assertEqual(str(ex.exception), f"Book The green way doesn't exist!")

        with self.assertRaises(Exception) as ex:
            self.my_bookstore.sell_book('Harry Potter', 4)
        self.assertEqual(str(ex.exception), f"Harry Potter has not enough copies to sell. Left: 3")

        result = self.my_bookstore.sell_book('Harry Potter', 2)
        self.assertEqual(result, f"Sold 2 copies of Harry Potter")
        self.assertEqual(self.my_bookstore.availability_in_store_by_book_titles, {'Harry Potter': 1, 'Lord Of the Rings': 1})
        self.assertEqual(len(self.my_bookstore), 2)
        self.assertEqual(len(self.my_bookstore.availability_in_store_by_book_titles), 2)
        self.assertEqual(self.my_bookstore.total_sold_books, 2)

        self.my_bookstore.sell_book('Harry Potter', 1)
        self.assertEqual(self.my_bookstore.total_sold_books, 3)

        self.my_bookstore.sell_book('Lord Of the Rings', 1)
        self.assertEqual(len(self.my_bookstore), 0)
        self.assertEqual(len(self.my_bookstore.availability_in_store_by_book_titles), 2)
        self.assertEqual(self.my_bookstore.total_sold_books, 4)
        self.assertEqual(self.my_bookstore.availability_in_store_by_book_titles, {'Harry Potter': 0, 'Lord Of the Rings': 0})

    def test___str__(self):
        self.my_bookstore.availability_in_store_by_book_titles = {'Harry Potter': 3, 'Lord Of the Rings': 1}
        expected_result = ['Total sold books: 0',
                           'Current availability: 4',
                           f" - Harry Potter: 3 copies",
                           f" - Lord Of the Rings: 1 copies"
        ]
        self.assertEqual(str(self.my_bookstore), '\n'.join(expected_result))

        self.my_bookstore.availability_in_store_by_book_titles = {}
        new_expected_result = ['Total sold books: 0',
                           'Current availability: 0',
                               ]
        self.assertEqual(str(self.my_bookstore), '\n'.join(new_expected_result))

        self.my_bookstore.availability_in_store_by_book_titles = {'Harry Potter': 3, 'Lord Of the Rings': 1}
        self.my_bookstore.sell_book('Harry Potter', 2)
        self.my_bookstore.sell_book('Lord Of the Rings', 1)

        final_expected_result = ['Total sold books: 3',
                           'Current availability: 1',
                           f" - Harry Potter: 1 copies",
                                 f" - Lord Of the Rings: 0 copies"
        ]
        self.assertEqual(str(self.my_bookstore), '\n'.join(final_expected_result))