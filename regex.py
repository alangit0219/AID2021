"""
	regex.py	re模塊	功能函數演示
"""

import re

#目標字符串
s = "Alex:1995,Sunny:1993"
pattern = r"\w+:\d+"	#正則表達式

#re 模塊調用findall
l = re.findall(pattern,s)
print(l)

#compile 對象調用findall
regex = re.compile(pattern)
l = regex.findall(s)
print(l)

regex = re.compile(pattern)
l = regex.findall(s,0,12)	#匹配範圍
print(l)

# 按照正則表達式內容切割字符串
l = re.split(r'[:,]',s)
print(l)

#替換目標字符串
s = re.sub(r':','-',s,1)
print(s)

s = re.subn(r':','-',s)
print(s)


