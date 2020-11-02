#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = '邮箱工具类'
__mtime__ = '2016/6/23'
"""
import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import sys


class SimpleMail(object):
    def __init__(self, from_name, to_addr, to_name):
        self.stmp_server = 'smtp.163.com'
        self.from_addr = 'name@mail.com'
        self.from_passwd = 'xxxxxx'
        self.from_name = from_name
        self.to_addr = to_addr
        self.to_name = to_name

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr) else addr))

    def sendmail(self, subject, content):
        try:
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['From'] = self._format_addr('%s <%s>' % (self.from_name, self.from_addr))
            msg['To'] = self._format_addr('%s <%s>' % (self.to_name, self.to_addr))
            msg['Subject'] = Header(subject, 'utf-8').encode()

            server = smtplib.SMTP(self.stmp_server, 25)
            # server.set_debuglevel(1)
            server.login(self.from_addr, self.from_passwd)
            server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
            server.quit()
            print ("邮件发送成功")
        except smtplib.SMTPException:
            print ("Error: 无法发送邮件, %s - %s" % (sys.exc_info()[0].args[0], sys.exc_info()[0].args[1]))
        except Exception:
            print (json.dumps(sys.exc_info()[0].args))


class TargetMail(SimpleMail):
    def __init__(self):
        self.from_name = u'from_name'
        self.to_addr = 'name@mail.com'
        self.to_name = u'to_name'
        super(TargetMail, self).__init__(self.from_name, self.to_addr, self.to_name)

    def sendmail(self, subject, content):
        super(TargetMail, self).sendmail(subject, content)

# 发送邮件
if __name__ == '__main__':
    TargetMail().sendmail("标题","内容")