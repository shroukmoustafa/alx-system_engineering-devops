import requests

def number_of_subscribers(subreddit):
    """Query Reddit API and return the number of subscribers."""
    # Set the User-Agent header to avoid 'Too Many Requests' error
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    
    # Define the URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the status code is 200, we assume the subreddit is valid
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        
        # If the status code is not 200, return 0 (invalid subreddit)
        else:
            return 0
    except requests.RequestException:
        # If there was a network-related error, return 0
        return 0

