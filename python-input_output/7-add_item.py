#!/usr/bin/python3
"""
Docstring for python-input_output.7-add_item
"""
import sys
import save_to_json_file from 5-save_to_json_file
import load_from_json_file from 6-load_from_json_file

file = "add_item.json"

try:
    my_list = load_from_json_file(file)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, file)
