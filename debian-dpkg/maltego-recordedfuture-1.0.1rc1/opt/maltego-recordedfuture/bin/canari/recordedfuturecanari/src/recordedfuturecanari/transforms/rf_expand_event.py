#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure  # , superuser
from canari.maltego.entities import *
from common.entities import RFEvent
from common.APIUtil import APIUtil

__author__ = 'Filip Reesalu'
__copyright__ = 'Copyright 2014, Recorded Future'
__credits__ = []

__license__ = 'Apache'
__version__ = '1.0'
__maintainer__ = 'Christian Heinrich'
__email__ = 'christian.heinrich@cmlh.id.au'
__status__ = 'Production'

__all__ = [
    'dotransform',
    'onterminate'
]

@configure(
    label='To Maltego Entity [Recorded Future]',
    description='Returns Maltego Entities [Recorded Future]',
    uuids=[ 'recfut.RFEventExpand' ],
    inputs=[ ('Recorded Future', RFEvent ) ],
    debug=False
)
def dotransform(request, response):

    # Report transform progress
    progress(50)
    # Send a debugging message to the Maltego UI console
    debug('Maltego Input Entity Value: %s' % request.value)
    
    eid = request.fields['eid']
    debug('Maltego Input Entity eid Field: %s' % eid)

    rfapi = APIUtil()

    reference_query = {
        "reference": {
            "cluster_id":eid,
            "limit": 100
        }
    }
    
    ents = []
    seen_ids = set()
    seen_ids.add(eid)
    for ceid, ent in rfapi.query(reference_query).get("entities", {}).items():
        if ceid not in seen_ids:
            ent["id"] = ceid
            ents.append(ent)
            seen_ids.add(ceid)
    
    e = request.value

    types = {'maltego.Person':'Person',
        'recfut.Company':['Company', 'OrgEntity'],
        'recfut.Organization':'Organization',
        'recfut.Product':'Product',
        'recfut.Technology':'Technology',
        'recfut.Position':'Position',
        'maltego.IPv4Address':'IpAddress',
        'maltego.Domain':"URL",
        'maltego.Location':['Continent', 'Country', 'City', 'ProvinceOrState', 'Region', 'NaturalFeature', 'GeoEntity'],
        'maltego.File':'WinExeFile',
        'maltego.Twit':'Username'
    }

    for ent in ents:
        c_type = "maltego.Phrase"
        for k, v in types.items():
            if type(v) == type([]) and ent['type'] in v:
                c_type = k
            elif v == ent['type']:
                c_type = k

        debug('c_type: %s' % c_type)
        
        if c_type == 'maltego.Person' :
            e = Person('%s' % ent['name'].encode('utf-8'))
            debug('ent[\'name\']: %s' % ent['name'].encode('utf-8'))
            # Add entity to response object        
            response += e
        
        if c_type == 'maltego.Phrase' :
            e = Phrase('%s' % ent['name'].encode('utf-8'))
            debug('ent[\'name\']: %s' % ent['name'].encode('utf-8'))
            # Add entity to response object        
            response += e

        # TODO Unit Test for Recorded Future API IPv4Address    
        if c_type == 'maltego.IPv4Address' :
            e = IPv4Address('%s' % ent['name'].encode('utf-8'))
            debug('ent[\'name\']: %s' % ent['name'].encode('utf-8'))
            # Add entity to response object        
            response += e
        
        # TODO Unit Test for Recorded Future API Domain    
        if c_type == 'maltego.Domain' :
            e = Domain('%s' % ent['name'].encode('utf-8'))
            debug('ent[\'name\']: %s' % ent['name'].encode('utf-8'))
            # Add entity to response object        
            response += e
        
        # TODO Unit Test for Recorded Future API Location  
        if c_type == 'maltego.Location' :
            e = Location('%s' % ent['name'].encode('utf-8'))
            debug('ent[\'name\']: %s' % ent['name'].encode('utf-8'))
            # Add entity to response object        
            response += e    

        # TODO Unit Test for Recorded Future API File
        if c_type == 'maltego.File' :
            e = File('%s' % ent['name'].encode('utf-8'))
            debug('ent[\'name\']: %s' % ent['name'].encode('utf-8'))
            # Add entity to response object        
            response += e  
        
        # TODO Unit Test for Recorded Future API Twit
        if c_type == 'maltego.Twit' :
            e = Twit('%s' % ent['name'].encode('utf-8'))
            debug('ent[\'name\']: %s' % ent['name'].encode('utf-8'))
            # Add entity to response object        
            response += e  
                              
    # Update progress
    progress(100)

    # Return response for visualization
    return response

def onterminate():
    debug('Caught signal... exiting.')
    exit(0)
