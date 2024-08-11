micropython模块有三种编写方法：

    1. 独立于MicroPython源码之外
    
        见官方文档：https://github.com/micropython/micropython/blob/master/docs/develop/cmodules.rst 

        参考示例见mircopython/examples/usercmodule

    2. 内建

        象micorpython modesp modmachine等模块一样，可以参考 https://blog.csdn.net/solar_Lan/article/details/88913109 里面的的文章；

    3. 调用已有模块
    
        MicroPython底层已有的MicroPython驱动，实现自己的模块驱动，像官方MicroPython/drivers/dht/dht.py 一样。
