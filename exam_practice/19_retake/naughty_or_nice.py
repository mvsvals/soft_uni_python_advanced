def naughty_or_nice_list(input_list: list, *args, **kwargs):
    santa_list = input_list
    output_list = {'Nice': [], 'Naughty': []}

    def check_occurences(occurence_type, list_type, input_data):
        if occurence_type == 'number':
            ocurrences = [x for x in santa_list if x[0] == input_data]
        elif occurence_type == 'name':
            ocurrences = [x for x in santa_list if x[1] == input_data]
        if len(ocurrences) == 1:
            output_list[list_type].append(ocurrences[0][1])
            santa_list.remove(ocurrences[0])

    for command in args:
        counting_number, list_type = int(command.split('-')[0]), command.split('-')[1]
        check_occurences('number', list_type, counting_number)

    for name, list_type in kwargs.items():
        check_occurences('name', list_type, name)

    if santa_list:
        output_list['Not found'] = [x[1] for x in santa_list]

    result = []
    for list_type, names in output_list.items():
        if names:
            result.append(f"{list_type}: {', '.join(names)}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))