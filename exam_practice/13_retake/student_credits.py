def students_credits(*args):
    courses = {}
    output = []
    for x in args:
        course_name, credits, max_test_points, diyans_points = [int(x) if x.isdigit() else x for x in x.split("-")]
        percentage = diyans_points / max_test_points
        courses[course_name] = credits * percentage
    diyan_total_credits = sum(x[1] for x in courses.items())
    if diyan_total_credits >= 240:
        output.append(f"Diyan gets a diploma with {diyan_total_credits:.1f} credits.")
    else:
        output.append(f"Diyan needs {240 - diyan_total_credits:.1f} credits more for a diploma.")
    for x in sorted(courses.items(), key=lambda x: -x[1]):
        output.append(f"{x[0]} - {x[1]:.1f}")
    return '\n'.join(output)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)