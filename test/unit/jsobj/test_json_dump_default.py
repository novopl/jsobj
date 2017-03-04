# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import date, datetime
from decimal import Decimal

import pytest

from jsobj import json_dump_default


class Serializable(object):
    def serialize(self):
        return 'serialized_value'


@pytest.mark.parametrize('in_val,out_val', (
    (Decimal('10.00'), 10.0),
    (datetime(2016, 12, 12, 6, 30, 45), '2016-12-12T06:30:45'),
    (date(2016, 12, 12), '2016-12-12'),
    (Serializable(), 'serialized_value'),
    ('str', 'str'),
    (10.0, 10.0),
    (123, 123),
))
def test_serializes_datetime_to_isoformat(in_val, out_val):
    assert json_dump_default(in_val) == out_val
