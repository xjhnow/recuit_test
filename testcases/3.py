import re


data2 = {'id':'#id#','isSelfEnrollment':'1'}
data2 = str(data2)

r = r'#(.+?)#'
res = re.search(r,data2)
print(res)
a = res.group()
print(a)
key = res.group(1)
print(key)

a = '660B8D2D5359FF6F94F8D3345698F88C'
print(len(a))