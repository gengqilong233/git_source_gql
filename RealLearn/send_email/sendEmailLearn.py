import smtplib # 发送邮件用到
from email.mime.text import MIMEText # 邮件正文用到
from email.mime.multipart import  MIMEMultipart # 往邮件内加信息用到
from email.mime.image import MIMEImage # 设置图片用到
from email.header import Header # 设置发送人、接收人、邮件标题用到



# 1、发送text内容邮件
mail_host = 'smtp.qq.com'

sender = '965456595@qq.com' # 发送人
password = 'bmgyvnvwcjhybdce' # 发送人邮箱授权码
receiver = '965456595@qq.com'# 收件人，因为可能是多个，所以是list
copy_receiver = '1016606805@qq.com,gengql@hfjy.com'
all_receivcer = [receiver] + [copy_receiver]

message = MIMEText('Python耿起龙', 'plain', 'utf-8') # 内容
# MIMEText函数的三个参数：1、内容 2、plain为文本的格式 3、是设置编码

message['From'] = Header('菜鸟耿起龙<gengql@hfjy.com>', 'utf-8') # 设置发件人
message['To'] = Header(receiver, 'utf-8') # 设置收件人
message['Cc'] = Header(copy_receiver, 'utf-8') # 设置抄送人
message['subject'] = Header('Python SMTP 邮件测试', 'utf-8') # 设置邮件标题
# ！！！ 内容、发件人、收件人、邮件标题为邮件的四大要素，缺失的话【邮件可能会被认为是辣鸡邮件】

try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    smtpObj.login(sender, password) # 登录SMTP服务器
    smtpObj.sendmail(sender, all_receivcer, message.as_string())
    print('测试通过')
except Exception as e:
    print(e)

# ----------------------------------------------------------------------------------------------------------------------

# 2、发送HTML内容邮件
# mail_host = 'smtp.qq.com'
# mail_password = 'bmgyvnvwcjhybdce'
#
# sender = '965456595@qq.com'
# reciver = ['gengql@hfjy.com']
#
# 字符串化html页面
# html_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">这是一个链接</a></p>
# """
#
# message = MIMEText(html_msg, 'html', 'utf-8') # 只需把MIMEText中的内容，格式替换成相应的HTML即可
# message['subject'] = Header('Python SMTP html内容邮件', 'utf-8')
# message['From'] = Header('耿起龙发送人', 'utf-8')
# message['To'] = Header('耿起龙接收人', 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP(mail_host, 25)
#     smtpObj.login(sender, mail_password)
#     smtpObj.sendmail(sender, reciver, message.as_string())
# except Exception as e:
#     print(e)

# ----------------------------------------------------------------------------------------------------------------------

# # 2、发送带附件的邮件
# mail_host = 'smtp.qq.com'
# mail_password = 'bmgyvnvwcjhybdce'
#
# sender = '965456595@qq.com'
# reciver = ['gengql@hfjy.com']
#
# message = MIMEMultipart() # 实例化函数
# message['From'] = Header('发送人', 'utf-8')
# message['To'] = Header('gengql@hfjy.com', 'utf-8')
# message['Subject'] = Header('带附件的邮件标题', 'utf-8')
#
# msg = MIMEText('这是内容', 'plain', 'utf-8') # 邮件正文内容
#
# att1 = MIMEText(open(r'e:\Desktop\草稿.txt').read(), 'base64', 'utf-8') # 存入附件
# att1['Content-Type'] = 'application/octet-stream' # 设置什么格式
# att1['Content-Disposition'] = 'attachment; filename="wodefujian.txt"' # 设置什么格式，filename为邮件内附件名
#
# message.attach(msg) # 将邮件正文内容加进发送信息
# message.attach(att1) # 将附件加入附加信息
#
# try:
#     smtpObj = smtplib.SMTP(mail_host, 25)
#     smtpObj.login(sender, mail_password)
#     smtpObj.sendmail(sender, reciver, message.as_string())
#     print('发送成功')
# except Exception as e:
#     print(e)

# ----------------------------------------------------------------------------------------------------------------------

# 2、发送带附件的邮件
# mail_host = 'smtp.qq.com'
# mail_password = 'bmgyvnvwcjhybdce'
#
# sender = '965456595@qq.com'
# reciver = ['gengql@hfjy.com']
#
# message = MIMEMultipart('related') # 实例化函数
# msgAlternative = MIMEMultipart('alternative') # 实例化函数
# message.attach(msgAlternative) # 将实例后的msgAlternative(二选一)附加到message上
#
# message['From'] = Header(sender, 'utf-8')
# message['To'] = Header('gengql@hfjy.com', 'utf-8')
# message['Subject'] = Header('带图片的邮件 标题', 'utf-8')
#
# msgAlternative = MIMEMultipart('alternative')
# message.attach(msgAlternative)
#
# # 字符串化html页面
# mail_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
# <p>图片演示：</p>
# <p><img src="cid:image1"></p>
# """
# msg = MIMEText(mail_msg, 'html', 'utf-8')
# msgAlternative.attach(msg)
#
# fp = open(r'e:\Desktop\TIM图片20180319181029.png', 'rb')
# msg_image = MIMEImage(fp.read())
# fp.close()
#
# msg_image.add_header('Content-ID', '<image1>')
# message.attach(msg_image)
#
# try:
#     smtpObj = smtplib.SMTP(mail_host, 25)
#     smtpObj.login(sender, mail_password)
#     smtpObj.sendmail(sender, reciver, message.as_string())
#     print('发送成功')
# except Exception as e:
#     print(e)

