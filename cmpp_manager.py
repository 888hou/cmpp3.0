
from cmpp_handle import *
from cmpp_net  import *


class cmppManager(object):

	connectedISMG = False
	'''
 	@cmpp需要的配置信息
	'''
	@staticmethod
	def initConfig():
		cmppManager.setServerIP("127.0.0.1")
		cmppManager.setServerPort(10086)
		cmppManager.setSrcID("100861121")
		cmppManager.setSPID("417393")
		cmppManager.setServiceID("AHB0090102")
		cmppManager.setPassword("888888")

	'''
	 @发送短信,也是短信模块的入口函数
	'''
	@staticmethod
	def submitMessage(message, number):
		if cmppManager.connectedISMG != True:
			cmppManager.initConfig()
			ret,sockFd = cmppHandle.connectISMG(cmppManager.IP, cmppManager.PORT)
			if  ret == 0 and sockFd > 0:
				cmppManager.connectedISMG = True
				#认证成功后，开启新的现场进行保活处理
				cmppHandle.service(sockFd)
			else :
				print('connected ISMG failed')
				cmppManager.connectedISMG = False
				return -1 
		if cmppHandle.sendMessage(sockFd, message, number) == 0 :
			print("send message success")

		else:
			print("send message failed")

	#网关IP
	@staticmethod
	def getServerIP():
		return cmppManager.IP 
	@staticmethod
	def setServerIP(ip):
		cmppManager.IP = ip
	

	#网关端口
	@staticmethod
	def getServerPort():
		return cmppManager.PORT
	@staticmethod 
	def setServerPort(port):
		cmppManager.PORT = port
	
	#服务代码
	@staticmethod
	def getSrcID():
		return cmppManager.SRCID
	@staticmethod
	def setSrcID(srcid):
		cmppManager.SRCID = srcid 

	#企业代码
	@staticmethod
	def getSPID():
		return cmppManager.SPID
	@staticmethod
	def setSPID(spid):
		cmppManager.SPID = spid 

	
	# 业务代码
	@staticmethod
	def getServiceID():
		return cmppManager.SERVICEID 
	@staticmethod
	def setServiceID(serviceid):
		cmppManager.SERVICEID = serviceid 

	#密码
	@staticmethod
	def getPassword():
		return cmppManager.PWD
	@staticmethod
	def setPassword(pwd):
		cmppManager.PWD = pwd 



if __name__ == "__main__":
	
	cmppManager.submitMessage("Helloworld", "10086")




