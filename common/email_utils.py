import os
import smtplib # 负责邮件发送
from common.localconfig_utils import local_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailUtils():
    def __init__(self,smtp_body,smtp_attch_path=None):
        self.smtp_server = local_config.SMTP_SERVER
        self.smtp_sender = local_config.SMTP_SENDER
        self.smtp_password = local_config.SMTP_PASSWORD
        self.smtp_cc = local_config.SMTP_CC
        self.smtp_receiver = local_config.SMTP_RECEIVER
        self.smtp_subject = local_config.SMTP_SUBJECT
        self.smtp_body = smtp_body
        self.smtp_attch = smtp_attch_path # 附件路径


    def mail_message_body(self):
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] =  self.smtp_cc # 多个人用切割方式处理
        message['subject'] =  self.smtp_subject
        message.attach(MIMEText(self.smtp_body,'html','utf-8'))
        if self.smtp_attch: # 附件路径
            attach_file = MIMEText(open(self.smtp_attch, 'rb').read(), 'base64', 'utf-8')  # read()读取所有数据
            attach_file_name = os.path.basename(self.smtp_attch)# 附件名称
            attach_file['Content-Type'] = 'application/octet-stream'
            attach_file.add_header("Content-Disposition", "attachment", filename=("gbk", "",attach_file_name ))
            message.attach(attach_file)
        return message
    def send_mail(self):
        smtp = smtplib.SMTP()  # 创建smtp对象
        smtp.connect(self.smtp_server)  # 连接smtp主机
        smtp.login(user=self.smtp_sender, password=self.smtp_password)  # 邮箱登录
        # 发邮件的发送人员，接收人员(列表)。
        smtp.sendmail(self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.split(','),self.mail_message_body().as_string())

if __name__ == '__main__':
    # EmailUtils('<h3 align="center">自动化测试报告</h3>').send_mail()

    # 发送附件
    html_path = os.path.join(os.path.dirname(__file__), '..', 'test_reports/P1P2接口自动化测试报告V1.4/P1P2接口自动化测试报告V1.4.html')
    EmailUtils('<h3 align="center">自动化测试报告</h3>',html_path).send_mail()
