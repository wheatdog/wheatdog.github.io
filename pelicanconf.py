#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tim Liou'
SITENAME = 'String Bulbs'
SITEURL = 'http://localhost:8000'
SITETITLE = SITENAME
SITESUBTITLE = 'Never Wanted To Dance'
SITELOGO = '/images/logo.png'
FAVICON = '/images/favicon.ico'

THEME = "themes/Flex"
PYGMENTS_STYLE = 'monokai'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

DATE_FORMATS = {
    'en': '%b. %d, %Y',
}

COPYRIGHT_YEAR = "2015-2016"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/wheatdog'),
          ('twitter', 'https://twitter.com/wdliou'))

USE_FOLDER_AS_CATEGORY = False
# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
