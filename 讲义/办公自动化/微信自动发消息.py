from wxauto import WeChat

# 初始化微信
wx = WeChat()

# 同步微信好友列表
wx.GetSessionList()

# 发送消息的好友
wx.ChatWith("汪昊")

# 发送消息
wx.SendMsg("你好，我是Python脚本")
