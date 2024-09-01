#!/usr/bin/python3
"""
Module for querying the Reddit API to find the number of subscribers
for a given subreddit. If an invalid subreddit is provided, the function
returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        int: The number of subscribers to the subreddit, or 0 if
             the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                return data.get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0

