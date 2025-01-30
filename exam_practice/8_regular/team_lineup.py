def team_lineup(*args):
    players_dic = {}
    for name, country in args:
        if not country in players_dic:
            players_dic[country] = []
        players_dic[country].append(name)
    output = []
    for key, value in sorted(players_dic.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f'{key}:')
        for item in value:
            output.append(f"  -{item}")
    return '\n'.join(output)

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
