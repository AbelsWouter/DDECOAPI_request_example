"""Uses ddecoapidataparser script to download AquaDesk data via the DD-ECO-API v2"""
from ddecoapidataparser import dataparser

"""
File: ddecoapi_uitvraag_voorbeeld.py
Author: Wouter Abels (wouter.abels@rws.nl)
Created: 28/03/22
Last modified: 19/09/2022
Python ver: 3.10.6
"""

"""
Limited Documentation of the API is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api-specs
URL's of the API can be found here: https://ddecoapi.aquadesk.nl/index.html
Syntax for Filtering the API request is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api/blob/main/filtering.md
"""

"""
Configure API key
api_key = (str)
- Fill in the key of own organization to download measurement data from the AquaDesk.
"""
api_key = ''

"""
Configure API version and call the dataparser class from the ddecoapidataparser script.
ddecoapi = class(str).
- Change this if DD-ECO-API version changes.
"""
ddecoapi = dataparser('https://ddecoapi.aquadesk.nl/v2/')


"""
EXAMPLE 1:
Get filtered dataframe of requested data, in this example only MACEV data after 01-04-2021 is requested and the measurementobjectnames are excluded.
"""
data_query = ddecoapi.parse_data_dump(query_url = 'measurements', query_filter = 'measurementdate:ge:"2021-04-01";taxontype:eq:"MACEV"', skip_properties='measurementobjectname', api_key = api_key)

"""
EXAMPLE 2:
Load TWN-list data via the DD-ECO-API, in this example query the TWN-list for all MACEV species is requested. This works without specific API Key since query_url parameters is openly accessible.
"""
twn_query = ddecoapi.parse_data_dump(query_url = 'parameters', query_filter = 'parametertype:eq:"TAXON";taxontype:eq:"MACEV"', api_key = api_key)
