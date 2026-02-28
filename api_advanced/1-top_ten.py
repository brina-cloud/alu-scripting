#!/usr/bin/python3
""" Module that queries the Reddit API and returns the top ten hot posts"""
import requests


def top_ten(subreddit):
    """ Queries the reddit api and returns the top ten hot posts """
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    header = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    info = r.json()['data']['children']
    for post in info:
        print(post['data']['title'])
