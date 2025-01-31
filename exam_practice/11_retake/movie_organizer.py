def movie_organizer(*args):
    movies_dict = {}
    output = []
    for movie_name, movie_genre in args:
        if movie_genre not in movies_dict:
            movies_dict[movie_genre] = []
        movies_dict[movie_genre].append(movie_name)
    movies_dict = dict(sorted(movies_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for genre, movies in movies_dict.items():
        output.append(f"{genre} - {len(movies)}")
        for movie in sorted(movies):
            output.append(f'* {movie}')
    return '\n'.join(output)

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))