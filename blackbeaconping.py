import os, urllib2, mimetypes, json, datetime, ssl

def black_beacon_ping_url(urls):
    for url in urls:
        try:
            start = datetime.datetime.now()
            res = urllib2.urlopen(url.get_url(), timeout=17)
            end = datetime.datetime.now()
            delta = (end - start)
            delta = int(((delta.microseconds + 0.0 + (delta.seconds + delta.days * 24 * 3600) * 10**6) / 10**6) * 1000)
            url.set_response_time(delta)
            url.set_http_status(res.getcode())
            url.set_message('%s\'s url, %s, had a response time of %sms and returned a %s.' % (url.get_title(), url.get_url(), url.get_response_time(), url.get_http_status()))
        except urllib2.HTTPError, e:
            url.set_http_status(e.code)
            url.set_message('%s\'s url, %s, had a response time of %sms and returned a %s.' % (url.get_title(), url.get_url(), url.get_response_time(), url.get_http_status()))
        except ssl.SSLError, e:
            url.set_message('%s\'s url, %s, timed out (timeout is set to 17 seconds).' % (url.get_title(), url.get_url()))
        except urllib2.URLError, e:
            url.set_message('%s\'s url, %s, had a response time of %sms and returned a %s.  This webservice also returned an error: %s' % (url.get_title(), url.get_url(), url.get_response_time(), url.get_http_status(), e.reason))
    return urls
