import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formatdate

"""
Gmailでメールを送信するプログラム
このプログラムを実行するには、利用するGmailアカウント側で
アプリのパスワードを生成する必要がある
"""

use_name = 'yu.tsujibayashi.wk@gmail.com'
# アプリが生成したパスワード
password = 'i j z w i t h d m o p d n w g c'

subject = 'test mail from python'
body_text = '[重要！！]test mail'

from_address = 'yu.tsujibayashi.wk@gmail.com'
to_address = 'yu.tsujibayashi.wk@gmail.com'

smtp_host = 'smtp.gmail.com'
smtp_port = 587

# Connecting To SMTP Server
smtp_obj = smtplib.SMTP(smtp_host, smtp_port)
smtp_obj.starttls()
smtp_obj.login(use_name, password)

# Create a message
msg = MIMEText(body_text)
msg['Subject'] = subject
msg['From'] = from_address
msg['To'] = to_address
msg['Date'] = formatdate()

# Send email
smtp_obj.send_message(msg)
smtp_obj.close()

 

