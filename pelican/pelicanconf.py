#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'charlesreid1'

SITENAME = u'charlesreid1 pages'

SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

# hooks use sunflower yellow
INTROCOLOR  = "#fff"
ACOLOR      = "#edac00"
AHOVERCOLOR = "#b48400"
BRIGHTCOLOR = "#f1ca1d"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "captain hook"
SITE_DESCRIPTION = "a webhook server for charlesreid1 hooks"
GITEA_URL = "https://git.charlesreid1.com/charlesreid1/hooks.charlesreid1.com"

# ---

# include <p> tags in the description

ABOUT_TITLE = "about hooks.charlesreid1.com"

ABOUT_DESCRIPTION = """
<p>
<a href="https://git.charlesreid1.com/bots/b-captain-hook">hooks on git.charlesreid1.com</a>
</p>

<p>&nbsp;</p>

<p><b>What is a webhook?</b></p>

<p>A webhook is just an HTTP request sent by one server to another
when an event happens. Think of it as a digital representation of a 
real-world event. You can set up webhooks for github repositories,
dockerhub builds, changes to domain names, or anything else you 
can imagine.</p>

<p>&nbsp;</p>

<p><b>What is a webhook server?</b></p>

<p>A webhook server is just a fancy name for an HTTP server that can 
accept webhooks from other servers. A webhook server is set up with 
various endpoints for various webhooks, and it can fire off other 
webhooks, run programs, or create data.
</p>

<p>&nbsp;</p>

<p><b>What is captain hook?</b></p>

<p>Captain Hook is a webhook server running on Python's 
Flask library. Flask is used to create endpoints for 
different services like git.charlesreid1.com or 
github.com.</p>

<p>&nbsp;</p>

<p><b>Where can I find Captain Hook?</b></p>

<p>Captain Hook is available at <a href="https://git.charlesreid1.com/bots/b-captain-hook">git.charlesreid1.com</a>.
</p>
"""


# ---


# This is where we document various webhook endpoints.

def make_links():
    descr = ""

    hooks = {
            'gitea': {
                'icon' : 'fa-code-fork',
                'text' : 'gitea webhooks',
                'url_short' : 'git.charlesreid1.com',
                'url_full' : 'https://git.charlesreid1.com'
            },
            'github': {
                'icon' : 'fa-github',
                'text' : 'github webhooks',
                'url_short' : 'github.com/charlesreid1',
                'url_full' : 'https://github.com/charlesreid1'
            },
            'dockerhub': {
                'icon' : 'fa-cloud',
                'text' : 'dockerhub webhooks',
                'url_short' : 'dockerhub.com/r/charlesreid1',
                'url_full' : 'https://dockerhub.com/r/charlesreid1'
            }
    }
    
    
    descr = ""
    
    for endpoint in hooks.keys():

        params = hooks[endpoint]

        descr += "<p>&nbsp;</p>\n\n"
        descr += "<h3 style=\"text-transform: lowercase;\"><code>https://hooks.charlesreid1.com/%s</code></h3>\n\n"%(endpoint)
        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(params['url_full'])
        descr += "<i class=\"fa fa-fw fa-2x %s\"></i> "%(params['icon'])
        descr += "%s webhook endpoint"%(endpoint)
        descr += "</a></p>\n\n"
    
    descr += "\n"

    return descr

LINKS_TITLE = "Captain Hook Endpoints"

LINKS_DESCRIPTION = make_links()


# ---


CONTACT_TITLE = "Contact charlesreid1"

CONTACT_DESCRIPTION = """<p>Get in touch!</p>
<p><a href="mailto:charles@charlesreid1.com">charles (at) charlesreid1.com</a></p>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

