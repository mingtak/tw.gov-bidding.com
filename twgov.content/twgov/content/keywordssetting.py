from five import grok
from Acquisition import aq_inner
#from BTrees.OOBTree import OOSet
from zope.annotation.interfaces import IAnnotatable, IAnnotations
from plone import api


def writeIn(string):
    with open('/home/plone/yyyyy', 'a') as yyyyy:
        yyyyy.write(string + '\n')

class KeywordsSetting(grok.View):
    """Keywords Setting View
    """

    grok.context(IAnnotatable)
    grok.require('zope2.View')
    grok.name('keywords_setting')

    def update(self):
        userId = str(self.request['AUTHENTICATED_USER'])
        userItem = api.user.get(userid=userId)
#        '''
        userItem.emailaddress = self.request['replyto']
        userItem.keyword1 = self.request['keyword1']
        userItem.keyword2 = self.request['keyword2']
        userItem.keyword3 = self.request['keyword3']
        userItem.keyword4 = self.request['keyword4']
        userItem.keyword5 = self.request['keyword5'] #'''
#        keywords = '%s %s %s %s %s %s \n' % (userItem.emailaddress, userItem.keyword1, userItem.keyword2, userItem.keyword3, userItem.keyword4, userItem.keyword5)
        return #writeIn(str(self.request))
