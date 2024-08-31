#!/usr/bin/python3
"""Module for top ten posts in a subreddit"""

import requests
from sys import argv


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Chrome/56.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title', ''))
