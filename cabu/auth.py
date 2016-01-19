# -*- coding: utf-8 -*-

import json
from functools import wraps
from flask import request, Response, current_app as app


def check_auth(username, password):
    """Determines if the given params are similar to the ones stored on config.

    This small function compares the given username and password to the ones and
    returning a boolean accordingly.

    Args:
        username (str): The username used for basic_auth.
        password (str): The password used for basic_auth.

    Returns:
        auth (bool): True if authorized, False if not.
    """
    return username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']


def authenticate():
    """Response helper for un-authorized attempts to access to the app.

    Returns:
        response (object): A Flask Response object with a custom message
        and a 401 status.
    """
    return Response(
        json.dumps({
            'message':
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials',
        }),
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_admin(f):  # pragma: no cover
    """Decorator to define endpoints that requires Basic Auth.

    Args:
        f (func): An route function.

    Returns:
        response (object): 401 if unauthorized.
        f (func): The route to call.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
