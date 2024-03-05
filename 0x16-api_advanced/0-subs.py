#!/usr/bin/python3
# Python code

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Total number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyCustomUserAgent"}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

# Example usage:
subreddit_name = "learnprogramming"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers in r/{subreddit_name}: {subscribers_count}")
