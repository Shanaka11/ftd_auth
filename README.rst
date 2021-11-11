=====
ftd_auth
=====

A Wrapper app to handle User functions in Django Rest Framework

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "ftd_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ftd_auth',
    ]

2. Include the ftd_auth URLconf in your project urls.py like this::
    path('user/', include('ftd_auth.urls')),

3. Run ``python manage.py migrate`` to create the polls models.