Accelerometer
======================================

The acceleration sensor can measure the acceleration due to gravity. During the acceleration process, the sensor uses the Newton's second law to obtain the acceleration value by measuring the inertial force received by the mass. The accelerometer on the mPython Board can measure acceleration, with a measurement range of -2g to + 2g.。

It is 3-axis measurement of the mPython Board with positive or negative values on each axis. As the positive axis approaches the direction of gravitational acceleration, its value increases toward the positive direction, and conversely decreases toward the negative direction. 

* X - Tilt forward and backward.
* Y - Tilt left and right。
* Z - Flip up and down。

.. image:: /../images/tutorials/xyz.png
    :align: center


Example：Observe the changes of the acceleration values of the three axes through the OLED display
::
    from mpython import *
    
    while True:
        oled.fill(0)     
        x1 = accelerometer.get_x()
        y1 = accelerometer.get_y()
        z1 = accelerometer.get_z()
        oled.DispChar("Acceleration x:", 0, 0)
        oled.DispChar(str(x1), 48, 0)
        oled.DispChar("Acceleration y:", 0, 16)
        oled.DispChar(str(y1), 48, 16)
        oled.DispChar("Acceleration z:", 0, 32)
        oled.DispChar(str(z1), 48, 32)
        oled.show()


First, import the mPython module::

    from mpython import *

Obtain X、Y、Z 3-axis acceleration::

    x1 = accelerometer.get_x()
    y1 = accelerometer.get_y()
    z1 = accelerometer.get_z()

.. Note::

    Obtain the 3 axis acceleration by  accelerometer.get_x() . The methods to get the 3-axis acceleration are ``get_x()`` 、``get_y()`` 、``get_z()`` 。
    The measured value of each axis is positive or negative according to the direction, indicating the value in grams。

You can try to place the mPython Board panel as follows and observe the 3-axis data:

* Flat on the surface top       --(0,0,-1)
* Flip the flat surface top   --(0,0,1)
* The bottom edge of the control board is upright --(1,0,0) 
* The left side of the control panel is upright --(0,1,0) 

.. Note::

    Did you find any patterns? When the acceleration of gravity is consistent with the direction of the acceleration axis, it is equal to the acceleration of gravity of 1g. Positive direction is + 1g, negative direction is -1g. 
    If you shake the control panel violently, you will see the acceleration reach ± 2g, which is because the maximum measurement value of this accelerometer is ± 2g.


Horizontal ball
++++++++++++++


.. literalinclude:: /../../examples/accelerometer/gradienter.py
    :caption: We use the accelerometer to make a horizontal ball that rolls up, down, left, and right
    :linenos:

.. image:: /../images/tutorials/gravity.gif
    :align: center
    :scale: 100 %
   

When it is detected that the control panel is tilted in the X-axis and Y-axis directions (range -1g to + 1g), the X-axis and Y-axis offset values, that is, acceleration values (range -1 to 1), are mapped to set The center point is the Y coordinate (range 32 to -32) and the X coordinate (range -64 to 64) on the X coordinate of the origin::

    if y<=1 and y>=-1:
        offsetX=int(numberMap(y,1,-1,-64,64))
    if x<=1 and x>=-1:
        offsetY=int(numberMap(x,1,-1,32,-32))

.. Note::

    numberMap(inputNum, bMin, bMax, cMin, cMax) is the mapping function, ``inputNum`` is the variable to be mapped, ``bMin`` is the minimum value that needs to be mapped, ``bMax`` is the maximum value that needs to be mapped, ``cMin`` as the minimum value of the mapped, ``cMax`` as the maximum value of the mapped.

The movement of the horizontal ball on the X and Y coordinates: the movement of the horizontal ball on the coordinates = the position of the center point + the offset value of the acceleration::

    move_x=Center_x+offsetX
    move_y=Center_y+offsetY 

If the horizontal ball moves to the center position, green light on, otherwise not lighted::

    if offsetX==0 and offsetY==0:
        rgb.fill((0,10,0))          #The horizontal ball lights green at the center, with a brightness of 10
        rgb.write()
    else:
        rgb.fill((0,0,0))           #The horizontal ball is not in the center position, and the green light not lighted
        rgb.write()



Calculate the tilt angle of the mPython Board
++++++++++++++++++++++++++++

.. literalinclude:: /../../examples/accelerometer/degrees.py
    :caption: By measuring the acceleration due to gravity, the tilt angle of the device relative to the horizontal plane can be calculated
    :linenos:


First, import the mPython module and ACOS function and Degrees function in the math module::

    from mpython import *
    from math import acos,degrees
  
Obtain the X axis acceleration::

    x = accelerometer.get_x()

Assuming that the reference plane of the mPython Board is the table top, during the tilting, the Y axis is parallel to the table top , and its angle is unchanged (always 0 degrees). What changes are the angle between the X axis and the desktop and the Z axis and the desktop. Angle, and the degree of change of the angle between the desktop and the X axis and Z axis is the same. In order to facilitate the analysis, we look down from the direction of the Y axis, then this problem will be simplified to only the two-dimensional relationship between the X axis and the Z axis. Suppose the control board is in the following state at a certain moment：

.. image:: /../images/tutorials/xgraph.png
    :align: center


In this figure, the Y axis has been simplified to coincide with the origin O of the coordinate system. Let's take a look at how to calculate the tilt angle of the control panel, which is the angle a with the desktop. g is the acceleration of gravity, gx and gz are the components of g in the X axis and Z axis respectively. 

|   Since the acceleration of gravity is perpendicular to the horizontal plane, we get：
|   Angle a + angle b = 90 degrees
|   The X-axis and Y-axis are perpendicular to each other.：
|   Angle c + angle b = 90 degrees
|   Therefore：
|   angle a = angle c

According to the arc cosine theorem, calculate the radian value of angle b::

    rad_x=acos(x)

Calculate the angle of the included angle, ie angle a = angle c = 90 degrees-angle b::

    deg_x=90-degrees(rad_x)

.. Note::

    * acos() the function returns the arc cosine radian value. 
    * degrees() the function is to convert radians to degrees.
