def gather_credits(credits_needed, *args):
    enrolled_courses = []
    gathered = 0
    for name, course_credits in args:
        if credits_needed > 0 and not name in enrolled_courses:
            enrolled_courses.append(name)
            credits_needed -= course_credits
            gathered += course_credits

    if credits_needed > 0:
        return f"You need to enroll in more courses! You have to gather {credits_needed} credits more."
    else:
        return f"Enrollment finished! Maximum credits: {gathered}." + '\n' + 'Courses: ' + ', '.join(sorted(enrolled_courses))