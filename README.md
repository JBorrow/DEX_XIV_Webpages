DEX Workshop Jan 2018
=====================

This is the webpage for the Jan 2018 DEX Workshop at Durham University.
It's just a basic webpage outlining where and when the event is; some
information about the local area; and a programme of events for the day.

 I see no reason not to open source it as an example of using jinja2 templating.

Setup
-----

Requires ```python > 3.6```.

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python3 compile.py
```

This will produce the html (static). If you are wishing to deploy the site
elsewhere, you'll also need to bring the ```static/``` directory along with you
for the images and css.
