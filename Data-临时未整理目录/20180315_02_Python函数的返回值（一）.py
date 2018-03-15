'''



'''

'''
def ZCY():
    A = 123
    A += 1
    print(A)            #输出会显示124，可以把该条设置为正常发邮件操作，不用输出
    return 123

Z = ZCY()               #获取返回值
print(Z)
'''


def show():
    print('aaa')
ret = show2()
print(ret)                         #如果没有定义返回值，那么默认为None



import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mail():
    ret = True
    try:
        msg = MIMEText('邮件内容','plain','utf-8')
        msg['From'] = formataddr(['张辰','发件人邮箱'])
        msg['To'] = formataddr(['走人','2421236226@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP('smtp.126.com',25)
        server.login('zhangchen@126.com','邮箱密码')
        server.sendmail('zhangchen@126.com',['2421236226@qq.com',],msg..as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

ret = mail()
if ret:
    print("发送成功")
else:
    print("发送失败")






