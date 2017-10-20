Dark Matter Day
===============

This is the webpage for Dark Matter Day 2017 at Durham University. It's just a
basic webpage outlining where and when the event is; I see no reason not to
open source it as an example of using jinja2 templating.

Feel free to do what you want with the source code (hence the MIT license).
I doubt you'll be able to sell it though...

Setup
-----

Requires ```python > 3.6```.

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python3 compile.py
```

This will produce the ```index.html```. If you are wishing to deploy the site
elsewhere, you'll also need to bring the ```static/``` directory along with you
for the images and css.
