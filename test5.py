import time#导入时间模块
def foo():#定义功能模块
    time.sleep(3)#睡眠三秒
    print('aaa')
def decorate(fun):#定义费时函数（嵌套功能）
    def bibao():#定义闭包功能
        start=time.time()#起始时间
        fun()#调用功能函数
        end=time.time()#结束时间
        print('花费的时间是%d'%(end-start))
    return bibao
foo=decorate(foo)
foo()
