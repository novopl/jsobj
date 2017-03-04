# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest
from jsobj import jsobj


@pytest.fixture
def test_obj():
    return jsobj(
        name='john',
        age=32
    )


def test_str_shows_json_string(test_obj):
    obj = jsobj.loads(str(test_obj))
    assert obj == test_obj


def test_unicode_shows_json_string(test_obj):
    obj = jsobj.loads(test_obj.__unicode__())
    assert obj == test_obj


def test_repr_shows_class_name_and_all_items(test_obj):
    assert repr(test_obj) == '<jsobj {}>'.format(str(test_obj))


def test_read_dict_value_though_attribute(test_obj):
    assert test_obj['name'] == test_obj.name
    assert test_obj['age'] == test_obj.age


def test_getattr_raises_AttributeError_if_value_doesnt_exist(test_obj):
    with pytest.raises(AttributeError):
        test_obj.non_existent_field


def test_set_value_using_an_attribute(test_obj):
    test_obj.name = 'jane'
    assert test_obj['name'] == 'jane'
