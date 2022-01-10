#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = {'q': sys.argv[1]}
        r = requests.post(url, data=q)
        if r.headers.get('content-type') != 'application/json':
            raise TypeError
        if r.json():
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
        else:
            print("No result")
    except IndexError:
        print("No result")
    except TypeError:
        print("Not a valid JSON")
