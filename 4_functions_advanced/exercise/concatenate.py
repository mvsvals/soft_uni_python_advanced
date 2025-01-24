def concatenate(*args, **kwargs):
    final_string = ''.join(args)
    for key, value in kwargs.items():
        final_string = final_string.replace(key, value)
    return final_string
