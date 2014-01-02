# -*- coding: utf-8 -*-

from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from twgov.content import MessageFactory as _


# Interface class; used to define content-type schema.

class IgovNotice(form.Schema, IImageScaleTraversable):
    """
    govNotice conttent type
    """
    form.model("models/govnotice.xml")

    govDepartment = schema.TextLine(
        title=_(u'governmetn departments'),
        required=False,
    )

    govBranch = schema.TextLine(
        title=_(u'governmetn branch unit'),
        required=False,
    )

    govAddress = schema.TextLine(
        title=_(u'governmetn branch unit address'),
        required=False,
    )

    contact = schema.TextLine(
        title=_(u'this notice contact'),
        required=False,
    )

    telNo = schema.TextLine(
        title=_(u'telephone number'),
        required=False,
    )

    faxNo = schema.TextLine(
        title=_(u'fax number'),
        required=False,
    )

    emailAddress = schema.TextLine(
        title=_(u'contact email address'),
        required=False,
    )

    noticeId = schema.TextLine(
        title=_(u'notice ID'),
        required=False,
    )

    noticeName = schema.TextLine(
        title=_(u'notice name'),
        required=False,
    )

    budget = schema.TextLine(
        title=_(u'notice budget'),
        required=False,
    )

    bidWay = schema.TextLine(
        title=_(u'bid way'),
        required=False,
    )

    decideWay = schema.TextLine(
        title=_(u'decide way'),
        required=False,
    )

    noticeTimes = schema.TextLine(
        title=_(u'number of notice times'),
        required=False,
    )

    noticeState = schema.TextLine(
        title=_(u'notice state'),
        required=False,
    )

    startDate = schema.Datetime(
        title=_(u'notice start date'),
        required=False,
    )

    endDate = schema.Datetime(
        title=_(u'notice end date'),
        required=False,
    )

    bidDate = schema.Datetime(
        title=_(u'notice bid date'),
        required=False,
    )

    bidAddress = schema.TextLine(
        title=_(u'notice bid address'),
        required=False,
    )

    bidDeposit = schema.TextLine(
        title=_(u'bid  deposit'),
        required=False,
    )

    documentSendTo = schema.TextLine(
        title=_(u'bid document send to'),
        required=False,
    )

    companyQualification = schema.Text(
        title=_(u'company qualification'),
        required=False,
    )

    companyAbility = schema.Text(
        title=_(u'company ability to basic qualifications'),
        required=False,
    )

    noticeUrl = schema.TextLine(
        title=_(u'notice url address'),
        required=False,
    )




class govNotice(Container):
    grok.implements(IgovNotice)

    # Add your class methods and properties here


class SampleView(grok.View):
    """ sample view class """

    grok.context(IgovNotice)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
