# 简单的基于wxpy和WeChat-sender将告警信息转发到微信群聊

* wxpy 在 itchat 的基础上，通过大量接口优化提升了模块的易用性，并进行丰富的功能扩展

* wechat_sender 是基于 wxpy 和 tornado 实现的一个可以将你的网站、爬虫、脚本等其他
  应用中各种消息 （日志、报警、运行结果等） 发送到微信的工具
## 准备
>* 在python中安装wxpy
   <br>`pip install wxpy`
>* 在python中安装 wechat-sender
   <br>`pip install wechat-sender`
## 首先wxpy中进行微信的登陆创建一个机器人
```
    from wxpy import *

    bot = Bot()
```
## 获取好友
```
    #获取好友
    Bot.friends()
    #获取群聊
    Bot.groups()
```
## 搜索好友群聊
```
    #搜索名字含有max的朋友
    user=bot.friends().search('MAX')[0]
    #搜索名字含有 监控 的群聊
    user=bot.groups().search('监控')[0]
```
## wechat-sender listen监听
```
    from wechat_sender import * 
    
    #监听bot 标识为user 发送消息对象为user
    listen(bot,token='user',receivers=[user])
```
## 在其他地方使用
```
    from wechat_sender import *

    def wechatsend(mess):
        #获取标识为user的sender对象
        sender = Sender(token='user')
        #向sender里的user好友发送消息
        sender.send(mess)
```