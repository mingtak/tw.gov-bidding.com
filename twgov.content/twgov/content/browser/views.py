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


class GetGovNotice(BrowserView):
    def __call__(self):
        #取得公告首頁
        getHtml = urllib2.urlopen(GOV_NOTICE_URL)
        hrefList = list()
        for line in getHtml:
            if 'href="/tps/tpam/main/tps/tpam/tpam_tender_detail.do' in line:
                href = line.split('href="')[1].split('">')[0]
                hrefList.append('%s%s' % (PCC_DOMAIN, href))

        #依連結取得各頁面
        portal = api.portal.get()
        catalog = api.portal.get_tool(name='portal_catalog')
        for link in hrefList:
            getNoticeHtml = urllib2.urlopen(link)
            doc = getNoticeHtml.read()
            soup = BeautifulSoup(doc.decode('utf-8'))

            findT11bTags = soup.findAll('th','T11b')
            #get value
            for T11b in findT11bTags:
                T11bString = T11b.string.strip()
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
                    splitText = text.split('/')
                    startDate = (int(splitText[0])+1911,
                                 int(splitText[1]),
                                 int(splitText[2]),)
                elif T11bString == NOTICE_KEYWORDS[15]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    splitText = text.split()
                    splitTextToDate = splitText[0].split('/')
                    splitTextToTime = splitText[1].split(':')
                    endDate = (int(splitTextToDate[0])+1911,
                               int(splitTextToDate[1]),
                               int(splitTextToDate[2]),
                               int(splitTextToTime[0]),
                               int(splitTextToTime[1]),)
                elif T11bString == NOTICE_KEYWORDS[16]:
                    [text for text in T11b.find_next_siblings("td")[0].stripped_strings]
                    splitText = text.split()
                    splitTextToDate = splitText[0].split('/')
                    splitTextToTime = splitText[1].split(':')
                    bidDate = (int(splitTextToDate[0])+1911,
                               int(splitTextToDate[1]),
                               int(splitTextToDate[2]),
                               int(splitTextToTime[0]),
                               int(splitTextToTime[1]),)
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

            #assign value
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
            item.startDate = datetime(startDate[0], startDate[1], startDate[2])
            item.endDate = datetime(endDate[0], endDate[1], endDate[2], endDate[3], endDate[4])
            item.bidDate = datetime(bidDate[0], bidDate[1], bidDate[2], bidDate[3], bidDate[4])
            item.bidAddress = bidAddress
            item.bidDeposit = bidDeposit
            item.documentSendTo = documentSendTo
            item.companyQualification = companyQualification
            item.companyAbility = companyAbility
            item.exclude_from_nav = True
            item.reindexObject(idxs=['exclude_from_nav'])
            item.noticeUrl = link
            # 先處理一筆
            return '%s%s' % ('ok', str([startDate, endDate, bidDate]))

        return '%s%s' % ('OK', len(hrefList)) 
