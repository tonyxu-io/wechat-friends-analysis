# -*- coding: UTF-8 -*-
import itchat

# Login to WeChat and Scan the QR Code
itchat.login()

# Get JSON reponse of WeChat friends
friends = itchat.get_friends(update=True)[0:]
# print(friends)