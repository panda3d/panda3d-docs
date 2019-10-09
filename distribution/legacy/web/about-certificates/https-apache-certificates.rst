.. _https-apache-certificates:

HTTPS (Apache) certificates
===========================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

If you already have an SSL-protected website with its own https address, then
you can use that website's certificate to sign your p3d files. When the user
is shown your certificate, he/she will be told something like "This
application has been signed by myhost.mydomain.net," where myhost.mydomain.net
is your website's hostname. If the user knows your web page, then this will
reassure the user that it is safe to allow your p3d app to run.

This kind of certificate may be most appropriate for a corporate or commercial
p3d file; the user may closely identify the company's web address with the
company itself.

Panda3D requires your certificate to be formatted in PEM form, which is the
same format used by Apache. If you are using Apache to host your website, then
you can use the public key and private key certificate files directly from
your system install directory. (There may also be a third file, that lists the
certificate's authentication chain. If so, all three files are needed to sign
your p3d file.) If you are using IIS or some other software to host your
website, then you may need to convert your certificate to PEM form first; you
can use the openssl command to do this. Search the internet for the exact
command sequence.

You can obtain an HTTPS certificate from numerous sources; they range in price
considerably, and many are quite inexpensive. Several companies offer a
completely cost-free HTTPS certificate, but these usually come with a very
short expiration date (90 days or so).
