import utils
import os

def test_index_key():
    test_dict = {"hello": "world", "foo": "bar", "FOO": "BAZ",
                 "HELLO": "WORLD", "zzz": "sleep"}
    out_list  = ["FOO", "foo", "HELLO", "hello", "zzz"] 
    block_index = test_dict.keys()
    block_index = sorted( block_index, key = utils.index_key )
    assert block_index == out_list

def test_sort_order_list():
    input_list = ["z", "b", "a"]
    order_list = ["b", "c", "d"]
    expected   = ["b", "c", "d", "z", "a"]

    out_list = utils.sort_order_list(input_list, order_list)
    assert out_list == expected
