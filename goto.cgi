#!/usr/bin/env python

import cgi, cgitb ; cgitb.enable()
import os, sys
import re

DIR="./go_urls"

def main():
    PATH_INFO = os.environ.get('PATH_INFO', '')
    if not PATH_INFO:
        print("Status: 301 Found\nLocation: /\n\n")
        return
    pi = re.sub(r'[^a-z0-9-_:@+]', '', PATH_INFO.lower())
    fn = os.path.join(DIR, pi)
    if os.path.isfile(fn):
        url = open(fn).read().strip()
        print("Status: 301 Found\nLocation: %s\n\n" % url)
    else:
        print("Status: 404 Not Found\nContent-type: text/plain\n\n"
            + "Not found: <%s>" % fn) #PATH_INFO)

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print("Status: 500 Internal Server Error\nContent-type: text/plain\n\n")
        print(repr(e))
