#! /usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup
from collections import deque

# bfs real-time status report
REPORT_MODE = 'bfs_status_report'
queue = deque()
crawled = 0

def buildURL(root_url, url):
	# check if it's a valid url
	# start with \ for internal links
	if url[0] == '/':
		# TODO filter out already crawled link
		next_url = root_url + url
		#print 'queuing {0}'.format(next_url)
		queue.append(next_url)
	# TODO check and add external

def crawler(url, key):
	global crawled
	crawled += 1

	# send request for web page
	response = requests.get(url)
	# check if web page has key
	if key in response.content:
		print 'found \'{0}\' in {1}'.format(key, url)
	# queue up all links
	soup = BeautifulSoup(response.content)
	for href in soup.findAll('a'):
		# check and queue url
		buildURL(url, href.get('href'))

def main():
	start_url = sys.argv[1]
	key = sys.argv[2]
	#Enqueue the starting URL
	queue.append(start_url)
	# main loop draining the crawling queue
	while len(queue) != 0:
		print 'You have crawled %d page(s) and there are(is) %d page(s) to be crawled...'% (crawled, len(queue))
		url = queue.popleft()
		print 'You are crawling %s'% url
		crawler(url, key)

if __name__ == '__main__':
	main()