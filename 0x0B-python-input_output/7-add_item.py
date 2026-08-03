#!/usr/bin/python3
'''
This module contains a script that adds all arguments to a Python list, and
then save them to a file.
'''
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        args_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        args_list = []

    for i in range(1, len(argv)):
        args_list.append(argv[i])

    save_to_json_file(args_list, 'add_item.json')
