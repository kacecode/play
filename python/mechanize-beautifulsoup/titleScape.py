import mechanize
import cookielib
#import time # if sleep is needed for testing
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

## Setup ##
mech = mechanize.Browser()

#setup cookies
#jar = cookilib.LWPCookieJar()
#mech.set_cookiejar(jar)

#set browser options
mech.set_handle_robots(False) # respects anti-scripting requests
mech.set_handle_gzip(True) # handle gzip responses
mech.set_handle_referer(True) # allow referer header
mech.set_handle_equiv(True) # handles inline http headers
mech.set_handle_refresh(True) # allow refresh redirect

#optional debugging
mech.set_debug_http(False)
mech.set_debug_redirects(False)
mech.set_debug_responses(False)

#spoof normal browser
#firefox
#mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#chrome
mech.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22'), ('Accept-Language', 'en-US,en;q=0.8')]


# Follows refresh 0 but not hangs on refresh > 0
#br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


## Work ##
url = 'http://www.purplestate.info'
response = mech.open(url)
html = response.read()
soup = BeautifulSoup(html)
main = soup.findAll('div', attrs={'id':'content'})
cols = soup.findAll('div', attrs={'class':'post'})
with open('example.html', 'w+') as f:
  for block in cols:
    print >> f, block