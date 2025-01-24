

def fill_the_box(height:int, length:int, width:int, *args):
    box_volume = height * length * width

    boxes = 0
    for item in args:
        if item == 'Finish':
            break
        boxes += item

    if box_volume > boxes:
        return f'There is free space in the box. You could put {box_volume - boxes} more cubes.'
    return f'No more free space! You have {boxes - box_volume} more cubes.'