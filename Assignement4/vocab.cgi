#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

print "Content-type:text/html\r\n\r\n"

print """
<html>
<head>
<title>Hello - Second CGI Program</title>
</head>
"""
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print """

<body>
	<form action="sample-script.cgi" method="post">
First Name: <input type="text" name="first_name"><br />
Last Name: <input type="text" name="last_name" />

<input type="submit" value="Submit" />
</form>
"""
print 		"<h2>Hello %s %s</h2>" % (first_name, last_name)
print "</body>"
print "</html>"
