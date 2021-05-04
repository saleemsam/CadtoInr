# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:53:13 2021

@author: USER
"""

from flask import Flask
from flask_mail import Mail, Message

import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

url='https://www.google.com/search?q=cad+to+inr&ei=4gV4YOTvHNXy9QPdn4ngCQ&oq=cad+to+inr&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEEMyBwgAELADEENQAFgAYP6sIGgBcAJ4AIAByQGIAckBkgEDMi0xmAEAqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwjk6Ku-9v_vAhVVeX0KHd1PApwQ4dUDCA4&uact=5'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
req = soup.find_all("span", {"class":"qXLe6d epoveb"})
print(req)

Data = []
for i in req:
    Data.append(i.get_text())

a=Data[0].split()[0]
print(a)

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'saleemchitra15@gmail.com'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'saleemchitra15@gmail.com', recipients = ['saleemchitra15@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail.The Current Value is "+str(a)
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   if float(a)>59.0:
       app.run(debug = True)
   else:
       exit(0)
