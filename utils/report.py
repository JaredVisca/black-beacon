import smtplib, os, datetime, sys
from email.mime.text import MIMEText

def black_beacon_report(urls):
    black_beacon_send_email(urls)
    black_beacon_write_logs(urls)

def black_beacon_send_email(urls):
    html = black_beacon_html_body_builder(urls)
    noreply = "noreply@joann.com"
    team_list = get_email_recipients_as_list()
    team_string = ','.join(team_list)
    email = MIMEText(html, 'html')
    email['Subject'] = black_beacon_subject_compiler(urls)
    email['To'] = team_string
    email['From'] = noreply
    email = email.as_string()
    smtp = smtplib.SMTP("mail.joann.com")
    smtp.sendmail(noreply, team_list, email)
    smtp.close()

def black_beacon_send_sms(urls):
    texts = 'texts.noreply@joann.com'
    team_list = get_text_recipients_as_list()
    for team_member in team_list:
        smtp = smtplib.SMTP("mail.joann.com")
        smtp.sendmail(texts, team_member, 'Black Beacon has identified a problem with a web service.')
        smtp.close()

def black_beacon_write_logs(urls):
    root_dir = sys.path[0]
    log_path = os.path.join(root_dir, 'logs/')
    if(os.path.exists(log_path)):
        time = datetime.datetime.now()
        string_time = time.strftime('%m-%d-%Y')
        filename = 'log-%s.txt' % string_time
        text = black_beacon_text_body_builder(urls)
        filepath = os.path.join(log_path, filename)
        if(os.path.isfile(filepath)):
            log = open(filepath, 'a')
            log.write(get_text_new_line())
            log.write(text)
            log.close()
        else:
            log = open(filepath, 'w+')
            log.write(text)
            log.close()

def black_beacon_html_body_builder(urls):
    html = ''
    for url in urls:
        html += black_beacon_build_title(url.get_title(), url.get_url_status())
        html += black_beacon_build_message(url.get_message())
        html += get_html_new_line()
    return html

def black_beacon_build_title(title, status):
    if(status == 'OK'):
        return "<div style=\"font-size: 18px; color: #fff; background-color: #35bc00; padding: 10px;\"> %s Status: %s </div>" % (title, status)
    elif(status == 'WARN'):
        return "<div style=\"font-size: 18px; color: #fff; background-color: #d8cd00; padding: 10px;\"> %s Status: %s </div>" % (title, status)
    elif(status == 'PROBLEM'):
        return "<div style=\"font-size: 18px; color: #fff; background-color: #b20202; padding: 10px;\"> %s Status: %s </div>" % (title, status)
		
def black_beacon_build_message(message):
    html = "<div style=\"background-color: #EFEFEF; padding: 20px;\">"
    html += message
    html += "</div>"
    return html

def black_beacon_text_body_builder(urls):
    text = 'Log for Black Beacon ran at %s' % get_current_time()
    for url in urls:
        text += get_text_new_line()
        text += '%s Status: %s' % (url.get_title(), url.get_url_status())
        text += get_text_new_line()
        text += url.get_message()
        text += get_text_new_line()
    return text

def black_beacon_subject_compiler(urls):
    code = 0
    text = ''
    for url in urls:
        if(url.get_url_status() == "PROBLEM"):
            return "PROBLEM: Black Beacon Report"
        elif(url.get_url_status() == "WARN"):
            code = 1
            text = "WARN: Black Beacon Report"
        elif(url.get_url_status() == "OK" and code != 1):
            text = "OK: Black Beacon Report"
    return text

def get_email_recipients_as_list():
    file_name = 'recipients.txt'
    root_dir = sys.path[0]
    input_path = os.path.join(root_dir, 'input/')
    file_path = os.path.join(input_path, file_name)
    if(os.path.exists(file_path)):
        if(os.path.isfile(file_path)):
            recipients_file = open(file_path, 'r')
            recipients = recipients_file.read()
            recipients_list = recipients.split()
            return recipients_list

def get_text_recipients_as_list():
    file_name = 'sms_recipients.txt'
    root_dir = sys.path[0]
    input_path = os.path.join(root_dir, 'input/')
    file_path = os.path.join(input_path, file_name)
    if(os.path.exists(file_path)):
        if(os.path.isfile(file_path)):
            recipients_file = open(file_path, 'r')
            recipients = recipients_file.read()
            recipients_list = recipients.split()
            return recipients_list

def get_current_time():
    time = datetime.datetime.now()
    string_time = time.strftime('%I:%M:%S%p')
    return string_time

def get_html_new_line():
    return '<br/>'

def get_text_new_line():
    return '\n'