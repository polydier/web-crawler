import sqlite3

#used Python 3.4
#creating Connection object that represents the database
conn = sqlite3.connect('example.db')

# create a cursor and call its execute method
c = conn.cursor()

#create table

c.execute('''CREATE TABLE IF NOT EXISTS url (urlname, urldata, code , date)''')

#insert a data row
c.execute("INSERT INTO url VALUES ('www.google.com', '<html><body>This is the google web page</body></html>', 'GOOG' ,  '2015-11-04')")

#save changes to the database
conn.commit()

#test if the data has been persisted in the database
#t = ('GOOG',)
#c.execute('SELECT * FROM url WHERE code = ?', t)
#print c.fetchone ()

c.execute('SELECT * FROM url')
rows = c.fetchall()

for row in rows:
	print (row)

#close the connection 
conn.close()

