#!/usr/bin/python3
"""Module for number of subscribers"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome/56.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    return response.json().get('data', {}).get('subscribers', 0)
