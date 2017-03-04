# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest
from jsobj import jsobj, json_dumps


@pytest.fixture()
def simple_data():
    return {
        'name': 'john',
        'age': 32
    }

@pytest.fixture()
def nested_data():
    return {
        'name': 'john',
        'age': 32,
        'account':{
            'bank': 'Bank Inc.',
            'number': {
                'sort_code': '11-22-33',
                'account': '12345678'
            }
        }
    }


def test_creates_empty_context_if_no_arguments_passed():
    obj = jsobj.create()
    assert obj == {}


def test_can_pass_initial_data_as_dict(simple_data):
    obj = jsobj.create(simple_data)

    assert obj == simple_data


def test_can_create_from_valid_json_string(simple_data):
    obj = jsobj.create(
        json_dumps(jsobj(simple_data))
    )

    assert obj == simple_data


def test_using_kwargs_with_constructor(simple_data):
    obj = jsobj(**simple_data)

    assert obj == simple_data


def test_nested_dicts_become_jsobjs(nested_data):
    obj = jsobj.create(nested_data)

    assert isinstance(obj.account, jsobj)
    assert isinstance(obj.account.number, jsobj)


def test_constructor_does_not_convert_nested_dicts_to_jsobj(nested_data):
    obj = jsobj(nested_data)

    assert not isinstance(obj.account, jsobj)
    assert not isinstance(obj.account['number'], jsobj)


def test_raises_ValueError_if_invalid_json_string_is_passed():
    with pytest.raises(ValueError):
        jsobj.create('invalid JSON string')
