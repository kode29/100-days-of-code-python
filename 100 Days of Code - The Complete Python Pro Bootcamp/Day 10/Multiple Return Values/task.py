def format_name(f_name, l_name):
    """Takes a first and last name and formats it to return the
        title case version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))