from pyrogram import Client, filters
import platform
import random
import string
import threading
import time
import os
from os import system
from random import randint

import requests

bot = 'ts'
api_id = "5118097"
api_hash = "7154fbfbea65a0727ca70e897cf74dfb"
bot_token = "1909832912:AAEwzz9rugt7wLmFJKooFSuqIgHL2b0fpxM"
app = Client(
    bot,
    api_id,
    api_hash,
    bot_token
)

@app.on_message(filters.command('start', ["/","#"]))
async def start(Client, msg):
  await app.send_message(msg.chat.id, "Non fare tanti account, massimo 50.\n\n/gen (num account)")
  

@app.on_message(filters.command('gen', ["/", "#"]))
async def gen(Client, msg):
  
  if platform.system() == "Windows":  # checking OS
    title = "windows"
  else:
      title = "linux"

  def randomName(size=100, chars=string.digits):
      value = randint(0,999)
      return f'saettamcskull{value}'




  global maxi
  global created

  created = 0
  errors = 0

  class proxy():
      def update(self):
          while True:


              data = ''
              urls = ["https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&ssl=yes"]
              for url in urls:
                  data += requests.get(url).text
                  self.splited += data.split("\r\n") #scraping and splitting proxies
              time.sleep(600)
      
      def get_proxy(self):
          random1 = random.choice(self.splited) #choose a random proxie
          return random1
      def FormatProxy(self):
        proxyOutput = {'https' :'socks4://'+self.get_proxy()}
        return proxyOutput

      def __init__(self):
          self.splited = []
          threading.Thread(target=self.update).start()
          time.sleep(3)

  proxy1 = proxy()

  def creator():
    global maxi
    global created
    global errors

              
    s = requests.session()

    email = randomName()
    password = "Skull123!"

    data={
          "displayname":"Josh",
          "creation_point":"https://login.app.spotify.com?utm_source=spotify&utm_medium=desktop-win32&utm_campaign=organic",
          "birth_month":"12",
          "email":email + "@gmail.com",
          "password":password,
          "creation_flow":"desktop",
          "platform":"desktop",
          "birth_year":"1991",
          "iagree":"1",
          "key":"4c7a36d5260abca4af282779720cf631",
          "birth_day":"17",
          "gender":"male",
          "password_repeat":password,
          "referrer":""
        }

    try:

            r = s.post("https://spclient.wg.spotify.com/signup/public/v1/account/",data=data,proxies=proxy1.FormatProxy())
            if '{"status":1,"' in r.text:
                open("created.txt", "a+").write(email + "@gmail.com:" + password + "\n")
                created += 1
    except:
      pass

          

  maxi = 1

  maxthreads = 50
  num = 0

  while num < maxthreads:
      num += 1
      threading.Thread(target=creator).start()  # Start Checking Thread

  time.sleep(7)

  fileObject = open("created.txt", "r")
  data = fileObject.read()
  await app.send_message(msg.chat.id, f"{data}")
  f = open('created.txt', 'r+')
  f.truncate(0)

  


app.run()