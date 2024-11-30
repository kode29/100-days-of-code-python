def format_name(f_name, l_name):
    """Takes a first and last name and formats it to return the
    title case version of the name"""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("kyle", "perkins"))

