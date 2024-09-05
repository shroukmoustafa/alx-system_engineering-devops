#!/usr/bin/python3
"""Module to query the Reddit API for number of subscribers in a subreddit"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit. Returns 0 if the subreddit is invalid or if
    any other error occurs."""
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:subscribers_count:v1.0 (by /u/your_username)"}

    try:
        # Make the request and do not follow redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the status code is not 200 (success), return 0
        if response.status_code != 200:
            return 0
        
        # Extract the number of subscribers from the response JSON
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    
    except requests.RequestException:
        # Return 0 in case of any request exception (network issues, etc.)
        return 0

