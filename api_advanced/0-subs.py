#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""
import requests


def number_of_subscribers(subreddit):
    """python3 -c 'print(__import__("my_module").__doc__)'"""

    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0"}
    r = response.get(url, headers=headers, allow-redirects="False")
    if response.status != 200:
    	return 0
    data = r.json()
    return (data.get("data", {}).get("subscribers", 0)

