
def generate_head(title):
    return '<meta charset = "UTF-8"><title> {} </title>'.format(title)


def generate_web_form(field_list):
    generate_fields = "\n".join(
        map(
            lambda x: '{0}: <br><input type="text" name="{0}"><br>'.format(x),
            field_list
        )
    )
    return "<form>{fields}</form>".format(fields=generate_fields)


def build_html_form(fields):
    with open("form_file.html", 'w') as f:
        f.write(
            "<html><head>{}</head><body>{}</body></html>".format(generate_head('Humayun Kabir'), generate_web_form(fields))
        )


if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    build_html_form(fields)
