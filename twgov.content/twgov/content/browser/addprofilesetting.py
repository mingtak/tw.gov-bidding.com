# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from Products.Five.browser import BrowserView
import urllib2
from ..config import GOV_NOTICE_URL
from ..config import PCC_DOMAIN
from ..config import TEST_STRING
from ..config import NOTICE_KEYWORDS
from plone import api
from random import randrange
from datetime import datetime


def writein(string):
    with open('/home/plone/yyyyy', 'a') as yyyyy:
        yyyyy.write('%s%s' % (str(string), '\n'))

class AddProfileSetting(BrowserView):
    def __call__(self):
        writein(self.request)
         
#        portal = api.portal.get()
#        api.content.create(container=portal['system'], type='twgov.content.profilesetting', title='noticeName',)     
