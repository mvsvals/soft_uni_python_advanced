def classify_books(*args, **kwargs):
    books_dict = {'Fiction': {name: 0 for genre, name in args if genre == 'fiction'},
                  'Non-Fiction': {name: 0 for genre, name in args if genre == 'non_fiction'}}
    for isbn, name in kwargs.items():
        if name in books_dict['Fiction']:
            books_dict['Fiction'][name] = isbn
        elif name in books_dict['Non-Fiction']:
            books_dict['Non-Fiction'][name] = isbn
    books_dict['Fiction'] = dict(sorted(books_dict["Fiction"].items(), key=lambda x: x[1]))
    books_dict['Non-Fiction'] = dict(sorted(books_dict["Non-Fiction"].items(), key=lambda x: x[1], reverse=True))
    output = []
    if books_dict['Fiction']:
        output.append('Fiction Books:')
        for name, isbn in books_dict['Fiction'].items():
            output.append(f"~~~{isbn}#{name}")
    if books_dict['Non-Fiction']:
        output.append('Non-Fiction Books:')
        for name, isbn in books_dict['Non-Fiction'].items():
            output.append(f"***{isbn}#{name}")
    return '\n'.join(output)

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))