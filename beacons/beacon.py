import os, json, sys
from utils import ping, report, analyze

class Beacon:
    def __init__(self, title=None, url=None, **kwargs):
        self.title = title
        self.url = url
        self.response_time = kwargs.get('response_time', 0)
        self.http_status = kwargs.get('http_status', 0)
        self.url_status = kwargs.get('url_status', '')
        self.message = kwargs.get('message', '')
        
    def 


def create_beacons(**kwargs):
    root_dir = sys.path[0]
    input_path = os.path.join(root_dir, 'input/')
    input_file = kwargs.get('input_file', 'urls.json')
    url_list = []
    file_path = os.path.join(input_path, input_file)
    if(os.path.exists(input_path)):
        if(os.path.isfile(file_path)):
            with open(file_path) as url_file:
                data = json.load(url_file)
                urls = data['urls']
            for url in urls:
                url_list.append(BlackBeacon(title=url['title'], url=url['url']))
    return url_list
