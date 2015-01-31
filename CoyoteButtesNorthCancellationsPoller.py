# Script that polls the permit-cancellation page for Coyote Buttes North.
# If a cancellation is found, an email will be sent to the designated address
# This script uses data structures that are more complicated than it really needs to be because I want to get used to Python lists :)

from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib.request
import re
from datetime import datetime
from datetime import date
from smtplib import SMTP

# define CoyoteButtesHTMLParser

class CoyoteButtesHTMLParser(HTMLParser):

    # Class property that stores the full permit availability chart in list form
    availabilitySummary = []

    # Getter that formats and availability summary into a string for return
    def getAvailabilitySummary(self):
        stringBlockSummary = ""
        for availabilities in self.availabilitySummary:
            stringBlockSummary = stringBlockSummary + availabilities
        return stringBlockSummary
    
    # Event handler that is called when an HTML start tag is encountered by the HTML parser
    # Tag is the type of HTML start tag (e.g. "a" for link, "td" for table cell, etc)
    def handle_starttag(self, tag, attrs):
        
        # Variables needed when parsing the start tag
        isAvailable = False
        permitsAvailable = 0
        dateAvailable = date(1900, 1, 1)
        
        # We only perform actions when a link tag is encountered
        if (tag == 'a'):
            for attr in attrs:
                # There are two identical links per table cell that we can encounter. We only want to process one of them.
                # The difference between them is the STYLE (one is the calendar date, and the other is the number that displays
                # the number of availabilities
                if ('style' in attr
                and attr.index('style')+1 < len(attr)
                and attr[attr.index('style')+1].lower().find('black') >= 0):
                    # We've found an opening
                    isAvailable = True
                elif ('title' in attr
                and attr.index('title')+1 < len(attr)
                and attr[attr.index('title')+1].lower().find('entries available') > 0):
                    # Extract number of available permits from the link title
                    titleString = attr[attr.index('title')+1]
                    m = re.search(r'\d+', titleString)
                    permitsAvailable = int(m.group())
                    
                    # Extract date from the link title. The date format is "January 20, 2015"
                    m = re.search(r'[a-zA-Z]+ \d+, \d+', titleString) 
                    dateAvailable = datetime.strptime(m.group(), '%B %d, %Y').date()
        
        # This is hit if there's a link on the page that isn't related to (or formatted to) what we're searching for
        if  not isAvailable:
            return
        
        # Just to make sure the availability date is in the future
        if ( (isAvailable) and (dateAvailable > date.today()) ):
            self.availabilitySummary.append('There are {0} permits available for {1}.\n'.format(permitsAvailable, dateAvailable))
            
# Load in Coyote Buttes North Page
parser = CoyoteButtesHTMLParser()

# Parse, check for available dates
rawResponse = urllib.request.urlopen(
'https://www.blm.gov/az/paria/hikingcalendar.cfm?areaid=2')
decodedPage = rawResponse.read().decode('utf-8')

parser.feed(decodedPage)

AvailabilityResult = parser.getAvailabilitySummary()

# Send email to relevant parties if something matches

TO = 'mira.web@gmail.com'
SUBJECT = 'Coyote Butts is Available. Heh. Heh. Heh.'
TEXT = parser.getAvailabilitySummary()

# Sign In with a test/shell account
sender = 'PoPau@comcast.net'
passwd = 'HelloWorld123'

# Use Comcast SMTP server
server = SMTP('smtp.comcast.net', 587)
server.ehlo()
server.starttls()
server.login(sender, passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % sender,
                    'Subject: %s' % SUBJECT,
                    '', AvailabilityResult])

# Only send mail if we have something to send. The If block could block out entire email block if performance matters.
if AvailabilityResult:                    
    try:
        server.sendmail(sender, [TO], BODY)
        print ('Availabilities found. Email sent')
    except:
        print ('error sending mail')
else:
    print("No availabilities found. No email sent.")
    
server.quit()