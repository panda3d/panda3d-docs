.. _public-key-private-key:

Public key, private key
=======================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

A certificate has two components: the public key, which is copied into each
p3d file you sign and is visible to everyone; and the private key, which you
must keep secret and safe. If anyone gains access to your private key, they
can use it to sign p3d files in your name, which means that users could
legitimately blame you for installing a virus on their computer!

Depending on the source that provided your certificate, you may have the
public key and private key saved in two separate files, or they may be
combined into the same file. Whichever way you store them, you must keep the
private key safe; it's best to keep it encrypted with a password, and decrypt
it only when you use it.
