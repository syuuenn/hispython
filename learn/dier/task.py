def removeOuterParentheses(s1):
    num1 = 0
    num2 = 0
    s2 = ''
    s3 = ''
    if s1 != '':
        for i in range(len(s1)):
            if i=='(':
                num1+=1
            elif i==')':
                num2+=1
            else:
                break
            if num1!=0 and num2!=0 and num1==num2:
                s2 = s1[0:(num1+num2)]
                s1-=s2



removeOuterParentheses("(()(()))")
