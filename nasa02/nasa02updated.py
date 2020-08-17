#!/usr/bin/env python3

import requests ## 3rd party URL lookup
import datetime

## define the main function
def main():
    # year = input("please enter the year that you would like to start search")
    # month = input (f"great! Please enter the month of {year} that you like to start search")
    # day = input(f"thank you! the last we need is the date in {month}, {year}")
    # date = f'{year}-{month}-{day}'
    # print(date)


    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2020-08-03'  ## start date for data
    enddate = '&end_date=2020-08-14' ## create a mechanism to utilize enddate
    mykey = '&api_key=XcZZaNTbWiVB9dfRLcesONOULtyTOG4gCahxwOG2' ## replace this with our API key

    neourl = neourl + startdate + mykey
    print(neourl)

    neojson = (requests.get(neourl)).json()
    neos = neojson.get("near_earth_objects")
    i = 0
    for key in neos.values():
        print(key)

# call main
main()
