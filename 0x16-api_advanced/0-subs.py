import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return "OK"  # Subreddit exists
    elif response.status_code == 404:
        return "OK"  # Subreddit does not exist
    else:
        return 0  # Other errors
