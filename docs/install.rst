============
Installation
============

Make sure you have Django installed. Then install the package from PyPI::

    pip install django-envelope

or::

    easy_install django-envelope

If you like living on the edge, grab the development version from Github_::

    git clone git://github.com/zsiciarz/django-envelope.git
    cd django-envelope
    python setup.py install

To enable a simple antispam check, install `django-honeypot`_. Envelope will
automatically pick that one up and use in the contact form.

.. _Github: http://github.com/zsiciarz/django-envelope
.. _`django-honeypot`: https://github.com/sunlightlabs/django-honeypot/
