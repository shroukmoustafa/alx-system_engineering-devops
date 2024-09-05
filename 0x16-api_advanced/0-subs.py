#!/usr/bin/python3
"""Module for task 0"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit  
 (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """

    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'your_app_name'}

    # Construct the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the JSON response to get the number of subscribers
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException:
        # Handle invalid subreddit or other errors
        return 0
