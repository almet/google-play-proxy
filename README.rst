A proxy for the google play store
#################################

Provides you with a way to download your APKs easily, and without being tracked
by Google. Since I don't use their market application on my phone, I wanted to
have a way to download the APKs from the web, hosted at a location I trust, so
here it is!

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
a package. So you can go with your browser at
http://localhost:6543/package/org.thoughtcrime.securesms

And it will download it at the location specified in the configuration file.
