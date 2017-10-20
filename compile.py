"""
Compiler for the basic website. Essentially just opens a yaml file and exposes
the structure as an object to our template.
"""

import jinja2
import yaml

def get_from_filesystem(templates, data_fn):
    """ Takes a list of template names and returns a zipped list of template
    objects and associated data values that are ready for rendering wih the
    render_template function. """

    template_loader = jinja2.FileSystemLoader(searchpath=".")
    template_env = jinja2.Environment(loader=template_loader)

    templates = list(map(template_env.get_template, templates))
    data = get_data(data_fn)
    
    return zip(templates, data)


def get_data(data_fn):
    """ Grabs the data from yaml/md files within the data directory if they
        exist, and if not returns an empty dictionary for that item. """

    data = []

    for item in data_fn:
        this_data = {}  # we will start with empty and add to it.

        # YAML Search
        try:
            with open(f"{item}", "r") as handle:
                this_data = dict(yaml.load(handle), **this_data)

        except FileNotFoundError:
            pass

        data.append(this_data)

    return data

if __name__ == "__main__":
    DATA = [
        "src/data.yaml",
    ]

    TEMPLATES = [
        "src/layout.html",
    ]

    OUTPUT = [
        "index.html",
    ]

    OUT_TEXT = [
        temp.render(**data) for temp, data in get_from_filesystem(
            TEMPLATES, 
            DATA
        )
    ]

    for filename, text in zip(OUTPUT, OUT_TEXT):
        with open(filename, "w") as handle:
            handle.write(text)
