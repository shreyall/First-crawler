from urllib.request import urlopen  # import module to connect to webpages directly
from link_finder import LinkFinder
from general import*

class Spider:
    # Class variables (shared among all instances)
    # Declaring blank variables so data can be passed on after
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''

    def __init__(self, project_name, base_url, domain_name):
        spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = spider.project_name + '/queue.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # boot function to create a folder and the text files in it
    @staticmethod
    def boot(self):
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in spider.crawled:
            print(thread_name + 'now crawling' + page_url)
            print('Queue' +str(len(Spider.queue)) + '| Crawled' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
    
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content Type')=='text/html':
                html_bytes=response.read()
                html_string=html_bytes.decode('utf-8')
            finder = LinkFinder(base_url, page_url)
            finder.feed(html_string)
            except:
                print("Error: can not crawl page")
                return set()
            return finder.page_links

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue: # continue means not do anything
                continue
            if url in Spider.crawled: # if url is in queued or crawled text, dont do anything
                continue
            if Spider.domain_name not in url:  # if domain name not in url, dont do anything 
                continue 
            spider.queue.add(url)

    @staticmethod
    def update_files():   ## convert the sets to files.. 
        set_to_file(Spider.queue , spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)