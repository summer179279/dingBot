import sys
import urllib2
import urllib
import json
import datetime

class DtalkRobot(object):
	"""docstring for DtRobot"""
	webhook = ""
	def __init__(self, webhook):
		super(DtalkRobot, self).__init__()
		self.webhook = webhook

	def sendText(self, msg, isAtAll=False, atMobiles=[]):
		data = {"msgtype":"text","text":{"content":msg},"at":{"atMobiles":atMobiles,"isAtAll":isAtAll}}
		return self.post(data)

	def sendMarkdown(self, title, text):
		data = {"msgtype":"markdown","markdown":{"title":title,"text":text}}
		return self.post(data)

	def sendLink(self, title, text, messageUrl, picUrl=""):
		data = {"msgtype": "link","link": {"text": text, "title":title,"picUrl": picUrl,"messageUrl": messageUrl}}
		return self.post(data)

	def sendActionCard(self, actionCard):
		data = actionCard.getData();
		return self.post(data)

	def sendFeedCard(self, links):
		data = {"feedCard":{"links":links},"msgtype":"feedCard"}
		return self.post(data)

	def post(self, data):
		post_data = json.JSONEncoder().encode(data)
 		print post_data
		req = urllib2.Request(self.webhook, post_data)
 		req.add_header('Content-Type', 'application/json')
		content = urllib2.urlopen(req).read()
		return content

class ActionCard(object):
	"""docstring for ActionCard"""
	title = ""
	text = ""
	singleTitle = ""
	singleURL = ""
	btnOrientation = 0
	hideAvatar = 0
	btns = []

	def __init__(self, arg=""):
		super(ActionCard, self).__init__()
		self.arg = arg

	def putBtn(self, title, actionURL):
		self.btns.append({"title":title,"actionURL":actionURL})

	def getData(self):
		data = {"actionCard":{"title":self.title,"text":self.text,"hideAvatar":self.hideAvatar,"btnOrientation":self.btnOrientation,"singleTitle":self.singleTitle,"singleURL":self.singleURL,"btns":self.btns},"msgtype":"actionCard"}
		return data
		
class FeedLink(object):
	"""docstring for FeedLink"""
	title = ""
	picUrl = ""
	messageUrl = ""

	def __init__(self, arg=""):
		super(FeedLink, self).__init__()
		self.arg = arg
		
	def getData(self):
		data = {"title":self.title,"picURL":self.picUrl,"messageURL":self.messageUrl}
		return data
		

webhook = "https://oapi.dingtalk.com/robot/send?access_token=841d1720c7fd87a0d3565e81d52a62459c3dc2e04e1a092096aa4afc29cc1360"
if __name__ == "__main__":

    robot = DtalkRobot(webhook)

    today = datetime.datetime.now()
    iloveyou = datetime.datetime(2018, 12, 20)
    print robot.sendText( "This is "+today.strftime('%Y-%m-%d')+" today. There are "+str((iloveyou-today).days)+" days till next date with Summer.", False, [])
