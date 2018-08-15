from wechat_sender import *

def wechatsend(mess):
    sender = Sender(token='user')
    sender.send(mess)