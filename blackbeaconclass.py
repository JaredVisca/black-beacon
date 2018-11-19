import os, json, sys

class BlackBeacon(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.response_time = 0
        self.http_status = 0
        self.url_status = ""
        self.message = ""

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

    def get_response_time(self):
        return self.response_time

    def get_http_status(self):
        return self.http_status

    def get_url_status(self):
        return self.url_status

    def get_message(self):
        return self.message

    def get_all(self):
        return (self.title, self.url, self.response_time, self.http_status, self.url_status, self.message)

    def set_response_time(self, response_time):
        self.response_time = response_time

    def set_http_status(self, http_status):
        self.http_status = http_status

    def set_url_status(self, url_status):
        self.url_status = url_status

    def set_message(self, message):
        self.message = message

def create_beacons():
    root_dir = sys.path[0]
    input_path = os.path.join(root_dir, 'input/')
    input_file = 'urls.json'
    url_list = []
    file_path = os.path.join(input_path, input_file)
    if(os.path.exists(input_path)):
        if(os.path.isfile(file_path)):
            with open(file_path) as url_file:
                data = json.load(url_file)
                urls = data['urls']
            for url in urls:
                url_list.append(BlackBeacon(url['title'], url['url']))
    return url_list
