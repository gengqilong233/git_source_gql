import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_Text(host='smtp.qq.com', sender='965456595@qq.com', receiver='965456595@qq.com', password='bmgyvnvwcjhybdce',
              subject='Python send Text',msg='这是发送text邮件的内容'):
    host = host

    sender = sender
    receiver = receiver
    password = password

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header('耿<965456595@qq.com>', 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP(host, 25)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, [receiver], message.as_string())
        print('发送成功')
    except Exception as e:
        print(e)


send_Text()
