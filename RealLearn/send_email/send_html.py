import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_html(host='smtp.qq.com', sender='965456595@qq.com', receiver='965456595@qq.com', password='bmgyvnvwcjhybdce',
              subject='Python send HTML',msg= """
                                                <p>Python send HTML</p>
                                                <p><a href="http://www.baidu.com">这是一个链接</a></p>
                                                """):
    host = host

    sender = sender
    receiver = receiver
    password = password

    message = MIMEText(msg, 'html', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP(host, 25)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, [receiver], message.as_string())
        print('发送成功')
    except Exception as e:
        print(e)

send_html()

