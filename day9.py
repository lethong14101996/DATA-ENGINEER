import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables
username = 'thong.lequoc@thegioididong.com'
password = 'Lethong@1410!((^'

def send_mail(text='Email Body', subject='Hello World', from_email='Steven Lee <thong.lequoc@thegioidididong.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host='mail.thegioididong.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass
send_mail(to_emails=["5379@itmwg.vn","lethong14101996@gmail.com"],html="<h1h>SENDING SUCCESS MAIL</h1>")