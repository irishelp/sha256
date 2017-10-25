# -*- coding: utf-8 -*-
# version python 3.5

import hashlib
import json
import sys

def	requestsign( message,signKey):
#    print (message)
	message1=json.dumps(message,sort_keys=True)
	
	message2 = json.loads(message1)

	requestkey=[]
	
	for key in message2:
		requestkey.append(key)
	
#	对请求报文参数进行排序
	requestkey.sort()	  

#	组签名字符串stringSignTemp
	stringSignTemp=''
	for lenth in requestkey:
		if lenth!='sign':
#			print (type(lenth))
#			print (type(message2[lenth]))
			stringSignTemp += lenth + '=' + message2[lenth] + '&'
#			print (stringSignTemp)
		else:
			print ("跳过sign参数拼接")

#	去掉尾部的&符号
	stringSignTemp1 = stringSignTemp[:-1]

#   拼接签名密钥
	stringSignTemp1 += signKey
#	print (stringSignTemp1)

	sha256 = hashlib.sha256()
	sha256.update(stringSignTemp1.encode('utf-8'))
	signvalue = sha256.hexdigest()
	print ("签名256加密结果：", signvalue )
	
	if message2['sign']==signvalue:
		print ('签名验证通过：pass')
		return (json.dumps(message2))
	else:
		print ('签名验证失败：fail')
		message2['sign']=signvalue
		print ('更新签名字段为最新的值:')
		print (message2['sign'])
		return (json.dumps(message2))

		
if __name__ == '__main__':
	
	signKey='zsdfyreuoyamdphhaweyrjbvzkgfdycs'
	message= {
	"txndir":"Q",
	"busicd":"PAUT",
	"inscd":"10134001",
	"chcd":"WXP",
	"mchntid":"402077158140001",
	"txamt":"000000000001",
	"orderNum":"201710250022",
	"sign":"9ab4f39af6acb13fb8bec034270120544d7d649955621422becc8e58e7ab1bd8",
	"version":"2.2",
	"signType":"SHA256",
	"charset":"utf-8",
	"subject":"20171012Test",
	"backUrl":"http://test.quick.ipay.so"
	}
	
	requestsign(message,signKey)
#	if len(sys.argv)==3:
#		print (sys.argv[1])
#		print (sys.argv[2])
#		requestsign(sys.argv[1],sys.argv[2])
#	else:
#		print ('参数不对')
	
	
	