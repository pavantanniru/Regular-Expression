import re
phone = "2004-959-559 # This is Phone Number"
num=re.sub(r'#.*$','',phone)
print(num)
num=re.sub(r'#.*$','',phone)
print(num)
phnum=re.sub(r'-','',num)
print(phnum)