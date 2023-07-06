# books = {
#     "Harry Potter": 10,
#     "Lord of the Rings": 5,
#     "Game of Thrones": 2,
#     "The Hunger Games": 8,
#       "To Kill a Mockingbird": 4
# }
# new_books_shell={}
# book_name=""
# while book_name!="these books only":
#     book_name=input("enter the book name to know how many more books are required:")
#     if book_name in books.keys():
#         quantity=books[book_name]
#         if quantity<10:
#            book_requires=10-quantity
#            new_books_shell[book_requires]= book_requires
#            print(f"{book_name}: {book_requires} more required")
#         else:
#             print(f"{book_name}: already have 10 copies")
#     elif book_name != "these books only":
#         print(f"{book_name}: not found in the library")

# print(new_books_shell) 
    

books = {
    "Harry Potter": 10,
    "Lord of the Rings": 5,
    "Game of Thrones": 2,
    "The Hunger Games": 8,
    "To Kill a Mockingbird": 4
}
def cal_books_order(books):
    new_book={}
    for book,qty in books.items():
        if qty<10:
            new_book[book]=10-qty
    return new_book
cal_books_order(books)  
print(cal_books_order(books))
          