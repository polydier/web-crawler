#! /usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

# dfs
REPORT_MODE = 'bfs_status_report'
# I use a list to implement the function of a stack.
stack = []
crawled = 0

def buildURL(root_url, url):
	# check if it's a valid url
	# start with \ for internal links
	if url[0] == '/':
		# TODO filter out already crawled link
		next_url = root_url + url
		#print 'Pushing %s' % next_url
		stack.append(next_url)

	# TODO check and add external

def crawler(url, key):
	global crawled
	crawled += 1
	# get the response of the website
	response = requests.get(url)
	# output if the key is in content
	if key in response.content:
		print 'found \'%s\' in %s'% (key, url)

	soup = BeautifulSoup(response.content)
	for href in soup.findAll('a'):
		# check and put the url in stack
		buildURL(url, href.get('href'))

def main():
	start_url = sys.argv[1];
	key = sys.argv[2];
	
	#Push the starting URL into stack
	stack.append(start_url)
	# main loop draining the crawling stack
	while len(stack) != 0:
		print 'You have crawled %d page(s) and there are(is) %d page(s) to be crawled...'% (crawled, len(stack))
		url = stack.pop()
		print 'You are crawling %s'% url
		crawler(url, key)

if __name__ == '__main__':
	main()