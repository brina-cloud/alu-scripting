#!/usr/bin/python3
""" Module that queries the Reddit API and returns the top ten hot posts"""
import requests


def top_ten(subreddit):
    """ Queries the reddit api and returns the top ten hot posts """
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    info = r.json().get("data", {}).get("children", [])
    for post in info[:10]:
        print(post.get("data", {}).get("title"))
