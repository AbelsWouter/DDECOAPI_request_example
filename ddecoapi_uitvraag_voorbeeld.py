# Imports the datapraser script from the ddecoapidataparser.py file
from ddecoapidataparser import dataparser

# ***
# File: ddecoapi_uitvraag_voorbeeld.py
# Author: Wouter Abels (wouter.abels@rws.nl)
# Created: 28/03/22
# Last modified: 028/03/2022
# Python ver: 3.9.7
# ***

# Limited Documentation of the API is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api-specs
# Implementation of the API is found here: https://ddecoapi.aquadesk.nl/index.html
# Syntax for Filtering the API request is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api/blob/main/filtering.md

# Load data via the DD-ECO-API v2
# Configure API key (str) ***fill in the key of own organisation***
api_key = ''

# Configure API url and call the ddeciapidataparser script
ddecoapi = dataparser('https://ddecoapi.aquadesk.nl/v2/')

# Get filtered dataframe of requested data, in this example only MACEV data after 01-04-2021 is requested and the measurementobjectnames are excluded
# query_url (str): API endpoint for query
    #         query_filter (str, optional): Filtering within API. Defaults to None.
    #         skip_properties (str, optional): Properties to skip in response. Defaults to None.
    #         api_key (str, optional): API key for identification as company. Defaults to None.
data_query = ddecoapi.parse_data_dump(query_url = 'measurements', query_filter = 'measurementdate:ge:"2021-04-01";taxontype:eq:"MACEV"', skip_properties='measurementobjectname', api_key = api_key)

# Load TWN list data via the DD-ECO-API, in this example query the TWN list for all MACEV species is requested
twn_query = ddecoapi.parse_data_dump(query_url = 'parameters', query_filter = 'parametertype:eq:"TAXON";taxontype:eq:"MACEV"', api_key = api_key)
