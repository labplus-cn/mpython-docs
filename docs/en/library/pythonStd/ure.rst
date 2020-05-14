:mod:`ure` -- Regular Expression
========================================

.. module:: ure
   :synopsis: regular exprression
   
This module implements the corresponding :term:`CPython` a subset of modules, as described below. Refers to CPython document for details: `re <https://docs.python.org/3.5/library/re.html#module-re>`_

This module implements regular expression operation. The supported regular expression syntax is a subset of CPython ``re`` module (actually a subset of POSIX extended regular expressions).

The supported operators and special sequences are:

``'.'``
   Mtach any role.

``'[]'``
   Match character set. Supports single characters and ranges, including negative sets (example ​​ ``[^a-c]`` ）.

``'^'``
   Matches the beginning of the string.

``'$'``
   Matches the end of the string.

``'?'``
   Matches one of the zero or previous sub patterns.
   
``'*'``
   Matches zero or more of the previous subpattern.

``'+'``
   Matches one or more of the previous subpatterns.

``'??'``
   Non-avaricious version?, Matches 0 or 1 and 0 preference. 

``'*?'``
   Non-avaricious version?, Match 0 or more, with the shortest match preference.

``'+?'``
   Non-avaricious version?, Match 1 or more, preferences to match the shortest.
   

``|``
   Matches the left or right sub pattern of this operator.

``(...)``
   Sub-grouping. Each group is capturing (the substrings it captures can be accessed through the `match.group()` method）. 

``\d``
   Match numbers. Amount to ``[0-9]`` 。

``\D``
   Match non numeric. Amount to ``[^0-9]`` 。

``\s``
   Match blanks. Amount to ``[ \t-\r]``

``\S``
   Match is not blank. Amount to ``[^ \t-\r]``

``\w``
   Match “word character”（ASCII only）. Amount to  ``[A-Za-z0-9_]`` 。

``\W``
   Unmatch “word character”（ASCII only）. Amount to ``[^A-Za-z0-9_]`` 。

``\``
   Escape character. Any other character following the backslash, except
   for those listed above, is taken literally. For example, ``\*`` is
   equivalent to literal ``*`` (not treated as the ``*`` operator).
   Note that ``\r``, ``\n``, etc. are not handled specially, and will be
   equivalent to literal letters ``r``, ``n``, etc. Due to this, it's
   not recommended to use raw Python strings (``r""``) for regular
   expressions. For example, ``r"\r\n"`` when used as the regular
   expression is equivalent to ``"rn"``. To match CR character followed
   by LF, use ``"\r\n"``.

   Escape role. n addition to those listed above, any other characters after the backslash are literal. Such as ，``\*`` equivalent to words ``*``（omission ``*`` operator）。
   It should be noted that there is no special treatment for ``\r`` ，``\n`` , And will be equivalent to the letters' ``r`` ，``n`` . Because of this, it is not recommended to use（the original Python string ``r""`` ）as a regular expression.
   For example, ``r"\r\n"`` when used as a regular expression is equivalent to ``"rn"`` . To match the character CR followed by LF, use ``"\r\n"`` . 

**Unsupported**:

* Count repetitions (``{m,n}``)
* Named group (``(?P<name>...)``)
* Non-capture group (``(?:...)``)
* More advanced assertions (``\b``, ``\B``)
* Escape of special characters ，such as ``\r`` ，``\n`` Using Python's own escape
* And so on

Example::

    import ure

    # As ure doesn't support escapes itself, use of r"" strings is not
    # recommended.
    regex = ure.compile("[\r\n]")

    regex.split("line1\rline2\nline3\r\n")

    # Result:
    # ['line1', 'line2', 'line3', '', '']

Function
---------

.. function:: compile(regex_str)

   Compile the regular expression and return the `regex <regex>` object.

.. function:: match(regex_str, string)

   Compile *regex_str* and match *string* . Matching always starts at the beginning of the string.
 
.. function:: search(regex_str, string)

   Compile *regex_str* and search it in a *string*. Unlike `match`, this will search
   string for first position which matches regex (which still may be
   0 if regex is anchored).

   Compile `regex_str` And search for it in a string. different from  ``match`` , The string that matches the first position of the regular expression is searched (it can still be 0 if the regular expression is anchored).

.. data:: DEBUG

   Tag values that display debugging information about compiled expressions.


