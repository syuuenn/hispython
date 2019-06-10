import re
string="我除了学习毫无兴趣"
ret=re.search('[\u4e00-\u9fa5]*',string)
# ret=re.split()
# re.sub()
print(ret)