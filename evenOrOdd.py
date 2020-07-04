#!/usr/bin/python3
import os

QUERY = os.getenv('QUERY_STRING')

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello World - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Hello World! This is my first CGI program</h2>')
print('<h3>{}</h3>'.format(QUERY))
print('</body>')
print('</html>')
