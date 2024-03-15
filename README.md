# ChatGPT_Python_Library
A python library to directly access chatGPT without needing an api or account or anything else!

# Install and import to python project
```
E='ChatGPT.py';B=exit;A=print;from os import system as F,listdir as G
if not E in G():
	try:from requests import get
	except:
		F('pip install requests')
		try:from requests import get
		except:A('Error! Please Install Requests Library');B()
	try:
		C=get('https://mr-r0ot.github.io/ChatGPT_Python_Library/ChatGPT.py')
		if C.status_code!=200:A('GiHub Error!');B()
	except:A('NetWork Error!');B()
	D=open(E,'w+');D.write(C.text);D.close()
import ChatGPT
```



# Use
```
ChatGPT(query='hello'  ,log=False) #Your can set log=True fro show logs
```




# Test
```
>>> print( ChatGPT(query='hello',log=False) )
Hello! How can I assist you today?


>>> print( ChatGPT(query='hello',log=True) )
 [ LOG + ]   Importing librarys
 [ LOG + ]   Creatting Options
 [ LOG + ]   Running firefox driver
 [ LOG + ]   connecting to server
 [ LOG + ]   connected
 [ LOG + ]   Sending data to server..
 [ LOG + ]   Getting Output
 [ LOG + ]   Quittng from driver
Hello! How can I assist you today?
```



CoDeD By NICOLA (TELEGRAM : t.me/black_nicola)
