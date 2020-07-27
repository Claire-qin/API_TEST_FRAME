import smtplib # 负责邮件发送
from email.mime.text import MIMEText # 负责发送普通邮件

# msg = MIMEText('Hello,P1P2','html','utf-8') #邮件内容
body_str ='''
<h3 align="center">自动化测试报告</h3>
<table border="2" align="center" width='50%',height='400'>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
</table>
'''
msg = MIMEText(body_str,'html','utf-8') #邮件html内容
# 发送人 收件人 抄送人 邮箱主题 填写
msg['from'] = '398260536@qq.com'
msg['to'] = '398260536@qq.com'
msg['cc'] = '1092595268@qq.com'
msg['subject'] = 'P1P2自动化测试框架学习'

smtp = smtplib.SMTP() # 创建smtp对象
smtp.connect('smtp.qq.com') # 连接smtp主机
#邮箱登录
smtp.login(user='398260536@qq.com',password='mwmmpnggdjxpbiec')
#发邮件的发送人员，接收人员(列表)。
smtp.sendmail('398260536@qq.com',['398260536@qq.com'],msg.as_string())

