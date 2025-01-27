
def list_roman_emperors(*args, **kwargs):
    output = []
    successful_emperors = [[x[0], int(kwargs[x[0]])] for x in args if x[1]]
    failed_emperors = [[x[0], int(kwargs[x[0]])] for x in args if not x[1]]
    successful_emperors.sort(key=lambda x: (-x[1], x[0]))
    failed_emperors.sort(key=lambda x: (x[1], x[0]))
    output.append(f"Total number of emperors: {len(successful_emperors) + len(failed_emperors)}")
    if successful_emperors:
        output.append("Successful emperors:")
        for emp in successful_emperors:
            output.append(f"****{emp[0]}: {emp[1]}")
    if failed_emperors:
        output.append("Unsuccessful emperors:")
        for emp in failed_emperors:
            output.append(f"****{emp[0]}: {emp[1]}")
    return '\n'.join(output)

print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))