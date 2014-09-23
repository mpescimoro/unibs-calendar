#!/usr/bin/env python

"""
Author : pescimoro.mattia@gmail.com
Licence : GPL v3 or any later version

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import urllib2
from HTMLParser import HTMLParser

# Create a subclass and override the handler methods
class DataParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_link = False
	self.position = 0
	
    def handle_starttag(self, tag, attrs):
        self.in_link = False
	if tag == 'td':
	    for attributes in attrs:
		# Extract lesson and room names
	    	if attributes[1] == 'subject_pos1' or attributes[1] == 'subject_pos3':
		    self.in_link = True
	elif tag == 'table':
	    for attributes in attrs:
	    	if attributes[0] == 'id':
                    self.in_link = True
		    # Table position (DAY x  HOUR)
		    s = attributes[1]
		    print s.upper()
		    
    def handle_endtag(self, tag):
        if tag == 'table':- 
            self.in_link = False

    def handle_data(self, data):
        if self.in_link and data.strip():
	    	if self.position == 0:
                    print data.upper()
		    self.position = 1
		else:
           	    print '{0}\n'.format(data.upper())
		    self.position = 0

# URL goes here
url = 'https://calendari.unibs.it/EasyCourse/Orario/Area_di_Scienze_Ingegneristiche/2014-2015/85/Curricula/Ingegneriainformatica_LaureatriennaleDM270_3_Curriculumgeneraleaa2012-13_05713.html'
fetch = urllib2.urlopen(url)
# Instantiate the parser and feed it with some HTML
parser = DataParser()
parser.feed(fetch.read())
parser.close()

# DISCLAIMER: this is random coding that relies on HTML formatting of a specific webpage. 
# Thus the only thing that keeps it working is the belief in lazy people.
# DO NOT use this as an example of good programming.
