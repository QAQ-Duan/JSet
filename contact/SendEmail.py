def SendEmail(receiver,dic):
    import smtplib
    import email

    # 负责构造文本
    from email.mime.text import MIMEText
    # 负责构造图片
    from email.mime.image import MIMEImage
    # 负责将多个对象集合起来
    from email.mime.multipart import MIMEMultipart
    from email.header import Header

    mail_host = "smtp.163.com"
    mail_sender = "qhduan99066@163.com"
    mail_license = "WCJPIGYLOOTQXARF"
    mail_receivers = receiver

    mm = MIMEMultipart('related')

    # 邮件主题
    subject_content = """留言通知"""
    # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["From"] = "<qhduan99066@163.com>"
    # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    mm["To"] = "<"+receiver+">"
    # 设置邮件主题
    mm["Subject"] = Header(subject_content,'utf-8')

    # 邮件正文内容
    body_content = "你好，"+dic['name']+"进行了留言，内容为"+dic['content']+"他的联系方式是"+dic['phone']
    # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
    message_text = MIMEText(body_content,"plain","utf-8")
    # 向MIMEMultipart对象中添加文本对象
    mm.attach(message_text)

    # 创建SMTP对象
    stp = smtplib.SMTP()
    # 设置发件人邮箱的域名和端口，端口地址为25
    stp.connect(mail_host, 25)  
    # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
    stp.set_debuglevel(1)
    # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    stp.login(mail_sender,mail_license)
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    stp.sendmail(mail_sender, mail_receivers, mm.as_string())
    print("邮件发送成功")
    # 关闭SMTP对象
    stp.quit()

if __name__ == "__main__":
    pass