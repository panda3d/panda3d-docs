.. _about-certificates:

About certificates
==================

.. warning::

   This section describes a deprecated feature as of Panda3D 1.10.0.

When a p3d file is embedded in a web page, it can potentially start running as
soon as a user visits the web page. This can be a big security problem for the
user, if a malicious person installs malware in a p3d file. There needs to be
a way for the user to prevent p3d files from running without his or her
approval.

To solve this problem, Panda3D uses a certificate signing approach. Before you
can put a p3d file on a web page, you must sign it with a special certificate
that identifies you and only you. When the user visits your web page, and sees
your signed p3d file, he or she will be shown your certificate, and given an
opportunity to approve it.

Once the user approves your certificate, the application will be allowed to
run. (And this application, and all other applications signed by the same
certificate, will also run automatically in the future without further
approval.)


.. toctree::
   :maxdepth: 2

   public-key-private-key
   self-signed-certificates
   https-apache-certificates
   email-certificates
