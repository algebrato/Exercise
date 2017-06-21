import httplib as ht
import smtplib as smtp
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def my_sender_mail(mailfrom,mailto,subject):
    
    msg = MIMEMultipart()
    msg['From'] = mailfrom
    msg['To'] = mailto
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg['Data'] = "Testo"

    f='risultati.pdf'

    with open(f, "rb") as fil:
        part = MIMEApplication( fil.read(), Name=basename(f))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
    
    server = smtp.SMTP('192.168.0.3')
    server.set_debuglevel(1)
    server.sendmail(mailfrom, mailto, msg.as_string())
    server.quit()


if __name__ == '__main__':

    while 1:
        conn=ht.HTTPConnection('plasma.fisica.unimi.it')

        try:
            conn.request('GET','/assets/materiale/ED-scritto_24_02_2017_risultati.pdf')
            #conn.request('GET','/assets/materiale/ED-scritto_20_06_2017_risultati.pdf')
        except Exception as e:
            print(type(e))

        res=conn.getresponse()

        if res.reason == "OK":
            cont=res.read()
            f = open("risultati.pdf", "w")
            f.write(cont)
            f.close()

            print "Send Mail..."
            
            my_sender_mail("algebrato@lcm.mi.infn.it","linuxfree2@gmail.com","Risultati-ED")
            conn.close()
            break

        conn.close()







