Storage
-------

Sometimes you need to store useful information. This information is stored as data: a representation of the information (in digital form when stored on a computer).
If you store data on your computer, even if you turn the device off and on again, it should. 

The MicroPython bit allows you to do this using a very simple file system. 

What is a file system?

It's a way to store and organize data in a persistent way - any data stored in the file system should continue to exist after the device restarts. 
As the name implies, data stored in the file system is organized into files.

.. image:: /../images/tutorials/files.jpg

Computer files are named digital resources stored on the file system. These resources contain useful information as data.
This is how paper documents work. It is a named container that contains useful information. Usually, both paper and digital files are named to indicate what they contain。
On a computer, the file ends with the suffix  ``.xxx`` . Generally, it indicates what type of data is used to represent information.
For example, ``.txt`` means a text file, `` .jpg`` JPEG image and  ``.mp3`` sound data encoded as MP3.

Some file systems (such as those on laptops or PCs) allow you to organize files into directories：Named containers combine related files and subdirectories.
However, the file system provided by MicroPython is a flat file system. Flat file systems have no directories - all files are only stored in the same place.

The Python programming language contains an easy-to-use and powerful way to use the computer's file system. MicroPython on mPython implements a useful subset of these functions, Make it easy to read and write files on the device, while also providing consistency with other Python versions.


Open a file
+++++++++++

The following are the relevant instructions for Python File operation.

open() method::

    #open(Path + file name, read-write mode) ，like f=open('/tmp/hello','w')
    #Read-write mode:r read only，r+ read-write，w new (will overwrite the original file), a append, b binary file. Such as:'rb','wb','r+b', etc
    The types of read and write modes are：
    rU or Ua opens in read mode, and provides universal newline support (PEP 278)
    w     Open in write mode，
    a     Open in append mode (starting with EOF, creating new files if necessary)
    r+     Open in read-write mode
    w+     Open in read-write mode (see w )
    a+     Open in read-write mode (see a )
    rb     Open in binary read mode
    wb     Open in binary write mode (see w )
    ab     Open in binary append mode (see a )
    rb+    Open in binary read-write mode (see r+ )
    wb+    Open in binary read-write mode (see w+ )
    ab+    Open in binary read-write mode (see a+ )

The file object is created using the open function. The following table lists commonly used functions of the file object::

    file.read([size]) # size if not specified, the entire file is returned, There is a problem if the file size is> 2 times the memory. f.read() return "" (empty string) when reading to the end of the file.
    file.readline() # return a row
    file.readline([size]) #size Return all rows if not specified
    for line in f: print line #access via iterator
    file.write("hello\n") #If you want to write data other than a string, first convert it to a string.
    file.tell() #Returns an integer representing the position of the current file pointer (that is, the number of bytes to the file header).
    file.seek(offset, [start point])  #用To move the file pointer, offset: unit: byte, can be positive or negative, starting position: 0 - file header, default value; 1 - current position; 2 - end of file.
    file.close() #close file



Details for use of open(), refers to :term:`CPython` document:`open() <https://docs.python.org/3.5/library/functions.html#open>`_。

----------------------------------------------------------

Open the ``open``  function to read and write files on the file system. After opening the file, you can use it until you close it (similar to how we use paper files). 

The best way to ensure this is to use the following with statement::

    with open('story.txt') as my_file:
        content = my_file.read()
    print(content)

The ``with`` statement uses the ``open``  function to open the file and assign it to the object. In the above example, the ``open`` function opens the called file ``story.txt`` (apparently a text file containing a story.
Call the object ``my_file`` used to represent the file in the Python code。
Then, in the indented code block below the  ``with`` statement, the ``my_file`` object is used for the content of the ``read()`` file and assigns it to the ``content`` object.

This is an important point, the next line containing the ``print`` statement is not indented. The code block associated with the ``with`` statement is just a single line of reading the file.
Once the code block associated with the ``with`` statement is closed, Python (and MicroPython) will automatically close the file for you.
This is called context processing, and the object created by the ``open`` function is the file's context handler.

In short, the scope of interaction with the file is defined by the code block associated with he statement with the file opened.

Confused？

Don't. I just said your code should look like this::

    with open('some_file') as some_object:
        # Read and write files in this code block

    # When the block is complete, then use MicroPython
    # File closed automatically.

Just like paper files, there are two reasons to open files：Read its content (as shown above) or write content to a file。
The default mode is to read files. If you want to write to a file, you need to ``open`` to tell the function as follows
::

    with open('hello.txt', 'w') as my_file:
        my_file.write("Hello, World!")

Note, the ``'w'`` parameter is used to set the ``my_file`` object to write mode.
You can also transmit a  ``'r'`` parameter to set the file object to read mode, but since this is the default setting, it is usually kept.

Writing data to a file is done through (you guessed it) the ``write`` method, which takes the string you want to write to the file as a parameter.
In the above example, I wrote the text “Hello，World！” Into a file named “hello.txt” .


.. note::

    * When you open a file and write (maybe multiple times while the file is open), if the file already exists, you will write the file content.
    * If you want to append data to a file, you should first read it, store the content somewhere, close it, append the data to the content, and then open it to write again with the modified content。
   


OS 
++++++

In addition to reading and writing files, Python can also manipulate them. Of course you need to know the files in the file system, sometimes you may also need to delete them.

On regular computers, the role of the operating system (such as Windows, OSX or Linux) is to manage it on behalf of Python.
Python provides such a function through a module called OS.
Since MicroPython is the operating system, we decided to maintain proper functionality in the OS module to maintain consistency, so that when you use “regular” Python on devices such as laptops or Raspberry Pi, you will know where to find them.

Basically, you can perform three operations related to the file system：List files, delete files and enquiry for file size。

To list files on the file system, use the listdir function. It returns a list of strings indicating the file name of the file on the file system::

    import os
    my_files = os.listdir()

To delete files, use the remove function. It needs a string to represent the file name of the file to be deleted as a parameter, as shown below::

    import os
    os.remove('filename.txt')

os commonly used method::

    os.chdir(path)          #Modify the path
    os.getcwd()             #Get current path
    os.listdir(dir)         #Directory listing
    os.mkdir(dir)           #Create a directory
    os.remove(path)         #Delete Files
    os.rmdir(dir)           #Delete directory
    os.rename(old_path, new_path)   #File rename
    os.stat(path)           #File / directory status, explained below：


For more OS module application，see :mod:`os` module chapter.


Main program main.py
++++++++++++++

boot.py and main.py, these two files are specially processed by MicroPython at startup. First execute the boot.py script (if it exists), and then execute the main.py script.

In addition, if you copy other Python files to the file system, then import is like any other Python module.
For example, if you have a  ``hello.py``  file containing the following simple code::

    def say_hello(name="World"):
        return "Hello, {}!".format(name)

You can import and use such ``say_hello`` function::

    from mpython import *
    from hello import say_hello

    oled.DispChar(say_hello(),0,0)
    oled.show()

.. note::

    If a script has been swiped on the device in addition to the MicroPython runtime, then MicroPython will ignore main.py and run your embedded script.

    To refresh only the MicroPython runtime, just make sure that the script you write in the editor contains zero characters. Once flashed, you can copy the main.py file.

.. footer:: The image of paper files is used under a Creative Commons License and is available here: https://www.flickr.com/photos/jenkim/2270085025
