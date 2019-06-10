class Cat(object):
    def  __init__(self,weiba,color,name):
        self.weiba=weiba
        self.color=color
        self.name=name
    def jump(self):
        print()
        print('%s猫可以眺'%(self.name))


hellokitty=Cat("尾巴",'白色','凯蒂')
jiafeimao=Cat('尾巴','黄色','加菲')

#print(hellokitty.weiba)
hellokitty.jump()

