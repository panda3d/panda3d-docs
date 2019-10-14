.. _signing-your-p3d-files:

Signing your p3d files
======================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

Once you have a certificate, you can use it to sign any of your p3d files. Be
sure the certificate is in pem format; use the openssl command to convert it
to pem format first if you need to.

The easiest way to sign a p3d file is to specify the -S parameter to packp3d
at the time you generate it:

.. code-block:: bash

    packp3d -S mycert.pem -o myapp.p3d -d c:/myapp

The above is the appropriate command to use if your public key and private key
are combined in the same file. If they are separate, you can specify both
files with "-S mypublic.pem,,myprivate.pem". (Note the double comma; it is
necessary.) If you also have a certificate chain file, then you should specify
all three files: "-S mypublic.pem,mychain.pem,myprivate.pem".

It is also possible to sign a p3d file after it has been generated, with the
multify command:

.. code-block:: bash

    multify -S mycert.pem -uvf myapp.p3d
    multify -S mycert.pem,mychain.pem,myprivate.pem -uvf myapp.p3d

You can add multiple signatures to a p3d file. If the user has already
approved any of the certificates used to sign a p3d file, then that p3d file
will be considered automatically approved. If the user has approved none of
the certificates, then the first one (and only the first one) used to sign the
file will be presented to the user for approval.
