:mod:`Builtin` --Builtins functions and exceptions 
================================

All built-in functions and exceptions are described here. They can also be obtained through the ``builtins`` module.



Function
-------------------

.. function:: abs()

Returns the absolute value of a number. Arguments can be integers or floating-point numbers. If the argument is a complex number, return its module. 




.. function:: all()

If all elements of `iterable` are true (or the iterator is empty), return to  `True` .

Equivalent to::

    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True

.. function:: any()

If any element of `iterable` is true, return `True`  . If the iterator is empty, return to `False` .

Equivalent to::

    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False

.. function:: bin()

Convert an integer to a binary string prefixed with “0b” .

::

    >>> bin(3)
    '0b11'
    >>> bin(-10)
    '-0b1010'

.. class:: bool()

Used to convert a given parameter to a boolean type. If there is no parameter, return `False` .

::

    >>>bool()
    False
    >>> bool(0)
    False
    >>> bool(1)
    True
    >>> bool(None)
    False


.. class:: bytearray()

Return to a new bytes array. The byte array class is a variable sequence that contains integers in the range 0 < = x < 256.

::

    >>>bytearray()
    bytearray(b'')
    >>> bytearray([1,2,3])
    bytearray(b'\x01\x02\x03')
    >>> bytearray('mpython')
    bytearray(b'mpython')
    >>>

.. class:: bytes()

The bytes function returns a new bytes object, which is an immutable sequence of integers in the range 0 < = x < 256. It is an immutable version of byte array. See CPython document： `bytes <https://docs.python.org/3.5/library/functions.html#bytes>`_

::

    >>>a = bytes([1,2,3,4])
    >>> a
    b'\x01\x02\x03\x04'
    >>> type(a)
    <class 'bytes'>
    >>>
    >>> a = bytes('hello')
    >>>
    >>> a
    b'hello'
    >>> type(a)
    <class 'bytes'>
    >>>

.. function:: callable()

Function to check whether an object is callable. If true is returned, the object called may still fail; however, if false is returned, the object called will never succeed.

::

    >>>callable(0)
    False
    >>> callable("mpython")
    False
    
    >>> def add(a, b):
    ...     return a + b
    ... 
    >>> callable(add)             # function return True
    True
    >>> class A:                  # class
    ...     def method(self):
    ...             return 0
    ... 
    >>> callable(A)               # class return True
    True
    >>> a = A()
    >>> callable(a)               # not realized __call__, return False
    False
    >>> class B:
    ...     def __call__(self):
    ...             return 0
    ... 
    >>> callable(B)
    True
    >>> b = B()
    >>> callable(b)               # realized __call__, return True
    True

.. function:: chr()

Returns the string format of the character whose 'Unicode'  `Unicode` code is an integer 'I' .

::

    >>>chr(0x30)
    '0'
    >>> chr(97) 
    'a'
    >>> chr(8364)
    '€'

.. decorator:: classmethod()

Encapsulate method.

A class method take itself as the first argument, just like an instance example itself as the first argument. Be accustomed to use the following declare class methods::

    class C:
        @classmethod
        def f(cls, arg1, arg2, ...): ...

@classmethod is a form called the decorator of a function. Class methods can be called on a class (for example, c.f()) or on an instance (for example, c(). F()).
Class instances other than the class to which they belong will be ignored. If the class method is invoked on the derived class of its class, The derived class object is passed in as the implied first parameter.

.. function:: compile(source, filename, mode[, flags[, dont_inherit]])

Compile a string into bytecode. For details. refers to CPython document： `compile <https://docs.python.org/zh-cn/3.7/library/functions.html#compile>`_

::

    >>>str = "for i in range(0,10): print(i)" 
    >>> c = compile(str,'','exec')   # Compile to bytecode object 
    >>> c
    <code object <module> at 0x10141e0b0, file "", line 1>
    >>> exec(c)
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> str = "3 * 4 + 5"
    >>> a = compile(str,'','eval')
    >>> eval(a)
    17

.. class:: complex([real[, imag]])

Returns a complex number with a value of real + imag * 1J, or converts a string or number to a complex number. If the first parameter is a character string, it is interpreted as a complex number and must be called without a second parameter. The second parameter cannot be a character string. Each argument can be of any numeric type (including complex numbers).
If imag is omitted, the default value is zero, and the constructor performs numerical conversion like int and float. If both arguments are omitted, 0j is returned.

::

    >>>complex(1, 2)
    (1 + 2j)
    
    >>> complex(1)    # number
    (1 + 0j)
    
    >>> complex("1")  # Treat as string
    (1 + 0j)
    
    # Note：Not to have spaces on both sides of the "+" sign, otherwise, an error will be reported, it cannot be written as "1 + 2j". To avoid error, it should be written as "1+2j". 
    >>> complex("1+2j")
    (1 + 2j)

.. function:: delattr(obj, name)

setattr() Related functions. An argument is an object and a string. The string must be a property of the object. If the object allows it, the function deletes the specified property.
Such as delattr(x, 'foobar') equivalent to del x.foobar .

::

    class Coordinate:
        x = 10
        y = -5
        z = 0
    
    point1 = Coordinate() 
    
    print('x = ',point1.x)
    print('y = ',point1.y)
    print('z = ',point1.z)
    
    delattr(Coordinate, 'z')
    
    print('--delete z after attribute--')
    print('x = ',point1.x)
    print('y = ',point1.y)
    
    # Trigger error
    print('z = ',point1.z)

----------------------------------------------------------------

.. class:: dict(**kwarg)
.. class:: dict(mapping, **kwarg)
.. class:: dict(iterable, **kwarg)

- ``**kwargs`` -- keyword
- ``mapping`` -- element container.
- ``iterable`` -- iteratable object.

dict() Function to create a dictionary

::

    >>>dict()                        # Create an empty dictionary
    {}
    >>> dict(a='a', b='b', t='t')     # enter keyword
    {'a': 'a', 'b': 'b', 't': 't'}
    >>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # Mapping function mode to construct dictionary
    {'three': 3, 'two': 2, 'one': 1} 
    >>> dict([('one', 1), ('two', 2), ('three', 3)])    # Iterative object method to construct the dictionary
    {'three': 3, 'two': 2, 'one': 1}
    >>>


.. function:: dir(object)

dir() When a function has no parameters, it returns the list of variables, methods and defined types in the current range; when it has parameters, it returns the list of properties and methods of parameters.
If the parameter contains  __dir__()，if it doesn't contains __dir__()，This method will maximize the collection of parameter information.
- ``object`` -- object, variable, type.


.. function:: divmod()

It takes two (non complex) numbers as arguments and returns a pair of quotients and remainder when integer division is performed. Mixed operand type, applicable to the rules of higher arithmetic operators. 
For integers, results are consistent with (a // b, a % b). For floating-point numbers, the result is (q, a % b) ，q is usually math.floor(a / b) but it might be smaller than 1.
In any case, Q * B + a% B and a are basically equal; if a% B is not zero, Its symbol is the same as B, and 0 < = ABS (a% B) < ABS (b).

::

    >>> divmod(7, 2)
    (3, 1)h
    >>> divmod(8, 2)
    (4, 0)
    >>> divmod(8, -2)
    (-4, 0)
    >>> divmod(3, 1.3)
    (2.0, 0.4000001)

.. function:: enumerate(sequence, [start=0])

enumerate() Function is used to combine a traversable data object (such as a list, tuple or string) into an index sequence, and list data and data subscripts. It is generally used in for loop.

- ``sequence`` -- A sequence, iterator, or other object that supports iteration.
- ``start`` -- Subscript start position.

::

    >>>seq = ['one', 'two', 'three']
    >>> for i, element in enumerate(seq):
    ...     print i, element
    ... 
    0 one
    1 two
    2 three

.. function:: eval(expression[, globals[, locals]])

eval() Function to execute a string expression and return the value of the expression.

- ``expression`` -- expression form.
- ``globals`` -- variable scope, global namespace, if provided, it must be a dictionary object.
- ``locals`` -- variable scope, global namespace, if provided, can be any mapping object.


::

    >>>x = 7
    >>> eval( '3 * x' )
    21
    >>> eval('pow(2,2)')
    4
    >>> eval('2 + 2')
    4
    >>> n=81
    >>> eval("n + 4")
    85

.. function:: exec(object[, globals[, locals]])

exec Execute Python statements stored in strings or files, Exec can execute more complex Python code than eval.

- ``object``：Required parameter, indicating the Python code to be specified. It must be a string or code object. If the object is a string, the string is first parsed into a set of Python statements and then executed (unless a syntax error occurs). If the object is a code object, it is simply executed.
- ``globals``：Optional parameter, representing the global namespace (storing global variables), If provided, it must be a dictionary object.
- ``locals``：Optional parameter indicating the current local namespace (storing local variables), If provided, it can be any mapping object. If this parameter is ignored, it will take the same value as globals.

::

    >>>exec('print("Hello World")')
    Hello World
    # Single line statement string
    >>> exec("print ('runoob.com')")
    runoob.com
    
    #  Single line statement string
    >>> exec ("""for i in range(5):
    ...     print ("iter time: %d" % i)
    ... """)
    iter time: 0
    iter time: 1
    iter time: 2
    iter time: 3
    iter time: 4

.. function:: filter(function, iterable)

Used to filter sequence and filter out unqualified elements, Returns an iterator object. If you want to convert it to a list, you can use list () to convert it.

- ``function`` -- Judgement function.
- ``iterable`` -- Iteratable objects.

Filter out all the odd numbers in the list::
 
    def is_odd(n):
        return n % 2 == 1
    
    tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    newlist = list(tmplist)
    print(newlist)


.. class:: float([x])

float() Function to convert integers and strings to floating-point numbers.

::

    >>>float(1)
    1.0
    >>> float(112)
    112.0
    >>> float(-123.6)
    -123.6
    >>> float('123')     # string
    123.0

.. function:: format(value[, format_spec])

Functions for formatting strings str.format()，It enhances string formatting. format Function can accept unlimited arguments, position may not in sequence. The basic syntax is to replace the previous% with {} and:.  For more detailed syntax, please refer to CPython 'Format String Syntax'  <https://docs.python.org/zh-cn/3.7/library/string.html#format-specification-mini-language>`_

::

    >>>"{} {}".format("hello", "world")    # Do not set the specified location, in the default order.
    'hello world'
    
    >>> "{0} {1}".format("hello", "world")  # Set specified location
    'hello world'
    
    >>> "{1} {0} {1}".format("hello", "world")  # Set specified location
    'world hello world

.. class:: frozenset([iterable])

Returns a frozen collection after which no more elements can be added or removed.

- ``iterable`` -- Objects that can be iterated, such as lists, dictionaries, tuples, and so on.


.. function:: getattr(object, name[, default])

Used to return an object property value.

::

    >>>class A(object):
    ...     bar = 1
    ... 
    >>> a = A()
    >>> getattr(a, 'bar')        # Get property bar value
    1
    >>> getattr(a, 'bar2')       # Property bar2 does not exist, triggering exception
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'A' object has no attribute 'bar2'
    >>> getattr(a, 'bar2', 3)    # Property bar2 does not exist, but the default value is set


.. function:: globals()

globals() Function returns all global variables in the current location as dictionary type.

.. function:: hasattr(object, name)

Judgement object if it contains corresponding attributes.

- ``object`` -- object.
- ``name`` -- string，property name.

::

    class Coordinate:
        x = 10
        y = -5
        z = 0
    
    point1 = Coordinate() 
    print(hasattr(point1, 'x'))
    print(hasattr(point1, 'y'))
    print(hasattr(point1, 'z'))
    print(hasattr(point1, 'no'))  # no such attribute

The output::

    True
    True
    True
    False

.. function:: hash(object)

Returns the hash value of the object, (if any). Hash value is an integer. The quick key  use to compare elements in the dictionary. Numeric variables of the same size have the same hash value. 


----------------------------------------------------------------


.. function:: help([object])

Check the detail description for purpose of the function or module. 


.. function:: hex(x)

Converts an integer to a lowercase hexadecimal string prefixed with “0x” .

::

    >>> hex(255)
    '0xff'
    >>> hex(-42)
    '-0x2a'

.. function:: id([object])

Get the id of the object. 

.. function:: input([prompt])

Receive a standard input data and return it as string type.


.. class:: int([x])
.. class:: int(x,base=10)

Converts a string or number to an integer. 

- ``x`` -- String or number. 
- ``base`` -- Decimal number, default decimal 

.. function:: isinstance(object, classinfo)

Returns true if the object argument is an instance of the classInfo argument, or an instance of a (direct, indirect, or virtual) subclass.
If the object is not an object of the given type, the function always returns false. Returns true if classInfo is a tuple of object type (or multiple recursion element groups), and if object is an instance of any of them.  
If classInfo is neither a type nor a type tuple or a recursive tuple of type, a typeError exception will be triggered.

.. admonition:: isinstance() and type() differences

    - `type()` does not consider a subclass as a parent type, and does not consider inheritance.
    - `isinstance()` Consider that the subclass is a parent type, and consider inheritance relationship. 

    *to judge whether two types are the same, recommended to use isinstance()。*


.. function:: issubclass(class, classinfo)

Returns true if class is a subclass (direct, indirect, or virtual) of classInfo. ClassInfo can be a tuple of a class object, and each element in classInfo is checked.
In other cases, a typeError exception will be triggered.

::

    class A:
        pass
    class B(A):
        pass
        
    print(issubclass(B,A))    # return True

    

.. function:: iter(object[, sentinel])

Used to generate iterators. 
- ``object`` -- Object gather that support iterations. 
- ``sentinel`` -- If the second parameter is sent, the parameter object must be a callable object (such as a function). At this time, ITER creates an iterator object, which will be called every time the iterator object's __next__() method, object is called.

::

    >>>lst = [1, 2, 3]
    >>> for i in iter(lst):
    ...     print(i)
    ... 
    1
    2
    3

.. function:: len()

Returns the length of an object (character, list, tuple, etc.) or the number of items. 
::

    >>>str = "runoob"
    >>> len(str)             # String length 
    6
    >>> l = [1,2,3,4,5]
    >>> len(l)               # Number of list elements 
    5

.. class:: list()

Used to convert a tuple or string to a list. 

::

    aTuple = (123, 'Google', 'baidu', 'Taobao')
    list1 = list(aTuple)
    print ("element list : ", list1)

    str="Hello World"
    list2=list(str)
    print ("element list : ", list2)

the output::

    element list :  [123, 'Google', 'Runoob', 'Taobao']
    element list :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

.. function:: locals()

Returns all local variables in the current location as dictionary type. 

::

    >>>def runoob(arg):    # Two local variables：arg、z
    ...     z = 1
    ...     print (locals())
    ... 
    >>> runoob(4)
    {'z': 1, 'arg': 4}      # Returns a dictionary of name / value pairs
    >>>

.. function:: map(function, iterable, ...)

map() The specified sequence is mapped according to the provided function. Returns an iterator that applies a function to each item in Iterable and outputs its result.  
If an additional Iterable parameter is entered, the function must accept the same number of arguments and be applied to items obtained in parallel from all iteratable objects. 
When there are multiple iteratable objects, the whole iteration will end when the shortest one is exhausted. 

::

    >>>def square(x) :            # compute square sum 
    ...     return x ** 2
    ... 
    >>> map(square, [1,2,3,4,5])   # compute the square sum of each element list
    [1, 4, 9, 16, 25]
    >>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # use lambda anonymous function
    [1, 4, 9, 16, 25]
    
    # Two lists are provided to add the list data in the same location 
    >>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    [3, 7, 11, 15, 19]


.. function:: max()

Returns the maximum value of the given parameter, which can be a sequence 

::

    print ("max(80, 100, 1000) : ", max(80, 100, 1000))
    print ("max(-20, 100, 400) : ", max(-20, 100, 400))
    print ("max(-80, -20, -10) : ", max(-80, -20, -10))
    print ("max(0, 100, -400) : ", max(0, 100, -400))

The output::

    max(80, 100, 1000) :  1000
    max(-20, 100, 400) :  400
    max(-80, -20, -10) :  -10
    max(0, 100, -400) :  100

.. class:: memoryview()

Returns the memory view object for the given parameter. The so-called memory view object refers to packaging the data supporting the buffer protocol and allowing Python code access without copying the object.

::

    >>>v = memoryview(bytearray("abcefg"))
    >>> v[1]
    98
    >>> v[-1]
    103
    >>> v[1:4]
    <memoryview>
    >>> bytes(v[1:4)
    b'bce'
    >>>


---------------------------------------------------------

.. function:: min()

Returns the minimum value of a given parameter, which can be a sequence. 
::

    print ("min(80, 100, 1000) : ", min(80, 100, 1000))
    print ("min(-20, 100, 400) : ", min(-20, 100, 400))
    print ("min(-80, -20, -10) : ", min(-80, -20, -10))
    print ("min(0, 100, -400) : ", min(0, 100, -400))

The output::

    min(80, 100, 1000) :  80
    min(-20, 100, 400) :  -20
    min(-80, -20, -10) :  -80
    min(0, 100, -400) :  -400



.. function:: next(iterator[, default])


Returns the next entry for the iterator. Get the next element by calling the iterator's __next__(). If the iterator is exhausted, the given default is returned, and if there is no default value, StopIteration is triggered.
::

    # First, to get the iterator object:
    it = iter([1, 2, 3, 4, 5])
    # loop:
    while True:
        try:
            # Get the next value:
            x = next(it)
            print(x)
        except StopIteration:
            # Exit loop when StopIteration is encountered
            break

.. class:: object()

.. function:: oct()

Convert an integer to an octal string.

::

    >>>oct(10)
    '012'
    >>> oct(20)
    '024'
    >>> oct(15)
    '017'
    >>>

.. function:: open()

open() Method is used to open a file and return the file object. This function is required during the processing of the file. If the file cannot be opened, an oserror will be thrown.
Note：used open() Method must close the file object, that is, call the close() method.

open() The common form of a function is to receive two parameters: file name and mode::

    open(file, mode='r')

mode Is an optional string that specifies the mode of opening the file. The default value is ' r ' , which means it opens in text mode and reads. Other common modes are: write 'w' (Truncate existing files）；
Exclusive creation 'x' ；write to add 'a' （On some UNIX systems, no matter where the current file pointer is, all writes are appended to the end of the file）。Available modes are:

=========  =================================
Mode       Description
'r'        Read (default)
'w'        Write, and truncate the file first
'x'        Exclusive creation, failure if file already exists
'a'        Write, append at the end if the file exists
'b'        binary mode
't'        Text mode (default)
'+'        Update disk file (read and write)
=========  =================================

The default mode is 'r' （Open and read text, same as 'rt' ）. For binary write，Open 'w+b' mode and truncate file to 0 bytes； 'r+b' Will not be truncated。


.. function:: ord(c)

这是 chr() 的逆函数。。它以一个字符串（Unicode 字符）作为参数,返回代表对应 Unicode 的整数。

::

    >>>ord('a')
    97
    >>> ord('€')
    8364
    >>>

.. function:: pow(x, y[, z])

返回 xy（x的y次方） 的值。

::

    print ("pow(100, 2) : ", pow(100, 2))
    print ("pow(100, -2) : ", pow(100, -2))
    print ("pow(2, 4) : ", pow(2, 4))
    print ("pow(3, 0) : ", pow(3, 0))

输出结果::

    pow(100, 2) :  10000
    pow(100, -2) :  0.0001
    pow(2, 4) :  16
    pow(3, 0) :  1

.. function:: print(*objects, sep=' ', end='\n', file=sys.stdout)

用于打印输出，最常见的一个函数。

    - ``objects`` ：复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
    - ``sep`` ：用来间隔多个对象，默认值是一个空格。
    - ``end`` ：用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
    - ``file`` ：要写入的文件对象。

::

    >>> print(1)
    1
    >>> print("Hello World")
    Hello World
    >>> a = 1
    >>> b = 'w3cschool'
    >>> print(a,b)
    1 w3cschool
    >>> print("aaa""bbb")
    aaabbb
    >>> print("aaa","bbb")
    aaa bbb
    >>>
    >>> print("www","w3cschool","cn",sep=".") # 设置间隔符
    www.w3cschool.cn


.. decorator:: property()

property() 函数的作用是在新式类中返回属性值。将 `property` 函数用作装饰器可以很方便的创建只读属性：

property 的 getter，setter 和 deleter 方法同样可以用作装饰器::

    class C(object):
        def __init__(self):
            self._x = None
    
        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x
    
        @x.setter
        def x(self, value):
            self._x = value
    
        @x.deleter
        def x(self):
            del self._x


.. function:: range()

range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。

函数语法:

    - ``range(stop)``
    - ``range(start, stop[, step])``

::

    >>>range(5)
    range(0, 5)
    >>> for i in range(5):
    ...     print(i)
    ... 
    0
    1
    2
    3
    4
    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(0))
    []
    >>>

有两个参数或三个参数的情况（第二种构造方法）::

    >>>list(range(0, 30, 5))
    [0, 5, 10, 15, 20, 25]
    >>> list(range(0, 10, 2))
    [0, 2, 4, 6, 8]
    >>> list(range(0, -10, -1))
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    >>> list(range(1, 0))
    []
    >>>
    >>>


.. function:: repr()

返回包含一个对象的可打印表示形式的字符串。

::

    >>>s = 'baidu'
    >>> repr(s)
    "'baidu'"
    >>> dict = {'baidu': 'baidu.com', 'google': 'google.com'}
    >>> repr(dict)
    "{'google': 'google.com', 'baidu': 'baidu.com'}"
    >>>

.. function:: reversed(seq)

返回一个反转的迭代器。

::

    # 字符串
    seqString = 'Runoob'
    print(list(reversed(seqString)))
    
    # 元组
    seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
    print(list(reversed(seqTuple)))
    
    # range
    seqRange = range(5, 9)
    print(list(reversed(seqRange)))
    
    # 列表
    seqList = [1, 2, 4, 3, 5]
    print(list(reversed(seqList)))

输出结果::

    ['b', 'o', 'o', 'n', 'u', 'R']
    ['b', 'o', 'o', 'n', 'u', 'R']
    [8, 7, 6, 5]
    [5, 3, 4, 2, 1]


.. function:: round(x [, n])

返回浮点数x的四舍五入值。

    - ``x`` - 数字表达式。
    - ``n`` - 表示从小数点位数，其中 x 需要四舍五入，默认值为 0

::

    print ("round(70.23456) : ", round(70.23456))
    print ("round(56.659,1) : ", round(56.659,1))
    print ("round(80.264, 2) : ", round(80.264, 2))
    print ("round(100.000056, 3) : ", round(100.000056, 3))
    print ("round(-100.000056, 3) : ", round(-100.000056, 3))

输出结果::

    round(70.23456) :  70
    round(56.659,1) :  56.7
    round(80.264, 2) :  80.26
    round(100.000056, 3) :  100.0
    round(-100.000056, 3) :  -100.0

.. class:: set([iterable])

set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

    >>> x = set('runoob')
    >>> y = set('google')
    >>> x, y
    ({'b', 'u', 'n', 'o', 'r'}, {'e', 'l', 'g', 'o'})     # 重复的被删除
    >>> x & y         # 交集
    {'o'}
    >>> x | y         # 并集
    {'e', 'u', 'o', 'n', 'r', 'l', 'g', 'b'}
    >>> x - y         # 差集
    {'b', 'u', 'n', 'r'}
    >


------------------------------------------------


.. function:: setattr(object, name, value)

setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。

对已存在的属性进行赋值::

    >>>class A(object):
    ...     bar = 1
    ... 
    >>> a = A()
    >>> getattr(a, 'bar')          # 获取属性 bar 值
    1
    >>> setattr(a, 'bar', 5)       # 设置属性 bar 值
    >>> a.bar
    5

如果属性不存在会创建一个新的对象属性，并对属性赋值::

    >>>class A():
    ...     name = "runoob"
    ... 
    >>> a = A()
    >>> setattr(a, "age", 28)
    >>> print(a.age)
    28
    >>>


.. class:: slice()


.. function:: sorted(iterable, *, key=None, reverse=False)

对所有可迭代的对象进行排序操作

- ``iterable`` -- 可迭代对象。
- ``key`` -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- ``reverse`` -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

sorted 的最简单的使用方法::

    >>>sorted([5, 2, 3, 1, 4])
    [1, 2, 3, 4, 5]                      # 默认为升序

利用key进行倒序排序::

    >>>example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    >>> result_list = sorted(example_list, key=lambda x: x*-1)
    >>> print(result_list)
    [7, 6, 5, 4, 3, 2, 1, 0]
    >>>

要进行反向排序，也通过传入第三个参数 reverse=True::

    >>>example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    >>> sorted(example_list, reverse=True)
    [7, 6, 5, 4, 3, 2, 1, 0]

.. decorator:: staticmethod()

将方法转换为静态方法。

静态方法不会接收隐式的第一个参数。要声明一个静态方法，请使用此语法::

    class C:
        @staticmethod
        def f(arg1, arg2, ...): ...

静态方法的调用可以在类上进行 (例如 C.f()) 也可以在实例上进行 (例如 C().f())。


.. class:: str()

函数将对象转化为str对象。

::

    >>>s = 'w3cschool'
    >>> str(s)
    'W3Cschool'
    >>> dict = {'w3cschool': 'w3cschool', 'google': 'google.com'};
    >>> str(dict)
    "{'google': 'google.com', 'w3cschool': 'w3cschool.cn'}"
    >>>


.. function:: sum(iterable[, start])

::

    >>>sum([0,1,2])
    3
    >>> sum((2, 3, 4), 1) # 元组计算总和后再加 1
    10
    >>> sum([0,1,2,3,4], 2) # 列表计算总和后再加 2
    12


.. function:: super()

super() 函数是用于调用父类(超类)的一个方法。

::

    class A:
        def add(self, x):
            y = x+1
            print(y)
    class B(A):
        def add(self, x):
            super().add(x)
    b = B()
    b.add(2)  # 3

.. class:: tuple()

将列表转换为元组。

::

    >>>list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
    >>> tuple1=tuple(list1)
    >>> tuple1
    ('Google', 'Taobao', 'Runoob', 'Baidu')


.. function:: type()

type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。

- ``type(object)``
- ``type(name, bases, dict)``

    - ``name`` -- 类的名称。
    - ``bases`` -- 基类的元组。
    - ``dict`` -- 字典，类内定义的命名空间变量。

.. Hint:: isinstance() 与 type() 区别

    - type() 不会认为子类是一种父类类型，不考虑继承关系。
    - isinstance() 会认为子类是一种父类类型，考虑继承关系。

    **如果要判断两个类型是否相同推荐使用 isinstance()。**

::

    >>> type(1)
    <type 'int'>
    >>> type('runoob')
    <type 'str'>
    >>> type([2])
    <type 'list'>
    >>> type({0:'zero'})
    <type 'dict'>
    >>> x = 1          
    >>> type( x ) == int    # 判断类型是否相等
    True
    
    # 三个参数
    >>> class X(object):
    ...     a = 1
    ...
    >>> X = type('X', (object,), dict(a=1))  # 产生一个新的类型 X
    >>> X
    <class '__main__.X'>

type() 与 isinstance()区别::

    class A:
        pass
    s
    class B(A):
        pass
    
    isinstance(A(), A)    # returns True
    type(A()) == A        # returns True
    isinstance(B(), A)    # returns True
    type(B()) == A        # returns False


.. function:: zip([iterable, ...])

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。

我们可以使用 list() 转换来输出列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

::

    >>>a = [1,2,3]
    >>> b = [4,5,6]
    >>> c = [4,5,6,7,8]
    >>> zipped = zip(a,b)     # 返回一个对象
    >>> zipped
    <zip object at 0x103abc288>
    >>> list(zipped)  # list() 转换为列表
    [(1, 4), (2, 5), (3, 6)]
    >>> list(zip(a,c))              # 元素个数与最短的列表一致
    [(1, 4), (2, 5), (3, 6)]
    
    >>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
    >>> list(a1)
    [1, 2, 3]
    >>> list(a2)
    [4, 5, 6]
    >>>


异常
----------

.. exception:: AssertionError

.. exception:: AttributeError

.. exception:: Exception

.. exception:: ImportError

.. exception:: IndexError

.. exception:: KeyboardInterrupt

.. exception:: KeyError

.. exception:: MemoryError

.. exception:: NameError

.. exception:: NotImplementedError

.. _OSError:

.. exception:: OSError

    参见CPython文档： ``OSError`` . MicroPython不实现 ``errno``  属性，而是使用标准方式访问异常参数： ``exc.args[0]`` .

.. exception:: RuntimeError

.. exception:: StopIteration

.. exception:: SyntaxError

.. exception:: SystemExit

   参见CPython文档： ``SystemExit`` .

.. exception:: TypeError

    参见CPython文档： ``SystemExit`` .

.. exception:: ValueError

.. exception:: ZeroDivisionError
