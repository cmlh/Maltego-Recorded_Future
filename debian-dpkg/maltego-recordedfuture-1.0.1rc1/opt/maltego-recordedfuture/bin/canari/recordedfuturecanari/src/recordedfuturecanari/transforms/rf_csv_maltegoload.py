#!/usr/bin/env python

import Tkinter, tkFileDialog
import json
import csv
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import RFCSV, RFEvent
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
    label='Import CSV File [Recorded Future]',
    description='http://support.recordedfuture.com/knowledgebase/articles/164320-csv-export-explained',
    uuids=[ 'recfut.RFImportCSV' ],
    inputs=[ ( 'Recorded Future', RFCSV ) ],
    debug=False
)
def dotransform(request, response):

    # Report transform progress
    progress(50)
    # Send a debugging message to the Maltego UI console
    debug('Maltego Input Entity Value: %s' % request.value)
    
    name = request.value
    debug('name: %s' % name)
    
    root = Tkinter.Tk()
    root.lift()
    root.withdraw()
    
    # TODO Raise exception if no CSV file is selected
    csvfilename = tkFileDialog.askopenfilename()
    

    data = csv.DictReader(open(csvfilename), delimiter=',',fieldnames=('Event Id','Event Type','Event Title','Start Time','End Time','Precision','Count','First Published Time','Last Published Time','Sample Fragment','Entities','Locations','Source Count','Positive Sentiment','Negative Sentiment'))

    next(data)

    for row in data:
        
        event = row['Event Type']+"-"+row['Event Id']
        e = RFEvent('%s' % event)
        e.eid = row['Event Id']
        e.etype = row['Event Type']
        e.title = row['Event Title']
        e.starttime = row['Start Time']
        e.stoptime =  row['End Time']
        e.fragment = row['Sample Fragment']
        e.precision = row['Precision']
        e.count = row['Count']
        e.firstpublished = row['First Published Time']
        e.lastpublished = row['Last Published Time']
        e.sourcecount = row['Source Count']
        e.possentiment = row['Positive Sentiment']
        e.negsentiment = row['Negative Sentiment']
        # Add entity to response object
        response += e

    # Update progress
    progress(100)


    # Return response for visualization
    return response

def onterminate():
    debug('Caught signal... exiting.')
    exit(0)
