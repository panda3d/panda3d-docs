.. _email-certificates:

Email certificates
==================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

You can also use a personal email certificate to sign your p3d files. When you
do this, and the user is shown your certificate, he/she will be told "This
application has been signed by yourname@youraddress.net," which reassures the
user of your personal identity.

An email certificate is sometimes called an S/MIME certificate, because it can
be used to send encrypted and signed email via the international S/MIME
standard.

This kind of certificate may be most appropriate for a p3d file produced by an
individual or by a small group. Signing a p3d file with your own email address
is a very personal touch.

You can obtain an email certificate from numerous sources. Many companies
charge a nominal fee for an email certificate intended for corporate use, but
some companies also offer a completely cost-free email certificate for
personal use, typically with a 1-year expiration date. (The expiration date is
a nuisance, but not a limit. You can replace it with a new certificate when it
expires.)

The process to obtain an email certificate can be a bit convoluted. Usually,
you will fill out a form at the company's website, receive an email to confirm
your email address, click on a link in the email, then download the
certificate into your browser. Once it has been installed in your browser, you
can find the certificate under the Preferences menus, and save it (as a
"backup") to a pkcs12 file on disk, with the .p12 extension. Then you can
convert it to a pem file using openssl, with the command sequence:



.. code-block:: bash

    openssl pkcs12 -in mycert.p12 -out mycert.pem -nodes



Typically, the public key and private key will be combined in the same file.
Keep this file safe.
