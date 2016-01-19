# -*- coding: utf-8 -*-


class CookieStorage(object):
    """Interface between Cookies and Database.

    Args:
        db (Database): The Database class instance to wrap.
    """

    def __init__(self, db):
        self.db = db

    def get(self, key):
        """Get the value of the given cookie key.

        Args:
            key (str): The name of the cookie key to retrieve.

        Returns:
            value (str): The value of the key or None if undefined.
        """
        # if callable(getattr(self.db, 'find')):
        return self.db.cookies.find_one({key: {'$exists': True}})

    def set(self, key, value):
        """Set the value of the defined cookie key.

        Args:
            key (str): The name of the cookie key to set.
            value (str): The value associated to the cookie key to set.

        Returns:
            raw_result (str): The result of the attempt to store the cookie.
        """
        r = self.db.cookies.replace_one({key: {'$exists': True}}, {key: value}, upsert=True)
        return r.raw_result

    def delete(self, key):
        """Delete the value of the given cookie key.

        Args:
            key (str): The name of the cookie key to delete.

        Returns:
            raw_result (str): The result of the attempt to delete the cookie.
        """
        return self.db.cookies.remove({key: {'$exists': True}})

    def clean(self):
        """Delete all the cookies stored in the database.

        Returns:
            raw_result (str): The result of the cleaning.
        """
        return self.db.cookies.remove({})
