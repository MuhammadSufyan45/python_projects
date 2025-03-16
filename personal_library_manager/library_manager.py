import os
import json

data_file = 'library.txt'

def Load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return []
    
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)


def add_book(library):
    title = input('Enter the title of the book: ').lower()
    author = input('Enter the author of the book: ').lower()
    year = input('Enter the year of the book: ').lower()
    genre = input('Enter the genre of the book: ').lower()
    read = input('Have you read the book? (yes/no): ').lower()

    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(book)
    save_library(library)
    print(f'Book {title} added successfully!')

def remove_book(library):
    title = input('Enter the title of the book you want to remove: ')
    initial_length = len(library)
    library = [book for book in library if book['title'] != title]
    if len(library) < initial_length:
        save_library(library)
        print(f'Book {title} removed successfully!')
    else:
        print(f'Book {title} not found in the library!')

def search_library(library):
    search_by = input('Enter the field of the book you want to search: ').lower()
    search_term = input(f'Enter the {search_by}: ').lower()
    books = [book for book in library if search_term in book[search_by].lower()]
    if books:
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {book['read']}")
    else:
        print(f'No book found with {search_term} in {search_by}!')

def percentage_read(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage = ( read_books / total_books ) * 100

    print(f'Total books: {total_books}')
    print(f'Percentage read: {percentage:.2f}')

def show_all_book(library):
    if library:
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {book['read']}")
    else:
        print('Library is empty!')

def main():
    library = Load_library()

    while True:
        print('''
        1. Add a book
        2. Remove a book
        3. Search library
        4. Percentage read
        5. Show all books
        6. Exit
        ''')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            percentage_read(library)
        elif choice == '5':
            show_all_book(library)
        elif choice == '6':
            print('Thanks for using the library manager!')
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()