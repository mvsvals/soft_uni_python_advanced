
def draw_cards(*args, **kwargs):
    output = []
    monster_cards = [f'  ***{x[0]}' for x in args if x[1] == 'monster'] + [f'  ***{key}' for key, value in kwargs.items() if value == 'monster']
    spell_cards = [f'  $$${x[0]}' for x in args if x[1] == 'spell'] + [f'  $$${key}' for key, value in kwargs.items() if value == 'spell']
    if monster_cards:
        output.append("Monster cards:")
        for card in sorted(monster_cards, reverse=True):
            output.append(card)
    if spell_cards:
        output.append("Spell cards:")
        for card in sorted(spell_cards):
            output.append(card)
    return '\n'.join(output)

print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))