"""
Compiler for the basic website. Essentially just opens a yaml file and exposes
the structure as an object to our template.
"""

import jinja2
import yaml

import numpy as np


def get_from_filesystem(templates, data_fn, shared_data=None):
    """ Takes a list of template names and returns a zipped list of template
    objects and associated data values that are ready for rendering wih the
    render_template function. """

    template_loader = jinja2.FileSystemLoader(searchpath="./src")
    template_env = jinja2.Environment(loader=template_loader)
    template_env.filters["talk_grab"] = talk_grab

    templates = list(map(template_env.get_template, templates))


    shared = get_data(shared_data)
    data = get_data(data_fn)

    if len(shared) == 1:
        shared = shared * len(data)

    out_data = [dict(d, **s) for d, s in zip(data, shared)]
    
    return zip(templates, out_data)


def talk_grab(name):
    """
    Grab a talk
    """

    data = np.loadtxt("src/talks.csv", usecols=(0, 1), dtype=str, delimiter=",")

    where = np.where(data[:, 0] == name)

    filename = data[where, 1]

    try:
        return filename[0][0]
    except:
        return ""


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
    SHARED_DATA = [
        "src/shared.yaml",
    ]

    DATA = [
        "src/home.yaml",
        "src/submit.yaml",
        "src/info.yaml",
        "src/prog.yaml"
    ]

    TEMPLATES = [
        "home.html",
        "submit.html",
        "info.html",
        "prog.html"
    ]

    OUTPUT = [
        "index.html",
        "submit.html",
        "information.html",
        "programme.html"
    ]

    OUT_TEXT = [
        temp.render(**data) for temp, data in get_from_filesystem(
            TEMPLATES, 
            DATA,
            SHARED_DATA
        )
    ]

    for filename, text in zip(OUTPUT, OUT_TEXT):
        with open(filename, "w") as handle:
            handle.write(text)
