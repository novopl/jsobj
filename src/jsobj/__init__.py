# -*- coding: utf-8 -*-
"""
Python implementaiton for a JavaScript-like object.

This wraps the built-in dict for performance and just give a conveniant
way to navigate the data.
"""
from __future__ import absolute_import, unicode_literals
import json
from datetime import date, datetime
from decimal import Decimal

from six import string_types, iteritems


def json_dump_default(value):
    """ Default JSON serializer. """
    if isinstance(value, Decimal):
        return float(value)

    elif isinstance(value, (date, datetime)):
        return value.isoformat()

    elif hasattr(value, 'serialize') and callable(value.serialize):
        return value.serialize()

    return value


def json_dumps(data, **kwargs):
    """ Equivalent of json.dumps but will properly serialize dates. """
    kwargs.setdefault('indent', 2)
    kwargs.setdefault('default', json_dump_default)
    return json.dumps(data, **kwargs)


class jsobj(dict):
    """ A simple context implementation.

    It allows easy reading/writing of values into it and can be easily
    serialized to/from JSON.
    """
    @classmethod
    def create(cls, data=None):
        """ Create new context.

        :param dict|string data:
            Initial context data. This will be shallow copied into the context.
            This can be either a string with the JSON object or anything that
            is accepted by the built-in dict() constructor.
        :return:
            Newly created context object.
        """
        if data is None:
            return cls()
        elif isinstance(data, string_types):
            return cls.loads(data)
        else:
            ret = cls()
            for name, value in iteritems(data):
                if isinstance(value, dict):
                    value = jsobj.create(value)
                ret[name] = value
            return ret

    @classmethod
    def loads(cls, string):
        """ Load context from JSON string. """
        return json.loads(string, object_pairs_hook=cls)

    def __repr__(self):
        """ Return pretty representation for the context. """
        return '<jsobj {0}>'.format(str(self))

    def __str__(self):
        """ Use JSON as string representation """
        return json_dumps(self)

    def __unicode__(self):
        return json_dumps(self)

    def __setattr__(self, name, value):
        """ This allows setting context values as if they were attributes. """
        self[name] = value

    def __getattr__(self, name):
        """ This allows reading context values as if they were attributes.

        This makes it a bit easier to use the Context objects (they work a bit
        like JavaScript objects).
        """
        try:
            return self[name]
        except KeyError:
            raise AttributeError("No attribute {}".format(name))
