#! /usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from BeautifulSoup import BeautifulSoup
from collections import deque
import argparse
import urlparse
import re

# bfs
TRAVERSE_MODE = 'bfs'
queue = deque()
# dfs
stack = []
# stats
crawled = []

# command line options
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("--url", type=str, help="the url to start with")
parser.add_argument("--key", type=str, help="the keyword to look for in web page")
parser.add_argument("--mode", type=str, help="(bfs or dfs) specify breadth-first or depth-first crawling")
parser.add_argument("--resume", type=str, help="specify the file to be used for resuming crawler")
args = parser.parse_args()

def get_all_links(content, page):
	# check if it's a valid url
	# full link to externals
    soup = BeautifulSoup(content)
    for i in soup.findAll('a', {'href': re.compile(r'^http://|https://')}):
    	next_url = urlparse.urljoin(page, i['href'])
    	if args.verbose:
    		print 'queuing %s' % (next_url)
    	if args.mode == 'bfs':
    		queue.append(next_url)
    	if args.mode == 'dfs':
			stack.append(next_url)
	# start with \ for internal links

def crawler(url, key):
	print 'crawling {0}'.format(url)
	# send request for web page
	response = requests.get(url)
	# check if web page has key
	if key in response.content:
		print 'found \'%s\' in %s'% (key, url)
	# queue up all links
	get_all_links(response.content, url)

def main():
	start_url = args.url
	key = args.key
	mode = args.mode
	# main loop draining the crawling queue
	if mode == 'bfs':
		queue.append(start_url)
		while len(queue) != 0:
			url = queue.popleft()
			crawler(url, key)

	if mode == 'dfs':
		stack.append(start_url)
		while len(stack) != 0:
			url = stack.pop()
			if url not in crawled:
				crawled.append(url)
				crawler(url, key)

if __name__ == '__main__':
	main()
	pass
