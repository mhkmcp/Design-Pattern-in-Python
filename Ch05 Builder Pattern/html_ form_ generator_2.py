
def generate_web_form(text_field_list=[], checkbox_field_list=[]):
    generate_fields = "\n".join(
        map(
            lambda x: '{0}: <br><input type="text" name="{0}"><br>'.format(x),
            text_field_list
        )
    )

    generate_fields += "\n".join(
        map(
            lambda x: '<label><input type="checkbox" id="{0}" value="{0}">{0}<br>'.format(x),
            checkbox_field_list
        )
    )
    return "<form>{fields}</form>".format(fields=generate_fields)


def build_html_form(text_field_list=[], checkbox_field_list=[]):
    with open("form_file-2.html", 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(
                generate_web_form(
                    text_field_list,
                    checkbox_field_list
                )
            )
        )


if __name__ == '__main__':
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awesome", "bad"]
    build_html_form(text_field_list=text_fields, checkbox_field_list=checkbox_fields)