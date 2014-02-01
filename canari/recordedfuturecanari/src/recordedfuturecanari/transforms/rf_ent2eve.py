#!/usr/bin/env python

from datetime import date
from dateutil.relativedelta import relativedelta
from canari.maltego.utils import debug, progress
from canari.framework import configure  # , superuser
from common.entities import RFEvent, Company
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
    label='To Event [Recorded Future]',
    description='Returns a Recorded Future Company Event(s)',
    uuids=[ 'recfut.RFEntityExpand' ],
    inputs=[ ('Recorded Future', Company ) ],
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
    # Limit to the past 6 months.
    min_pub = date.today() + relativedelta(months=-6)

    cluster_query = {
    "cluster": {
        "document": {
            "published": {
                "min": str(min_pub)
                }
            },
            "attributes": [
            {
                "entity": { "id" : eid },
            }
            ],
                "limit": 100
        }
    }

    for eve in rfapi.query(cluster_query).get("events", []):
        e = RFEvent(eve['type'] + " [id: {0}]".format(eve['id']));
        e.eid = eve['id'];
        e.etype = eve['type'];
        e.starttime = eve['attributes'].get('start','');
        e.stoptime = eve['attributes'].get('stop','');
        e.fragment = eve['stats']['top_sources'][0]['fragment'].encode('utf-8');
        e.document_link = eve['stats']['top_sources'][0]['document_link'].encode('utf-8');
        # Add entity to response object
        response += e
    
    # Update progress
    progress(100)

     

    # Return response for visualization
    return response

def onterminate():
    debug('Caught signal... exiting.')
    exit(0)
