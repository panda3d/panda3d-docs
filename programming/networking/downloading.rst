.. _downloading-a-file:

Downloading a File
==================

To download a file while the game is running without blocking the connections
one has to use :class:`.HTTPClient` and :class:`.HTTPChannel` objects. This will
allow the file to be downloaded in the background using the downloadTask task.

.. code-block:: python

   self.http = HTTPClient()
   self.channel = self.http.makeChannel(True)
   self.channel.beginGetDocument(DocumentSpec('http://my.url/'))
   self.rf = Ramfile()
   self.channel.downloadToRam(self.rf)
   taskMgr.add(self.downloadTask, 'download')

   def downloadTask(self, task):
       if self.channel.run():
           # Still waiting for file to finish downloading.
           return task.cont
       if not self.channel.isDownloadComplete():
           print("Error downloading file.")
           return task.done
       data = self.rf.getData()
       print("got data:")
       print(data)
       return task.done

You can also download to file

.. code-block:: python

   channel.downloadToFile(Filename(fileName))

The file channel can be queried for further information while the game is
running to get the current download state.

.. code-block:: python

   mbDownloaded = self.channel.getBytesDownloaded() / 1024 / 1024
   percentDownloaded = 100. * self.channel.getBytesDownloaded() / channel.getFileSize()
