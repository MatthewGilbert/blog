#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

LOAD_CONTENT_CACHE = False

AUTHOR = u'Matthew Gilbert'
SITENAME = u'matthewdgilbert'
SITEURL = ''

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

CUSTOM_CSS = 'static/custom.css'
# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'pdfs', 'extra/custom.css', 'extra/CNAME']

ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
            'extra/custom.css': {'path': 'static/custom.css'},
            'extra/CNAME': {'path': 'CNAME'}
}

HIDE_SIDEBAR = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

BANNER = 'images/banner.jpg'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins']

PLUGINS = ['ipynb.markup']

THEME = 'theme'

ARTICLE_EXCLUDES = ['.ipynb_checkpoints'] 
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False

DEFAULT_CATEGORY = 'finance'

BOOTSTRAP_THEME = 'readable-old'
PYGMENTS_STYLE = 'github'

CUSTOM_LICENSE='The views expressed on this site are my own and do not reflect those of my employer'
