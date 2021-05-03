# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:21:37 2021

@author: USER
"""



import requests
from bs4 import BeautifulSoup
from lxml import html


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

def triggermail():
    
    import pythoncom
    pythoncom.CoInitialize()
    import win32com.client as win32
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = "saleemchitra15@outlook.com"
    #mail.To = "srinath.chidurala@yash.com; rahul.kondhalkar@yash.com"
    #mail.Cc = "divyanshu.sharma@yash.com; saleem.chitrachedu@yash.com"
    mail.Subject = 'CAD TO INR price'
    mail.Body = 'CAD to INR rate is changed to'+ str(Data)
    
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi,<br><br>
        
           CAD to INR rate is modified to Data. 
           <br>Please see modified URL details in attached document. <br><br>
           
           Please Note: This is a system generated email.<br><br>
        </p>
      </body>
    </html>
    """
    mail.HTMLBody = mail.Body
    #mail.HTMLBody = html #this field is optional
    # To attach a file to the email (optional):
    #attachment  = "D:\\Data Science\\webscraping\\Modified_articles.csv"
    #mail.Attachments.Add(attachment)
    mail.display()
    mail.Send()

if float(a)<60.0:
    triggermail()