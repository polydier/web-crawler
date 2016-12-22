# -*- coding: utf-8 -*-

import sqlite3

# Using http://www.debrice.com/building-a-simple-crawler/ as reference
# https://docs.python.org/2/library/sqlite3.html

class CrawlerData(object)

	def __init__(self, db_file)
		self.conn = sqlite3.connect(db_file)
		c = self.conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS url (url name, content text, last update date)''')
		self.conn.commit()
		self.cursor = self.conn.cursor()
	
	def insert(self, url, data, time):
        """
        save the content for a given url and its corresponding data
        """
        self.cursor.execute("INSERT INTO url VALUES (?,?,?)",
            (url, data, time))
        self.conn.commit()
		
	def fetch(self, url):
        """
        return the content for a given url
        """
        self.cursor.execute("SELECT content FROM url WHERE url=?",
            (url))
        row = self.cursor.fetchone()
        if row:
            return row[0]
	