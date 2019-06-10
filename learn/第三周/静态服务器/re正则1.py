import re
# str_1='a879 aga 嬉しい'
# ret=re.match('a.{3}\s\w{3}\s\w{3}',str_1)
# print(ret.group())
#\s\D{3}\s\w{3}


# ret1=re.match('[\d^4]','5')
ret=re.match('Host:\s[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:','Host: 256.255.255.255:8000')
print(ret.group())
# [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-65536]