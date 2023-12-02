book_list = []
wishlist = []

book_name = input ("Enter the name of a book you own: ")
book_list.append(book_name)

book_name = input ("Enter the name of another book you own (or press 'Enter' to skip): ")

if book_name:
    book_list.append(book_name)

print(f"\nYour library: {book_list}\n")

book_name = input("Enter the name of a book you wish to have in the future: ")
wishlist.append(book_name)

book_name = input("Enter the name of another book you wish to have in the future (or press 'Enter' to skip): ")
if book_name:
    wishlist.append(book_name)

print(f"\nYour wishlist: {wishlist}\n")

acquired_book = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")

if acquired_book in wishlist:
    wishlist.remove(acquired_book)
    if acquired_book in book_list:
        print(f"Your book {acquired_book} is in your library.")
    else:
        book_list.append(acquired_book)

print(f"\nupdated library: {book_list}")
print(f"updated wishlist: {wishlist}\n")

donated_book = input("Enter the name of a book you want to donate (or press 'Enter' to skip): ")

if donated_book in book_list:
    book_list.remove(donated_book)
    print(f"\nFinal library after donation: {book_list}\n")
else:
    print(f"\nFinal library: {book_list}\n")

