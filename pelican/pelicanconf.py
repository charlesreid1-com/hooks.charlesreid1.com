#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import markdown

AUTHOR = u'charlesreid1'
SITENAME = u'charlesreid1 hooks'
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

INTROBKG='theme/img/intro-bg-rigging.jpg'
LINKSBKG='theme/img/links-bg-mast.jpg'

# img/ should be in content/
# available at <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "captain hook"
SITE_DESCRIPTION = "a webhook server for charlesreid1 hooks"
GITEA_URL = "https://git.charlesreid1.com/charlesreid1/hooks.charlesreid1.com"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "About"

ABOUT_TITLE = "about hooks.charlesreid1.com"

ABOUT_TEXT = """
**What is a webhook?**

A webhook is just an HTTP request sent by one server to another
when an event happens. Think of it as a digital representation of a 
real-world event. You can set up webhooks for github repositories,
dockerhub builds, changes to domain names, or anything else you 
can imagine.

<br />

**What is a webhook server?**

A webhook server is just a fancy name for an HTTP server that can 
accept webhooks from other servers. A webhook server is set up with 
various endpoints for various webhooks, and it can fire off other 
webhooks, run programs, or create data.

<br />

**What is Captain Hook?**

Captain Hook is a webhook server running on Python's 
Flask library. Flask is used to create endpoints for 
different services like git.charlesreid1.com or 
Github.com.

<br />

**Where can I find Captain Hook?**

Captain Hook is available at 
[git.charlesreid1.com/bots/b-captain-hook](https://git.charlesreid1.com/bots/b-captain-hook).
"""

ABOUT_DESCRIPTION = about_md.convert(ABOUT_TEXT)



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
            }
            #'dockerhub': {
            #    'icon' : 'fa-cloud',
            #    'text' : 'hub.docker.com webhooks',
            #    'url_short' : 'hub.docker.com/r/charlesreid1',
            #    'url_full' : 'https://hub.docker.com/r/charlesreid1'
            #}
    }
    
    
    descr = ""
    
    for endpoint in hooks.keys():

        params = hooks[endpoint]

        descr += "<p>&nbsp;</p>\n\n"
        descr += "<h3 style=\"text-transform: lowercase;\"><code>https://hooks.charlesreid1.com/webhook</code></h3>\n\n"
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
