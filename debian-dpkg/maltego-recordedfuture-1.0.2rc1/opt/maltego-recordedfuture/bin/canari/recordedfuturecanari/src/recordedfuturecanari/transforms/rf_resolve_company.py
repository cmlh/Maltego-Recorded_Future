#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Company, CompanyName
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
    label='To Company Entity [Recorded Future]',
    description='Returns a Recorded Future Company Entity',
    uuids=[ 'recfut.ResolveRFCompany' ],
    inputs=[ ( 'Recorded Future', CompanyName ) ],
    debug=False
)
def dotransform(request, response):

    # Report transform progress
    progress(50)
    # Send a debugging message to the Maltego UI console
    debug('Maltego Input Entity Value: %s' % request.value)
    
    name = request.value
    debug('name: %s' % name)
    
    rfapi = APIUtil()

    entity_query = {
                    "entity":{"name":name, "type":["Company", "Organization"], "limit":1}
                    }

    query_response = rfapi.query(entity_query)
    eid = None
    for q_eid, q_ent in query_response.get('entity_details', {}).items():
        debug("Found eid: {0}".format(q_eid))
        name = q_ent['name']
        eid = q_eid
        etype = q_ent['type']
        ent = q_ent

    if not eid:
        debug("Could not resolve any company/organization named '{0}'".format(name.encode('utf-8')))
        exit(1)

    # Create MyRecordedfutureEntity entity with value set to 'Hello <request.value>!'
    e = Company('%s' % request.value)
    e.eid = eid
    # Update progress
    progress(100)

    # Add entity to response object
    response += e

    # Return response for visualization
    return response

def onterminate():
    debug('Caught signal... exiting.')
    exit(0)
