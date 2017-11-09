# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


from datetime import date,datetime

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

'''
from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')
'''

from_addr = '2567661786@qq.com'
password = 'zkwmydlugriyebgi'
#password = 'wztrdgyklemebie'
to_addr = '18811371255@163.com'
smtp_server = 'smtp.qq.com'

#　邮件内容
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

msg['From'] = _format_addr('文艺数学君 <%s>' % from_addr)
msg['To'] = _format_addr('尊敬的王先生 <%s>' % to_addr)
# 邮件标题
t = datetime.now()
header_title = datetime.strftime(t,'%Y-%m-%d')
msg['Subject'] = Header(header_title, 'utf-8').encode()

print(msg.as_string())

print('-----------')

try:
    server = smtplib.SMTP(smtp_server,587)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print('Success!')
except:
    print("Falied")