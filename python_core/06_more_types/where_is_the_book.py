books: dict[str, str] = {
    "Life of Pi": "Adventure Fiction", 
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics", 
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book:str = input()

#change this part to use the .get() method
result:str = books.get(book, "Book not found")

print(result)


