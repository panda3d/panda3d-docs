.. _ssl-hosting:

SSL hosting
===========

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

As stated previously, the Panda3D plugin system first downloads the
contents.xml from the root of your host URL, and uses this file to validate
all of the other files that must be downloaded for a particular package. This
ensures that the files downloaded are precisely the same files that you
uploaded--as long as that initial contents.xml file is downloaded correctly.

It is theoretically possible, through DNS spoofing, for a hacker to substitute
a compromised contents.xml file that allows compromised packages to be
inadvertently downloaded to a user's machine. Though this is unlikely, this
can be protected against by hosting the contents.xml file on a secure domain,
with an https address. The https protocol protects against DNS spoofing by
ensuring that only the named host is actually contacted.

Using this feature is completely optional, but it does provide a bit more
security against hackers. By convention, if you specify your host URL with an
https address, like this:

.. code-block:: python

   packager.setHost('https://example.com/myrootdir/')

then Panda3D will understand that the contents.xml file should be downloaded via
the https protocol. However, the remaining files will be downloaded via ordinary
http protocol, from the same address, e.g. http://example.com/myrootdir/ . This
avoids the overhead of https on every download, and also allows downloading from
mirror hosts to distribute the download burden. If your cleartext http address
it not the same as the https address, you can specify the specific address with
the downloadUrl parameter, e.g.:

.. code-block:: python

   packager.setHost('https://example.com/myrootdir/',
                    downloadUrl = 'http://example.com:8080/myrootdir/')

The first URL is the host URL, and is the address from which contents.xml will
be downloaded, and is also the URL that should be specified when downloading
the package later. The second URL is the "download URL", and is the address
from which all of the other data, after contents.xml, will be downloaded.
