#!/usr/bin/python3
"""
task 1
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """method doc"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "subscribers" in data["data"]:
            return "OK"  # Subreddit exists
        else:
            return 0  # No subscribers data
    elif response.status_code == 404:
        return "OK"  # Subreddit does not exist
    else:
        return 0  # Other errors
