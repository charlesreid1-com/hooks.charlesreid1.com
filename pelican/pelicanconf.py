#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "captain hook"
SITE_DESCRIPTION = "a webhook server for charlesreid1 hooks"

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
# Add links to wiki pages, flask wiki page, 
# blog posts, etc.


# ---


# This is where we document various webhook endpoints.

# include <p> tags in the description

def make_links_description():
    descr = ""

    botlinks = {
            'twitter' : {
                'Apollo Space Junk Bot Flock' : 'https://twitter.com/charlesreid1/lists/space-junk-botflock',
                'Paradise Lost Bot Flock' :     'https://twitter.com/charlesreid1/lists/miltonbotflock',
                'Ginsberg Bot Flock' :          'https://twitter.com/charlesreid1/lists/ginsbergbotflock',
                'Math Tripos Bot' :             'https://twitter.com/math_tripos'
            },

            'git.charlesreid1.com' : {
                'Rainbow Mind Machine' :        'https://git.charlesreid1.com/bots/b-rainbow-mind-machine',
                'Apollo Space Junk Bot Flock' : 'https://git.charlesreid1.com/bots/b-apollo',
                'Paradise Lost Bot Flock' :     'https://git.charlesreid1.com/bots/b-milton',
                'Ginsberg Bot Flock' :          'https://git.charlesreid1.com/bots/b-ginsberg',
                'Math Tripos Bot' :             'https://git.charlesreid1.com/bots/b-tripos'
            },

            'pages.charlesreid1.com' : {
                'Rainbow Mind Machine' :        'https://pages.charlesreid1.com/rainbow-mind-machine',
                'Apollo Space Junk Bot Flock' : 'https://pages.charlesreid1.com/apollo',
                'Paradise Lost Bot Flock' :     'https://pages.charlesreid1.com/milton',
                'Ginsberg Bot Flock' :          'https://pages.charlesreid1.com/ginsberg',
                'Math Tripos Bot' :             'https://pages.charlesreid1.com/tripos'
            },

            'github (mirror)' : {
                'Rainbow Mind Machine' :        'https://github.com/charlesreid1/rainbow-mind-machine',
                'Apollo Space Junk Bot Flock' : 'https://github.com/charlesreid1/apollospacejunk',
                'Paradise Lost Bot Flock' :     'https://github.com/charlesreid1/milton',
                'Ginsberg Bot Flock' :          'https://github.com/charlesreid1/ginsberg',
                'Math Tripos Bot' :             'https://github.com/charlesreid1/tripos-bot'
            },

            'github pages (mirror)' : {
                'Rainbow Mind Machine' :        'https://charlesreid1.github.io/rainbow-mind-machine',
                'Apollo Space Junk Bot Flock' : 'https://charlesreid1.github.io/apollospacejunk',
                'Paradise Lost Bot Flock' :     'https://charlesreid1.github.io/milton',
                'Ginsberg Bot Flock' :          'https://charlesreid1.github.io/ginsberg',
                'Math Tripos Bot' :             'https://charlesreid1.github.io/tripos-bot'
            }

    }

    fa_icons = {
            'twitter' : '<i class="fa fa-twitter fa-fw"></i>',
            'git.charlesreid1.com' : '<i class="fa fa-code-fork fa-fw"></i>',
            'pages.charlesreid1.com' : '<i class="fa fa-file-o fa-fw"></i>',
            'github (mirror)' : '<i class="fa fa-github fa-fw"></i>',
            'github pages (mirror)' : '<i class="fa fa-github-square fa-fw"></i>'
    }

    for key in botlinks.keys():
        descr += "<h3>charlesreid1 bots on %s:<h3>\n\n"%(key)
        fa_icon = fa_icons[key]

        links = botlinks[key]
        for bot_name in links.keys():
            bot_link = links[bot_name]
            descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(bot_link)
            descr += "%s %s"%(fa_icon, bot_name)
            descr += "</a></p>\n"
        
        descr += "\n"

    return descr

LINKS_TITLE = "bot links"

LINKS_DESCRIPTION = make_links_description()


# ---


CONTACT_TITLE = "Contact @charlesreid1"

CONTACT_DESCRIPTION = """<p>Get in touch!</p>
<p><a href="mailto:charles@charlesreid1.com">charles__at__charlesreid1.com</a></p>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
