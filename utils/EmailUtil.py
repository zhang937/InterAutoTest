from config.Conf import ConfigYaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
class SendEmail:
    def __init__(self,smtp_addr,username,password,recv,title,conntent=None,file=None):
        self.smtp_addr=smtp_addr
        self.username=username
        self.password=password
        self.revc=recv
        self.title=title
        self.conntent=conntent
        self.file=file
    def send_mail(self):
        msg=MIMEMultipart()
        msg.attach(MIMEText(self.conntent,_charset="utf-8"))
        msg["Subject"]=self.title
        msg["From"]=self.username
        msg["To"]=self.revc
        if self.file:
            att=MIMEText(open(self.file).read())
            att["Content-Type"]='application/octet-stream'
            att["Conntent-Disposition"]="attachment;filename='%s'"%self.file
            msg.attach( att)
        self.smtp=smtplib.SMTP(self.smtp_addr,port=25)
        self.smtp.login(self.username,self.password)#密码为邮箱授权码。
        self.smtp.sendmail(self.username,self.revc,msg.as_string())
if __name__ == '__main__':
    tst=ConfigYaml().get_email_info()
    em=SendEmail(tst["smtpserver"],tst["useremail"],tst["password"],tst["reseremail"],"接口测试用例测试","123456")
    em.send_mail()