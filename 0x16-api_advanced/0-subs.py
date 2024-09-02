#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    # Define the base URL for the Reddit API with the provided subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define a custom User-Agent to avoid issues with rate limiting
    headers = {'User-Agent': 'custom_agent_for_reddit_query'}

    try:
        # Send the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the status code indicates a successful request
        if response.status_code == 200:
            # Parse the JSON response and extract he subscriber count
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 if the subreddit is invalid 
            return 0
    except requests.RequestException:
        # In case of any other exceptions, return 0
        return 0
