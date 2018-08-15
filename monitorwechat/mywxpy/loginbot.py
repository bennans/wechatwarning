from wxpy import *
from wechat_sender import *

import os
def loginb():
    path = os.path.abspath(os.path.dirname(os.getcwd()))+'\\static\\qr.png'
    bot = Bot(qr_path=path)
    user = bot.groups().search('监控测试')[0]
    listen(bot,token='user',receivers=[user])
loginb()