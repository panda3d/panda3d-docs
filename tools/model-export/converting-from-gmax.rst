.. _converting-from-gmax:

Converting from GMax
====================

To convert models to Panda from GMax, you must first convert models to .X
format, and then load them into Panda as .X files, or convert them further
using x2egg and/or egg2bam.

There is a fair amount of work involved in setting up the GMax-to-X converter,
but once it is set up the conversion process is reportedly very easy.

Installation
------------


There are several plug-ins required to export .X files from gmax:

1. First download the ‘Gmax gamepack SDK’ found at this link: `FlightSimulator
exporter
plugin <http://www.microsoft.com/games/flightsimulator/fs2004_downloads_sdk.asp#gmax>`__.
Size is about 15Mb. Although only 3 files are actually needed, they are not
available as separate downloads, so unfortunately you’ll need to download the
whole thing.

2. Next, download programs
'`MDLCommander <http://hometown.aol.de/_ht_a/docmoriarty3/fs2002/en/mdlcommander_dl.html>`__'
and '`Middleman <http://thegreatptmd.tripod.com/>`__'.

3. After download, you’ll see that the 'fs2004_sdk-gmax-setup' is an exe. If
you install it in the default gmax directory, you’ll end up with a lot of
extra stuff that you don’t need. So create a new folder somewhere on your hard
drive and install it there.

4. When done, open the folder, go to gamepacks > fs2004 > plugins. And copy
all 3 files: 'FSModelExp.dle', 'makemdl.exe' and 'makemdl.parts.xml' to your
main ../gmax/plugins folder.

5. You need to rename two of the files. Right click on 'makemdl.exe' and
rename it to to 'mkmdl.exe'. Then right click on 'makemdl.parts.xml' and
rename it to 'mkmdl.parts.xml' (without the quotes).

6. Next, unzip 'MDLCommander.zip'. Then copy 'mdlcommander.exe' to your main
../gmax/plugins folder. This file also needs to be renamed. Right click on
'mdlcommander.exe' and rename it to 'makem.exe'.

7. Finally, unzip 'Middleman13beta3.zip'. Then copy 'makemdl.exe' to your main
../gmax/plugins folder. That’s it, you’re done!

Using
-----


To convert your gmax model to .X format: Go to ‘File > Export’ and select
‘Flightsim Aircraft Object (.MDL) from the file type dropdown. Type in a
filename and click Save. The Middleman dialog window should now appear. Click
the ‘Options’ tab and check ‘SaveXFile’ (this saves the x file) and
‘nocompile’ (this tells mdlcommander to only create an .X file not mdl/bgl).
Then click the GO button.

After a few seconds the dialog will close and your newly exported .X model
should be in the directory where you saved it to.

Bugs in the Process
-------------------


The GMax converter writes slightly nonstandard .X files; it writes the name
"TextureFileName" instead of "TextureFilename" for each texture reference. It
may also generate hyphens in identifiers. Both of these can confuse the X file
parser in Panda3D version 1.0.4 and earlier (this will be fixed in a future
release of Panda). In the meantime, the temporary workaround is to edit the .X
file by hand to rename these strings to the correct case and remove hyphens.
