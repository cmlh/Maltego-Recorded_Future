#!/usr/bin/env python

from canari.maltego.entities import EntityField, Entity


class RecfutEntity(Entity):
    # namespace = 'recfut'
    # https://github.com/allfro/canari/issues/17
    _namespace_ = 'recfut'

@EntityField(name='properties.company', propname='propertiescompany', displayname='Company Entity')
@EntityField(name='eid', propname='eid', displayname='Entity ID')
@EntityField(name='properties.rftype', propname='propertiesrftype', displayname='Event Type')
class Company(RecfutEntity):
    pass


@EntityField(name='properties.companyname', propname='propertiescompanyname', displayname='Company Name to Lookup')
class CompanyName(RecfutEntity):
    pass


@EntityField(name='properties.organization', propname='propertiesorganization', displayname='Organisation Entity')
@EntityField(name='eid', propname='eid', displayname='Entity ID')
@EntityField(name='properties.rftype', propname='propertiesrftype', displayname='Event Type')
class Organization(RecfutEntity):
    pass


@EntityField(name='properties.position', propname='propertiesposition', displayname='Position Entity')
@EntityField(name='eid', propname='eid', displayname='Entity ID')
@EntityField(name='properties.rftype', propname='propertiesrftype', displayname='Event Type')
class Position(RecfutEntity):
    pass


@EntityField(name='properties.product', propname='propertiesproduct', displayname='Product Entity')
@EntityField(name='eid', propname='eid', displayname='Entity ID')
@EntityField(name='properties.rftype', propname='propertiesrftype', displayname='Event Type')
class Product(RecfutEntity):
    pass


@EntityField(name='properties.rfcsv', propname='propertiesrfcsv', displayname='Name Your Project')
@EntityField(name='source', propname='source', displayname=None)
class RFCSV(RecfutEntity):
    pass


@EntityField(name='rfevent', propname='rfevent', displayname='Recorded Future - Event Cluster ID')
@EntityField(name='eid', propname='eid', displayname='Entity ID')
@EntityField(name='etype', propname='etype', displayname='Event Type')
@EntityField(name='starttime', propname='starttime', displayname='Start Time')
@EntityField(name='stoptime', propname='stoptime', displayname='Stop Time')
@EntityField(name='fragment', propname='fragment', displayname='Fragment')
@EntityField(name='document_link', propname='documentlink', displayname='Document Link')
@EntityField(name='precision', propname='precision', displayname='Precision')
@EntityField(name='count', propname='count', displayname='Count')
@EntityField(name='firstpublished', propname='firstpublished', displayname='First Published')
@EntityField(name='lastpublished', propname='lastpublished', displayname='Last Published')
@EntityField(name='pos_sentiment', propname='possentiment', displayname='Positive Sentiment')
@EntityField(name='neg_sentiment', propname='negsentiment', displayname='Negative Sentiment')
class RFEvent(RecfutEntity):
    pass


@EntityField(name='properties.technology', propname='propertiestechnology', displayname='Technology Entity')
@EntityField(name='eid', propname='eid', displayname='Entity ID')
@EntityField(name='properties.rftype', propname='propertiesrftype', displayname='Entity Type')
class Technology(RecfutEntity):
    pass


