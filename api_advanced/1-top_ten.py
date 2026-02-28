#!/usr/bin/python3
""" Module that queries the Reddit API and returns the top ten hot posts"""
from wsgiref import headers

import requests


def top_ten(subreddit):
    """ Queries the reddit api and returns the top ten hot posts """
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    header = {"User-Agent": "python:subreddit.top.ten:v1.0"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    info = r.json().get("data", {}).get("children", [])
    for post in info:
        print(post.get("data", {}).get("title", ""))
