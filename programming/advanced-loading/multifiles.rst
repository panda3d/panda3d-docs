.. _multifiles:

Multifiles
==========

A *multifile* is a file that contains a set of files, similar to a .zip or .rar
archive file.  They are meant for containing multiple resources such as models,
textures, sounds, shaders, and so on, and Panda can load them directly from the
multifiles without having to unpack them first. Many games employ a similar
concept of "data" file such as .upk for Unreal Engine and .pak for Quake Engine.

The multify program
-------------------

The multify console program creates such files. You can get information about
the commandline parameters by running multify with the ``-h`` option. This is
how program describes itself::

   Usage: multify -[c|r|u|t|x] -f <multifile_name> [options] <subfile_name> ...

multify is used to store and extract files from a Panda Multifile. This is
similar to a tar or zip file in that it is an archive file that contains a
number of subfiles that may later be extracted.

Panda's VirtualFileSystem is capable of mounting Multifiles for direct access to
the subfiles contained within without having to extract them out to independent
files first.

The command-line options for multify are designed to be similar to those for
tar, the traditional Unix archiver utility.

Read Assets
-----------

If you want to prepare to read assets from a Multifile directly, you can
"mount" it into the virtual file system:

.. only:: python

   .. code-block:: python

      from panda3d.core import VirtualFileSystem
      from panda3d.core import Multifile
      from panda3d.core import Filename
      vfs = VirtualFileSystem.getGlobalPtr()
      vfs.mount(Filename("foo.mf"), ".", VirtualFileSystem.MFReadOnly)

.. only:: cpp

   .. code-block:: cpp

      VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
      vfs->mount("./foo.mf", ".", VirtualFileSystem::MF_read_only);

If you want to read assets, you can mount a whole directory structure from a
webserver.

If your webserver hosts::

   http://localhost/mydir/models/myfile.bam
   http://localhost/mydir/maps/mytexture.png


Put this in your config.prc::

   vfs-mount-url http://myserver/mydir /mydir
   model-path /mydir

Or, equivalently, write this code at startup:

.. only:: python

   .. code-block:: python

      vfs.mount(VirtualFileMountHTTP('http://myserver/mydir'), '/mydir', 0)
      getModelPath().appendDirectory('/mydir')

.. only:: cpp

   .. code-block:: cpp

      VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
      vfs->mount(new VirtualFileMountHTTP("http://myserver/mydir"), "/mydir", 0);
      get_model_path().append_directory("/mydir");

.. only:: python

   and then you can load models like this in your Python code:

   .. code-block:: python

      model = loader.loadModel('models/myfile.bam')
      texture = loader.loadTexture('maps/mytexture.png')

If you want to prepare for reading and writing assets to a Multifile do the
following.

.. only:: python

   .. code-block:: python

      from panda3d.core import VirtualFileSystem
      from panda3d.core import Multifile
      from panda3d.core import Filename

      mf = Multifile()
      mf.openReadWrite("models.mf")

      vfs = VirtualFileSystem.getGlobalPtr()
      if vfs.mount(mf, ".", VirtualFileSystem.MFReadOnly):
          print('mounted')

.. only:: cpp

   .. code-block:: cpp

      PT(Multifile) mf = new Multifile;
      mf->open_read_write("models.mf");

      VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
      if (vfs->mount(mf, ".", VirtualFileSystem::MF_read_only) {
          std::cerr << "mounted\n";
      }

If you want to prepare for reading and writing assets to a 'subdirectory'
Multifile do the following. Note "mysys" must always be literally written in
any python code. E.g. "mysys/memfdir/mfbar2.txt"

.. only:: python

   .. code-block:: python

      from panda3d.core import VirtualFileSystem
      from panda3d.core import Multifile
      from panda3d.core import Filename

      mf = Multifile()
      mf.openReadWrite("models.mf")

      vfs = VirtualFileSystem.getGlobalPtr()
      if vfs.mount(mf, "mysys", VirtualFileSystem.MFReadOnly):
          print('mounted')

.. only:: cpp

   .. code-block:: cpp

      PT(Multifile) mf = new Multifile;
      mf->open_read_write("models.mf");

      VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
      if (vfs->mount(mf, "mysys", VirtualFileSystem::MF_read_only) {
          std::cerr << "mounted\n";
      }

If you are having problems loading from multifiles you can list the complete
contents of your .mf file with a command like::

   multify -tvf mymultifile.mf

Doing a sanity inspection like this can be useful to ensure that your assets are
in the right place within the multifile.

Multifile objects
-----------------

The :class:`~panda3d.core.Multifile` class is designed for opening, reading and
writing multifiles. You can open a new multifile by creating an instance of the
class and calling the :meth:`~.Multifile.open_read()` method:

.. only:: python

   .. code-block:: python

      from panda3d.core import Multifile

      mf = Multifile()
      mf.openRead("foo.mf")

.. only:: cpp

   .. code-block:: cpp

      PT(Multifile) mf = new Multifile;
      mf->open_read("foo.mf");

The :meth:`~.Multifile.open_read()` method opens the multifile as read-only.
If you want to make changes to it and write it back to disk, you will need to
use the :meth:`~.Multifile.open_read_write()` method.
Also, there exists :meth:`~.Multifile.open_write()` to create a new multifile.

If you have made important structural changes to a Multifile, it is recommended
to rewrite the multifile using the :meth:`~.Multifile.repack()` method.
(This won't work if you've opened it using :meth:`~.Multifile.open_read()`.)
If you are uncertain about whether it has become suboptimal, you can call
:meth:`~.Multifile.neesd_repack()` which returns True if the Multifile is
suboptimal and should be repacked.

To write it back to disk, you can use the :meth:`~.Multifile.flush()` method
which flushes the changes you've made to the multifile back to disk, or the
:meth:`~.Multifile.close()` method if you're done with the file.

To mount Multifile objects into the VirtualFileSystem without writing them to
disk first, here's an example on how to mount them:

.. only:: python

   .. code-block:: python

      mf = Multifile()
      #... now do something with mf

      vfs = VirtualFileSystem.getGlobalPtr()
      vfs.mount(mf, ".", VirtualFileSystem.MFReadOnly)

.. only:: cpp

   .. code-block:: cpp

      PT(Multifile) mf = new Multifile;
      //... now do something with mf

      VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
      vfs->mount(mf, ".", VirtualFileSystem::MF_read_only);

Subfiles
--------

Files that are added to a multifile are called subfiles. You can add existing
files to a multifile object using the :meth:`~.Multifile.add_subfile()` method.
This method takes three arguments: the target filename, the existing source file
and the compression level (1-9).
There is also :meth:`~.Multifile.update_subfile()`, which does the same thing
but if the file already exists, only updates it if the content is different.

There are several other methods which operate on subfiles, which you can find on
the :class:`~panda3d.core.Multifile` page in the API Reference.
Here are a few examples of working with subfiles:

.. only:: python

   .. code-block:: python

      from panda3d.core import VirtualFileSystem
      from panda3d.core import Multifile
      from panda3d.core import Filename

      m = Multifile()

      # Add an existing real os file with compression level 6
      m.openReadWrite("foo.mf")
      m.addSubfile("bar.txt", Filename("/tmp/bar.txt"), 6)
      m.flush()

      # Destroy the contents of the multifile
      # Add an existing real os file to be the first multifile
      m.openWrite("foo.mf")
      m.addSubfile("bar.txt", Filename("/tmp/bar.txt"), 6)
      m.flush()

      # Permanently re-order in ascending order the
      # directories and files in the multifile
      m.openReadWrite("foo.mf")
      m.repack()
      m.flush()

      # Open a multifile and replace the contents of the mulifile file
      # with new contents
      m = Multifile()
      m.openReadWrite("foo.mf")
      m.updateSubfile("bar.txt", Filename("/tmp/bar2.txt"), 9)
      m.flush()

      # Open a multifile and extract all files smaller than 3kb
      # New real os files are created with the contents of the multifile data
      m = Multifile()
      m.openRead("foo.mf")
      for i in range(m.getNumSubfiles()):
          if m.getSubfileLength(i) < 3 * 1024:
              m.extractSubfile(i, Filename("/tmp/" + m.getSubfileName(i)))

      # Find, print and remove a file named bar.txt
      barIdx = m.findSubfile("bar.txt")
      if barIdx != -1:
          # It returns -1 if it doesn't exist
          print(m.readSubfile(barIdx))
          m.removeSubfile(barIdx)
      m.flush()

      m.close()

.. only:: cpp

   .. code-block:: cpp

      std::ostringstream os (std::ios::in | std::ios::out);
      std::istream is (os.rdbuf ());

      os.write((char*)&stuff, sizeof(stuff));

      PT(Multifile) mf = new Multifile();
      mf->open_write(fileName);
      mf->add_subfile("foo.mf", &is,6);
      mf->flush();
      mf->close();

If the foo.mf file were to have a contained bar.egg.pz file, load the egg and
use it similar to other model loading methods.

.. only:: python

   .. code-block:: python

      nodepath = loader.loadModel("foo/bar")

Stream-Based
------------

Multifile algorithms are stream-based and not random-based. In a running game,
from the output, if a message is received saying something similar to the words
``seek error for offset`` then a file in the multifile is trying to be accessed
by a random-based method. For multifiles and fonts, an example of a random-based
file is an .rgb file. An alternative different from the use of an .rgb file is
the use of a .ttf instead. An example follows.

::

   # models is the original directory
   # models.mf it the new target multifile
   multify -c -f models.mf -v models

In the game, from the multifile models.mf, load the .ttf file.

.. only:: python

   .. code-block:: python

      font = loader.loadFont("models/arial.ttf")

.. only:: cpp

   .. code-block:: cpp

      PT(TextFont) font = FontPool::load_font("models/arial.ttf");

Encryption
----------

Multifiles can also encrypt your files with a password.
To do so, you need to set the encryption flag and password using the
:meth:`~.Multifile.set_encryption_flag()` and
:meth:`~.Multifile.set_encryption_password()` methods, before adding, extracting
or reading multifiles.

At the OS prompt, to create a password protected multifile and print out the
contents do the following.

::

   # models is the original directory
   # models.mf it the new target multifile
   multify -c -f models.mf -ep "mypass" -v models


This code creates a multifile and adds an encrypted file to it:

.. only:: python

   .. code-block:: python

      m = Multifile()
      m.openReadWrite("foo.mf")
      m.setEncryptionFlag(True)
      m.setEncryptionPassword("foobar")

      # Add a new file to the multifile
      m.addSubfile("bar.txt", Filename("/tmp/bar.txt"), 1)
      m.flush()
      m.close()

.. only:: cpp

   .. code-block:: cpp

      PT(Multifile) m = new Multifile;
      m->open_read_write("foo.mf");
      m->set_encryption_flag(true);
      m->set_encryption_password("foobar");

      // Add a new file to the multifile
      m->add_subfile("bar.txt", Filename("/tmp/bar.txt"), 1);
      m->flush();
      m->close();

You can read encrypted multifiles the same way:

.. only:: python

   .. code-block:: python

      m = Multifile()
      m.openRead("foo.mf")
      m.setEncryptionFlag(True)
      m.setEncryptionPassword("foobar")
      # Prints the contents of the multifile
      print(m.readSubfile("bar.txt"))

.. only:: cpp

   .. code-block:: cpp

      PT(Multifile) m = new Multifile;
      m->open_read("foo.mf");
      m->set_encryption_flag(True);
      m->set_encryption_password("foobar");
      // Prints the contents of the multifile
      std::cout << m->read_subfile("bar.txt");

At the OS prompt, to see the contents of a password protected multifile perform
``multify -tvf models.mf -p "mypass"``

You can test the reading in a of password-protected multifile, followed by the
mounting of the file using the following code.

.. only:: python

   .. code-block:: python

      from panda3d.core import Multifile
      mf = Multifile()
      mf.openRead("models.mf")
      mf.setEncryptionFlag(True)
      mf.setEncryptionPassword("mypass")

      from panda3d.core import VirtualFileSystem
      vfs = VirtualFileSystem.getGlobalPtr()
      if vfs.mount(mf, ".", VirtualFileSystem.MFReadOnly):
          print('mounted')

.. only:: cpp

   .. code-block:: cpp

      PT(Multifile) mf = new Multifile;
      mf->open_read("models.mf");
      mf->set_encryption_flag(true);
      mf->set_encryption_password("mypass");

      VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr();
      if (vfs->mount(mf, ".", VirtualFileSystem::MF_read_only)) {
          std::cerr << "mounted\n";
      }

When running the application, the following should be seen::

   mounted

You can check if a certain subfile is encrypted or not using the
:meth:`~.Multifile.is_subfile_encrypted()` method, which takes the subfile index
as parameter.

It is possible to have a multifile where different subfiles have different
encryption, but you will not be able to mount it with the VirtualFileSystem or
use it with the multify tool. To mount an encrypted file using the virtual file
system, pass the password as parameter to the
:meth:`~.VirtualFileSystem.mount()` method:

.. only:: python

   .. code-block:: python

      from panda3d.core import VirtualFileSystem, Filename
      vfs = VirtualFileSystem.getGlobalPtr()
      vfs.mount(Filename("foo.mf"), ".", vfs.MFReadOnly, "foobar")

.. only:: cpp

   .. code-block:: cpp

      VirtualFileSystem *vfs = VirtualFileSystem::get_global_ptr()
      vfs->mount("./foo.mf", ".", VirtualFileSystem::MF_read_only, "foobar");

To use encryption with the multify tool, run it with the ``-e`` option, which
will prompt for a password on the command line. Alternatively, if you also
specify the ``-p "password"`` option, you can specify it in the command instead
of typing it at the prompt.
