import smtplib
import base64

from email.mime.text import MIMEText

# mailto_list = ["lihan@xxx.com"]
mail_host = "smtphost"
sender_user = "sender"
sender_passw = "passwd"
sender_mail_domain = "xxx.com"

class sendemail():
    def __init__(self,to_list,sub,content):
        self.to_list = to_list
        self.sub = sub
        self.content = content
    def send_mail(self):
        sender = "Ling" + "<" + sender_user + "@" + sender_mail_domain + ">"
        msg = MIMEText(self.content, _subtype='plain', _charset='gb2312')
        msg['Subject'] = self.sub
        msg['From'] = sender
        msg['To'] = self.to_list
        print msg
        try:
            server = smtplib.SMTP()
            server.connect(mail_host)
            ##server.login(sender_user,sender_passw)
            server.sendmail(sender, self.to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False



# if __name__ == '__main__':
#     if send_mail(mailto_list, "hello", "hello world"):
#         print "Send successfully!"
#     else:
#         print "Send failed!"


