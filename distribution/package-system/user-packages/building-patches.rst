.. _building-patches:

Building patches
================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

One of the key advantages to Panda's package system is that any updates you
make to a package are automatically downloaded and installed by users. You
don't need to do anything special for this to work: simply rebuild a new
package using the ppackage tool with the latest contents, using the -i
parameter to point ppackage to your existing install directory. This will
generate new package data and update the contents.xml file accordingly. When
you then copy this install directory to your webserver host, p3d files that
reference your package will automatically download and install the new
contents for that package before they start to run.

This will mean all of your users will have to redownload the entire package
file, which may be a large download. As a convenience to your users (and to
relieve bandwidth burden on your servers), you may wish to provide patches
instead. This works on the assumption that most of the package contents are
not changing from one release to the next, and it allows your users who
already have the previous version of a package to download only the changes
necessary between the previous version and the current version, which is often
a much smaller download and will save considerable time and bandwidth.

To enable this, you simply run
``ppatcher -i /my/install/dir``, where /my/install/dir
is your install directory that you have already populated with ppackage.

The first time you run ppatcher on a particular install directory, it prepares
that directory for future patches, and declares the current revision number
"rev 1". You may then use ppackage to build new versions of the packages in
that install directory.

The second and later times you run ppatcher, it builds patches from the
last-patched version to the current version now visible in the install
directory. Each time you run ppatcher, any packages in the install directory
with changes since the last ppatcher will be patched and the current revision
number will be incremented.

Thus, you should run ppatcher each time you are ready to make a formal release
of your modified code. This will allow the users to download the minimal
patches necessary to receive the latest code.

You may release intermediate versions for testing purposes without running
ppatcher. If you do, users who visit your servers will have to download the
entire file again, even if they already have a previous version installed.
This way, these users can test your changes and report success or failure; you
can continue to make new releases without running ppatcher and allow your
users to continue to test them. Then, when you are satisfied that the release
is ready for the world, you can run ppatcher to formalize it.

We don't recommend running ppatcher for each intermediate release, because
each time you run ppatcher, a new patch file is added to the version chain.
This patch file will then forever be a part of the version chain (until it is
eventually aged out). Users who have an older version of the package will have
to download and apply all patch files in the chain in order to update to the
latest version. If there are many intermediate patch files in the chain, this
process will be slower and involve more bandwidth than if there are only a few
patch files.
