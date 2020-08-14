#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

def moewmoew():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    moewlist = []
    for catfact in r.json().get("all"):
        moewlist.append(catfact.get("text"))
    print("\n\n here is your Moewledge of the day:\n\n"+ random.choice(moewlist))
moewmoew()
