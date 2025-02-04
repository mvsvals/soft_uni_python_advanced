def add_songs(*args):
    songs = {}
    for song, lyrics in args:
        if song not in songs:
            songs[song] = []
        songs[song].extend(lyrics)
    output = []
    for song, lyrics in songs.items():
        output.append(f"- {song}")
        for lyric in lyrics:
            output.append(lyric)
    return '\n'.join(output)



print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))