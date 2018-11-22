import os, json, sys, ping, report, analyze, beacon

def report_builder(urls):
    blackbeaconreport.black_beacon_report(urls)

def log_builder(urls):
    blackbeaconreport.black_beacon_write_logs(urls)

def problem_indicator(urls):
    for url in urls:
        if(url.get_url_status() == "PROBLEM"):
            return True
    return False

if __name__ == "__main__":
    job_schedule_arg = sys.argv[1:]
    job_schedule = ''.join(job_schedule_arg)
    urls = blackbeaconclass.create_beacons()
    urls = blackbeaconping.black_beacon_ping_url(urls)
    urls = blackbeaconanalyze.analyze_responses(urls)
    if(problem_indicator(urls)):
        report_builder(urls)
        blackbeaconreport.black_beacon_send_sms(urls)
    else:
        log_builder(urls)
