:mod:`math` -- Mathematical operation function
=====================================

.. module:: math
   :synopsis: mathematical functions

This module implements the corresponding :term:`CPython` A subset of modules, as described below. See CPython Document for details:`math <https://docs.python.org/3.5/library/math.html#module-math>`_.

This ``math`` module provides some basic mathematical functions for dealing with float numbers. 
*Note:* at pyboard，Float numbers have 32-bit accuracy. 


Functions
---------

.. function:: acos(x)

   returns arccosine value ``x``.

.. function:: acosh(x)

   returns inverse hyperbolic cosine value ``x``.

.. function:: asin(x)

   R arcsine returned ``x``.

.. function:: asinh(x)

   inverse hyperbolic sine returned ``x``.

.. function:: atan(x)

   returns inverse tangent ``x``.

.. function:: atan2(y, x)

   returns main value of arctangent ``y/x``.

.. function:: atanh(x)

   returns inverse hyperbolic tangent ``x``.

.. function:: ceil(x)

   returns an integer， ``x`` Round to positive infinity.
   

.. function:: copysign(x, y)

   return ``x`` to the symbol of ``y`` .

.. function:: cos(x)

   returns cosine ``x``.

.. function:: cosh(x)

   returns hyperbolic cosine value ``x``.

.. function:: degrees(x)

   returns radian ``x`` convert to degrees. 

.. function:: erf(x)

   returns error function ``x``

.. function:: erfc(x)

   returns complementary error function  ``x``.

.. function:: exp(x)

   returns exponent ``x``.

.. function:: expm1(x)

   returns ``exp(x) - 1``.

.. function:: fabs(x)

   returns absolute value ``x``.

.. function:: floor(x)

   Returns an integer， ``x`` Round to negative infinity.

.. function:: fmod(x, y)

   Returned to the rest ``x/y``.

.. function:: frexp(x)

The float number is disintegrate into mantissa and exponent. 将浮点数分解为尾数和指数。The returned value is tuple返回的值是元组 ``(m, e)`` as such ``x == m * 2**e`` 
absolutely right. If ``x == 0`` ，then the function returns ``(0.0,0)`` ，if not ``0.5 <= abs(m) < 1`` .

.. function:: gamma(x)

   returns Gamma function ``x``.

.. function:: isfinite(x)

    In case ``x`` is limited, then return ``True``.

.. function:: isinf(x)

   In case ``x`` is unlimited, then return ``True``.

.. function:: isnan(x)

    In case ``x`` not digital, then return ``True``.

.. function:: ldexp(x, exp)

   returns ``x * (2**exp)``.

.. function:: lgamma(x)

   returns the natural logarithm of gamma function ``x``.

.. function:: log(x)

   returns the natural logarithm ``x``.

.. function:: log10(x)

  returns the logarithm of base 10 ``x``.

.. function:: log2(x)

  returns the logarithm of base 2 ``x``.

.. function:: modf(x)

   returns a tuple of two float numbers, it's a fraction of a number and an integral part of it `` x`` . Both return values have the same symbol ``x`` .

.. function:: pow(x, y)

   returns  ``y`` the power of ``x `` .

.. function:: radians(x)

   returns ``x`` convert degrees to radians. 

.. function:: sin(x)

   returns sine ``x``.

.. function:: sinh(x)

  returns hyperbola sine ``x``.

.. function:: sqrt(x)

  returns square root  ``x``.

.. function:: tan(x)

   returns tangent value ``x``.

.. function:: tanh(x)

   returns hyperbolic tangent ``x``.

.. function:: trunc(x)

  returns an integer, ``x`` round to 0. 

Constants
---------

.. data:: e

  tThe base of natural logarithm

.. data:: pi

   Ratio of circumference to diameter
