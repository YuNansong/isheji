from dingtalkchatbot.chatbot import DingtalkChatbot
from common.getYaml import switchInfo
# ===============================
# 发送钉钉消息
# ===============================
class SendDingTalk:

    # 发送钉钉提醒开关
    def getSwitch(self):
        isOn = switchInfo['switchInfo']['isOn']
        return isOn
    # 发送钉钉提醒，is_at_all=False 不@所有人
    def sendDingTalkMsg(self,msg):
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=2c62d40e4ee70f16565ea87e0535f6c8666641a5f3730016588d2c335cc0ee45"
        xiaoding = DingtalkChatbot(webhook)
        isOn = self.getSwitch()
        if isOn == 1:
            xiaoding.send_text(msg="爱设计-" + msg, is_at_all=False)  # 如果钉钉群设置了安全关键词，发消息必须有关键词内容
            return msg
        else:
            return ""