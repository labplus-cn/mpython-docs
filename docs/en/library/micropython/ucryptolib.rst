:mod:`ucryptolib` -- Encrypted password
==========================================

.. module:: ucryptolib
   :synopsis: Encrypted password

Class
-------

.. class:: aes

    .. classmethod:: __init__(key, mode, [IV])

        Initialize password object, suitable for encryption / decryption. Note: After initialization, the password object can only be used for encryption or decryption. Does not support running decrypt() after encrypt().

        Parameter:

            * ``key`` Encryption / decryption key (similar to bytes)
            * ``mode`` :

                * ``1`` (Or ``ucryptolib.MODE_ECB`` if present）Electronic Code Book(ECB)
                * ``2`` (ucryptolib.MODE_CBC if present）
                * ``6`` (Or ucryptolib.MODE_CTR if present) (CTR)

            * ``IV`` CBC mode initialization vector
            * For counter mode, IV is the initial value of the counter

    .. method:: encrypt(in_buf, [out_buf])

        encrypt in_buf. If out_buf is not given, return the result as a newly allocated bytes object.
       Otherwise, the result is written to the variable buffer out_buf. in_buf and out_buf can also refer to the same variable buffer, in this case, the data is encrypted in place.

    .. method:: decrypt(in_buf, [out_buf])

        Similar to `encrypt()` , but for decryption.
