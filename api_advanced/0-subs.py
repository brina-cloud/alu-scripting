#!/usr/bin/python3
""" Module that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""

    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
    	return 0
    info = r.json()
    return (info.get("data", {}).get("subscribers", 0))


