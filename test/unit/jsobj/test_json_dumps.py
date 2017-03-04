# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from jsobj import jsobj, json_dumps
from mock import patch


@patch('json.dumps')
def test_by_default_resulting_json_is_indented(p_json_dumps):
    obj = jsobj({'field': 'value'})

    p_json_dumps.return_value = '{}'
    json_dumps(obj)

    p_json_dumps.assert_called_once()

    args, kw = p_json_dumps.call_args
    assert 'indent' in kw
    assert kw['indent'] == 2

