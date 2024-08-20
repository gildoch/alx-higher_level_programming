#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id"""

if __name__ == "__main__":
    import sys
    from urllib import request
    url = sys.argv[1]
    with request.urlopen(url) as resp:
        print(resp.headers.get('X-Request-Id'))
