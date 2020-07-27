# 发送带附件的邮件
import os
import smtplib # 负责邮件发送
from email.mime.text import MIMEText # 负责发送普通邮件
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
body_str ='''
<h3 align="center">自动化测试报告</h3>
<table border="2" align="center" width='50%',height='400'>
<tr><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td></tr>
</table>
'''
msg.attach(MIMEText(body_str,'html','utf-8'))  #邮件html内容

# 发送人 收件人 抄送人 邮箱主题 填写
msg['from'] = '398260536@qq.com'
msg['to'] = '398260536@qq.com'
msg['Cc'] = '1092595268@qq.com' # 多个人用切割方式处理
msg['subject'] = 'P1P2自动化测试框架学习'

# 添加附件
html_path = os.path.join(os.path.dirname(__file__),'..','test_reports/P1P2接口自动化测试报告V1.4/P1P2接口自动化测试报告V1.4.html')
attach_file = MIMEText(open(html_path,'rb').read(),'base64','utf-8') # read()读取所有数据
attach_file['Content-Type']='application/octet-stream'
attach_file.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试报告V1.4.html"))
# attach_file['Content-Disposition']='attachment;filename="V1.4.html"' # 不能写中文
msg.attach(attach_file)

smtp = smtplib.SMTP() # 创建smtp对象
smtp.connect('smtp.qq.com') # 连接smtp主机
smtp.login(user='398260536@qq.com',password='mwmmpnggdjxpbiec') #邮箱登录
#发邮件的发送人员，接收人员(列表)。
smtp.sendmail('398260536@qq.com',['398260536@qq.com'],msg.as_string())

