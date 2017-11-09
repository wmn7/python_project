from __future__ import absolute_import, unicode_literals
from envelopes import Envelope, SMTP

# 这一组常量, 可以单独用 enum 管理
FROM_ADDR = "2567661786@qq.com"
FROM_ADDR_PASSWORD = "zkwmydlugriyebgi"
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = "465"

class MailUtils(object):
    @classmethod
    def send_mail(cls, mail_body, subject, from_addr, to_addrs, cc_addrs, attachments, headers=None):  #这里的参数组织顺序, 看个人喜好
        """发送邮件

        :param mail_body: 邮件mail body(默认html格式)
        :param subject: 主题
        :param from_addr: 发件人( 最好的格式: ("xxx@xx.com", "nick name")  )
        :param to_addrs: 收件人列表
        :param cc_addrs: 抄送人列表
        :param attachments: 附件列表, 基本是文件路径名
        :param headers: 额外的邮件头
        :return:
        """
        
        envelope = Envelope(
            from_addr=from_addr,
            to_addr=to_addrs,
            subject=subject,
            html_body=mail_body,
            cc_addr=cc_addrs or None
        )

        if headers is not None:
            for header_key, header_value in headers:
                envelope.add_header(header_key, header_value)

        for attachment in attachments:
            envelope.add_attachment(attachment)

        server = SMTP(
            host=SMTP_SERVER,
            port=SMTP_PORT,
            login=FROM_ADDR,
            password=FROM_ADDR_PASSWORD,
            
            tls=True,
            timeout=10
        )

        server.send(envelope)
