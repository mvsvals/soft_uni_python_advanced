def softuni_students(*args, **kwargs):
    output = []
    invalid_students = []
    for course_id, student in sorted(args, key=lambda x: x[1]):
        if course_id in kwargs:
            output.append(f"*** A student with the username {student} has successfully finished the course {kwargs[course_id]}!")
        else:
            invalid_students.append(student)
    if invalid_students:
        output.append("!!! Invalid course students: " + ', '.join(invalid_students))
    return '\n'.join(output)

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
