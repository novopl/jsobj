# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest
from jsobj import jsobj


def test_all_resulting_objects_are_Context_instances():
    obj = jsobj.loads('''{
        "nested": {
            "value": 123.5
        }
    }''')
    assert isinstance(obj, jsobj)
    assert isinstance(obj.nested, jsobj)


def test_raises_ValueError_if_invalid_json_string_is_passed():
    with pytest.raises(ValueError):
        jsobj.loads('invalid JSON string')


def test_raises_TypeError_if_argument_is_not_a_string():
    with pytest.raises(TypeError):
        jsobj.loads(123)

    with pytest.raises(TypeError):
        jsobj.loads({})

    with pytest.raises(TypeError):
        jsobj.loads(123.5)
