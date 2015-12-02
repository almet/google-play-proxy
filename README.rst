Documentation
=============

A proxy for Google Play. Provides you with a way to download your APKs easily,
and without being tracked by Google.

How to use it?
##############

Install it using pip
::

  $ pip install gplayproxy

Then, run it how you want, for instance with pserve::

  $ pserve gplayproxy.ini

In a separate process, you also need to run the worker::

  $ rqworker

Then, the only thing you need is an HTTP client to tell the proxy to download
a package. For instance::

  $ http post http://localhost:6543/package/org.thoughtcrime.securesms
