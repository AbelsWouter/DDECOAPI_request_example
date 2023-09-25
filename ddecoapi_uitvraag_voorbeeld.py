"""Uses ddecoapiparser package to download AquaDesk data via the DD-ECO-API v2
First in your terminal write: "pip install ddecoapiparser" to download the ddecoapiparser package from PyPI
"""
import ddecoapiparser as dd
import dotenv
import os

"""
File: ddecoapi_uitvraag_voorbeeld.py
Author: Wouter Abels (wouter.abels@rws.nl)
Created: 28/03/22
Last modified: 18/09/23
Python ver: 3.11.4
"""

"""
The ddecoapiparser package is found here: https://pypi.org/project/ddecoapiparser/
Source code of the ddecoapiparser is found here: https://github.com/AbelsWouter/ddecoapiparser
Limited Documentation of the API is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api-specs
URL's of the API can be found here: https://ddecoapi.aquadesk.nl/index.html
Syntax for Filtering the API request is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api/blob/main/filtering.md
"""

"""
Configure API key
api_key = (str)
- Fill in the key of own organization to download measurement data from the AquaDesk.
"""
dotenv.load_dotenv()
api_key = os.getenv('API_KEY')

"""
EXAMPLE 1:
Get filtered dataframe of requested data, in this example only MACEV data after 01-04-2021 is requested and the measurementobjectnames are excluded.
"""
locations =  ["NRDZE_0001","NRDZE_0007"]
skip_properties = 'changedate,compartment,limitsymbol,collectiondate,measuredunit,measurementobject'
data_query = dd.parse_data_dump(query_url = 'measurements', query_filter = f"measurementdate:ge:'2015-01-01';measurementdate:le:'2020-12-31';taxontype:eq:'MACEV';measurementobject:in:{locations}", api_key = api_key, skip_properties=skip_properties)

"""
To view the data use a print statement or write the query to a CSV file.
"""
print(data_query)
data_query.to_csv('measurement_data.csv')

"""
EXAMPLE 2:
Load TWN-list data via the DD-ECO-API, in this example query the TWN-list for all MACEV species is requested. This works without specific API Key since query_url parameters is openly accessible.
"""
twn_query = dd.parse_data_dump(query_url = 'parameters', query_filter = 'parametertype:eq:"TAXON";taxontype:eq:"MACEV"', api_key = api_key)

"""
To view the data use a print statement or write the query to a CSV file.
"""
twn_query.to_csv('parameter_data.csv')
print(twn_query)