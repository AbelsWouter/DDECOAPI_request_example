# DDECOAPI Request Example
This repository contains the code to request data via the DD-ECO-API using the ddecoapiparser package.

Extra Information:
 - The ddecoapiparser package is found here: https://pypi.org/project/ddecoapiparser/
 - Source code of the ddecoapiparser is found here: https://github.com/AbelsWouter/ddecoapiparser
 - Limited Documentation of the API is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api-specs
 - Implementation of the API is found here: https://ddecoapi.aquadesk.nl/index.html
 - Syntax for Filtering the API request is found here: https://github.com/DigitaleDeltaOrg/dd-eco-api/blob/main/filtering.md

Arguments of an API request query:
 - query_url (str): Select the desired url of the API to get the correct data.
 - query_filter (str, optional): Filtering within API. Defaults to None.
 - skip_properties (str, optional): Properties to skip in response. Defaults to None.
 - api_key (str, optional): API key for identification as company, required for some url's . Defaults to None.
