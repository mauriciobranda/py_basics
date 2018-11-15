import sys
import requests
import json
import urllib.parse

#number of pages in JSON feed

def print_page(page_num, num_passenger):
    endpoint = "https://swapi.co/api/starships/?"
    type = 'json'

    #specifies api parameters
    url = endpoint + urllib.parse.urlencode({"format": type, "page": page_num})

    #gets info
    json_data = requests.get(url).json()
    # number_of_ship = json_data['count']
    if 'results' in json_data:
      for ship in json_data['results']:
          if has_pilot(ship) and has_enough_passenger(ship, num_passenger):
              print_pilots_on(ship)

def get_pilot_name(pilot):
    type = 'json'

    #specifies api parameters
    url = pilot

    #gets info
    json_data = requests.get(url).json()
    return json_data["name"]

def print_pilots_on(ship):
    for pilot in ship['pilots']:
       print(get_pilot_name(pilot), ship['name'])

def has_pilot(ship):
    if ship['pilots']:
      return True
    return False

def has_enough_passenger(ship, num):
    if ship['passengers'] != "unknown" and int(ship['passengers']) >= num:
      return True
    return False

def print_pilots_and_ships(num_passenger):

    page_list = [1,2,3,4,5,6,7,8,9]
    # list to store names

    for page in page_list:
        print_page(page, num_passenger)


if __name__ == '__main__':
    num_passenger = int(20)
    print_pilots_and_ships(num_passenger)