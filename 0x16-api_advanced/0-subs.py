#!/usr/bin/python3
# Python code

""" How many subs? """

import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns number subscribers """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
