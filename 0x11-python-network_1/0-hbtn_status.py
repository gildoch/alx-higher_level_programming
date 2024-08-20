#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    from urllib import request
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as resp:
        data = resp.read()
        print("Body response:")
        print('\t - type: {}'.format(type(data)))
        print('\t - content: {}'.format(data))
        print('\t - utf8 content: {}'.format(data.decode("utf-8")))
