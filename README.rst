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

Notes
------------

The Package will provide following url endpoints

    token/ --- Login & Token
    token/refresh/ --- Refresh Token
    create_user/ --- Create New User
    verify_email/<int:user_id>/<str:token> --- Verify Email
    remove/<int:user_id> --- Remove User
    update/<int:user_id> --- Update User
    change_password_req --- Change Password Request
    change_password/<int:user_id>/<str:token> --- Change Password

