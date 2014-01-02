# -*- coding: utf-8 -*-


#from zc.relation.interfaces import ICatalog
#from zope.component import getUtility
from bs4 import BeautifulSoup
from Products.Five.browser import BrowserView
#from Products.CMFCore.utils import getToolByName
import urllib2
#from chardet import detect
#import json
from ..config import GOV_NOTICE_URL
from ..config import PCC_DOMAIN
from ..config import TEST_STRING
from ..config import NOTICE_KEYWORDS
from plone import api
from random import randrange
from datetime import datetime
#import sys


class GetGovNotice(BrowserView):
    def __call__(self):
        #取得公告首頁
        getHtml = urllib2.urlopen(GOV_NOTICE_URL)
        hrefList = list()
        for line in getHtml:
            if 'href="/tps/tpam/main/tps/tpam/tpam_tender_detail.do' in line:
                href = line.split('href="')[1].split('">')[0]
                hrefList.append('%s%s' % (PCC_DOMAIN, href))

#        return '%s\t%s' % (len(hrefgetHref), str(getHref))

        #依連結取得各頁面
        portal = api.portal.get()
        catalog = api.portal.get_tool(name='portal_catalog')
        for link in hrefList:
            getNoticeHtml = urllib2.urlopen(link)
            doc = getNoticeHtml.read()
            soup = BeautifulSoup(doc.decode('utf-8'))

            findT11bTags = soup.findAll('th','T11b')
#            testre = str()
#            return len(findT11bTags)
            for T11b in findT11bTags:
                T11bString = T11b.string
                if T11bString == NOTICE_KEYWORDS[0]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    govDepartment = text
                elif T11bString == NOTICE_KEYWORDS[1]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    govBranch = text
                elif T11bString == NOTICE_KEYWORDS[2]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    govAddress = text
                elif T11bString == NOTICE_KEYWORDS[3]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    contact = text
                elif T11bString == NOTICE_KEYWORDS[4]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    telNo = text
                elif T11bString == NOTICE_KEYWORDS[5]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    faxNo = text
                elif T11bString == NOTICE_KEYWORDS[6]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    emailAddress = text
                elif T11bString == NOTICE_KEYWORDS[7]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    noticeId = text
                elif T11bString == NOTICE_KEYWORDS[8]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    noticeName = text
                elif T11bString == NOTICE_KEYWORDS[9]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    budget = text
                elif T11bString == NOTICE_KEYWORDS[10]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    bidWay = text
                elif T11bString == NOTICE_KEYWORDS[11]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    decideWay = text
                elif T11bString == NOTICE_KEYWORDS[12]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    noticeTimes = text
                elif T11bString == NOTICE_KEYWORDS[13]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    noticeState = text
                elif T11bString == NOTICE_KEYWORDS[14]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    startDate = text
                elif T11bString == NOTICE_KEYWORDS[15]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    endDate = text
                elif T11bString == NOTICE_KEYWORDS[16]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    bidDate = text
                elif T11bString == NOTICE_KEYWORDS[17]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    bidAddress = text
                elif T11bString == NOTICE_KEYWORDS[18]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    bidDeposit = text
                elif T11bString == NOTICE_KEYWORDS[19]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    documentSendTo = text
                elif T11bString == NOTICE_KEYWORDS[20]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    companyQualification = text
                elif T11bString == NOTICE_KEYWORDS[21]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    companyAbility = text

            contentId = '%s%s' % (str(datetime.now().strftime('%Y%m%d%H%M')), str(randrange(10000000,100000000)))
            api.content.create(container=portal['gov_notice'], type='twgov.content.govnotice', title=noticeName, id=contentId)
            brain = catalog(id=contentId)
            item = brain[0].getObject()
            item.govDepartment = govDepartment
            item.govBranch = govBranch
            item.govAddress = govAddress
            item.contact = contact
            item.telNo = telNo
            item.faxNo = faxNo
            item.emailAddress = emailAddress
            item.noticeId = noticeId
            item.noticeName = noticeName
            item.budget = budget
            item.bidWay =bidWay
            item.decideWay = decideWay
            item.noticeTimes = noticeTimes
            item.noticeState = noticeState
#            item.startDate =
#            item.endDate =
#            item.bidDate =
            item.bidAddress = bidAddress
            item.bidDeposit = bidDeposit
            item.documentSendTo = documentSendTo
            item.companyQualification = companyQualification
            item.companyAbility = companyAbility

#            return govDepartment

#日期是民國，要先轉成西元再處理
#            item.start_date = datetime(2013,12,31) #這個格式可以
#            item.end_date = datetime(2013,12,11,12,10,35)
        return '%s%s' % ('OK', len(hrefList)) 
