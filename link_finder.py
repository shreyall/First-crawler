# Generic HTML parser to sift through website code ie read the website (HTML) code
from html.parser import HTMLParser 
from urllib import parse 

# Make a class with HTMLParser functions along with other custom functions 
class LinkFinder(HTMLParser):
    
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        #if its an anchor tag 'a' loops through attributes to check if href
        #if href, parse it, join the base url to it and store it to the set selflinks
        if tag=='a':
            for (attribute, value) in attrs:
                if attribute=='href':
                    url=parse.urljoin(self.base_url, value)
                    self.links.add(url)

# REturns the set with the links
    def page_links(self):
        return self.links

    # Catch any errors and deliver the message
    def error(self, message):
        pass

##  finder = LinkFinder()
##  finder.feed('<html><head><title>Test</title></head>'
 #           '<body><h1>Parse me</h1></body></html>')