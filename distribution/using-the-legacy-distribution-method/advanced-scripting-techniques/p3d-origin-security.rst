.. _p3d-origin-security:

P3D origin security
===================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

script_origin
-------------

In order to make it harder for a malicious web page to take advantage of an
inadvertent weakness in your p3d file's security, most JavaScript code is
forbidden from calling Python methods exposed by your p3d file.

This is controlled by setting the script origin of your p3d file. The default
script origin is empty, which means that no web pages are allowed to call
Python functions in your p3d file from JavaScript. You can set the
script_origin string to a list of hostnames that are trusted; for instance, if
you set it to "www.mydomain.com", then web pages hosted at
http://www.mydomain.com will be allowed to call your Python functions.

Note that this only affects calls into Python from JavaScript. Regardless of
the setting of script_origin, your Python code is always allowed to call any
JavaScript function. Thus, you only need to worry about setting the
script_origin if you need to write JavaScript code that calls Python functions
directly. If you are not certain whether you need this, you should leave the
script_origin setting alone.

The term "origin" is taken from JavaScript's "same-origin" policy which
normally limits the web pages that a given JavaScript program may operate on.
The origin is defined as the protocol, host, and port of the URL that hosts
the p3d file. If you omit the protocol, then any protocol is allowed; if you
omit the port, then the default port is assumed. You may define the host as
either an explicit host, e.g. "www.mydomain.com", or with one or more "*"
characters, which stands for any one component of a domain, e.g.
"*.mydomain.com" matches "alpha.mydomain.com" and "beta.mydomain.com" but not
"mydomain.com" or "www.alpha.mydomain.com". The special code "**" stands for
any zero or more components, e.g. "**.mydomain.com" matches any of the above,
including "mydomain.com" and "www.alpha.mydomain.com", but not
"yourdomain.com".

If you really wish to remove restrictions for the script_origin, you can set
it to "**", which means any host at all. We strongly recommend not doing this,
for obvious reasons.

You can also set the script_origin to a semicolon-delimited set of origin
strings; for instance, "www.mydomain.com;mydomain.com" would allow either
www.mydomain.com or mydomain.com, but not any other variant.

If a p3d file is hosted on a page that doesn't match its script_origin, then
that page's JavaScript code is forbidden from calling any Python methods
exposed the p3d file. It is also forbidden from accessing any attributes you
assign to appRunner.main, even for read-only access. (It is, however, allowed
to query certain built-in properties of main, such as main.downloadProgress or
main.read_system_log().)

You can set the script_origin with the -c parameter to packp3d, e.g.
``-c script_origin=www.mydomain.com``.

run_origin
----------

A variant on the script_origin that is less often used is run_origin. This is
a stronger restriction than script_origin; if a p3d file is hosted on a page
that doesn't match its run_origin, then the p3d file cannot be started at all.
You can do this to prevent third parties from deep-linking your p3d file or
otherwise running it out of its intended context. This is less of a security
restriction, and more a usage restriction on your own content. (Of course, a
malicious individual may make a copy your p3d file and modify the run_origin
setting, to allow it to run on their own page. But they will have to re-sign
it with their own certificate, since any modifications will invalidate your
own signature.)

The default run_origin is "**", which means there is no restriction. You can
set the run_origin with the -c parameter to packp3d, e.g.
``-c run_origin=www.mydomain.com``.
