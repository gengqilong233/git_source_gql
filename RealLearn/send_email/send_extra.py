import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header



def send_Extra(host='smtp.qq.com', sender='965456595@qq.com', receiver='gengql@hfjy.com', password='bmgyvnvwcjhybdce',
              subject='Python send HTML&extra',messag= """
                                                <p>Python send HTML&extra</p>
                                                <p><a href="http://www.baidu.com">这是一个链接</a></p>
                                                """, type='html', extra=r'e:\Desktop\线上问题.txt', extra_name='ce1.txt'):
    '''支持发送带任何格式附件的邮件'''

    host = host
    code =  'utf-8'

    sender = sender
    receiver = receiver
    password = password

    message = MIMEMultipart()

    message['From'] = Header(sender, code)
    message['To'] = Header('gengql@hfjy.com', code)
    message['Subject'] = Header(subject, code)

    msg = MIMEText(messag, type, code)
    # extra1 = MIMEText(open(extra).read(), 'base64', code)  # 注释部分代码只适合TXT文档，可用没注释的这两行(30,31)
    # extra1['Content-Type'] = 'application/octet-stream' # 设置什么格式
    # extra1['Content-Disposition'] = 'attachment; filename='+extra_name # 设置什么格式，filename为邮件内附件名  +"'"++"'"
    extra1 = MIMEApplication(open(extra, 'rb').read())
    extra1.add_header('Content-Disposition', 'attachment', filename=extra_name)


    message.attach(msg)
    message.attach(extra1)

    try:
        smtpObj = smtplib.SMTP(host, 25)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print('发送成功')
    except Exception as e:
        print(e)

# send_Extra(extra=r'e:\Desktop\测试加密.xlsx', extra_name='ceshi2.xlsx')
send_Extra()



