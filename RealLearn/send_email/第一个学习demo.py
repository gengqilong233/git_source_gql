from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email.utils import parseaddr,formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = "965456595@qq.com"
password = "bmgyvnvwcjhybdce"
to_addr = "gengql@hfjy.com"

msg = MIMEText('hello,hahaha', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr) # Header('965456595@qq.com', 'utf-8')
msg['To'] = _format_addr('管理员 <%s>' % to_addr) # Header('gengql@hfjy.com', 'utf-8')
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
# msg['Subject'] = Header('这个东西到底是啥', 'utf-8')

# from_addr = "965456595@qq.com"
# password = "uxigpdmvntpmbbhe"
# to_addr = "gengql@hfjy.com"
smtp_server = 'smtp.qq.com'


server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
print('发送成功')
server.quit()

