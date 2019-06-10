# 输出1-2+3-4+5-6+…99的和
s = 1
for i in range(2,4):
  print('$$',i)
  if (i%2)==1:
      s+=i
  else:
      s-=i
print(s)

