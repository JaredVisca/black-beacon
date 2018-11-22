import os, urllib2, mimetypes, json, datetime

def ping_url(object):
    try:
        start = datetime.datetime.now()
        res = urllib2.urlopen(Beacon.url)
        end = datetime.datetime.now()
        delta = (end - start)
        delta = int(((delta.microseconds + 0.0 + (delta.seconds + delta.days * 24 * 3600) * 10**6) / 10**6) * 1000)
        Beacon.response_time(delta)
        Beacon.http_status(res.getcode())
        Beacon.message('%s\'s url, %s, had a response time of %sms and returned a %s.' % (Beacon.title, Beacon.url, Beacon.response_time, Beacon.http_status)
    except urllib2.HTTPError, e:
        Beacon.http_status(e.code)
        Beacon.message('%s\'s url, %s, had a response time of %sms and returned a %s.' % (Beacon.title, Beacon.url, Beacon.response_time, Beacon.http_status)
    except urllib2.URLError, e:
        Beacon.set_message('%s\'s url, %s, had a response time of %sms and returned a %s.  This webservice also returned an error: %s' % (Beacon.title, Beacon.url, Beacon.response_time, Beacon.http_status, e.reason))
    return Beacon
