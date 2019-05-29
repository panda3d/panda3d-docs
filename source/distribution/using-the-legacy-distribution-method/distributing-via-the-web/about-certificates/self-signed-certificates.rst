.. _self-signed-certificates:

Self-signed certificates
========================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

The self-signed certificate is the simplest kind of certificate to acquire,
since it doesn't require working with any certificate agencies. You can
generate a self-signed certificate on your own, and you can use it to sign
your p3d files.

A self-signed certificate is not as good as an authenticated certificate,
though, because there's no one to certify that you really are who you claim to
be. The user has to take your word for it. If you use a self-signed
certificate to sign your p3d file, the user will be presented with a warning,
and will have to go through an additional step to approve your certificate. We
recommend you use a self-signed certificate only for internal development, but
get a normal authenticated certificate when you're ready to make your app
available to the public.

You can use the openssl command to generate a self-signed certificate. You
probably already have openssl installed if you're running on Linux or Mac; if
you're on Windows, you can find it on the internet easily.

A sample command sequence to generate a self-signed certificate follows:



.. code-block:: bash

    openssl genrsa 1024 > mycert.pem
    openssl req -new -x509 -nodes -sha1 -days 365 -key mycert.pem >> mycert.pem


