import os

def analyze_responses(urls):
    for url in urls:
        if (http_status_check(url.get_http_status())):
            if url.get_response_time() <= 12999:
                url.set_url_status("OK")
            elif url.get_response_time() >= 13000 and url.get_response_time() <= 19999:
                url.set_url_status("WARN")
            elif url.get_response_time() >= 20000:
                url.set_url_status("PROBLEM")
        else:
            url.set_url_status("PROBLEM")
    return urls

def http_status_check(http_status):
    if(http_status != 200):
        return False
    else:
        return True
