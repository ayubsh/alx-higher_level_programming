#!/usr/bin/python3
""" Sums Args """
import sys


if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        item_l = load_from_json(filename)
    except FileNotFoundError:
        item_l = []

    for i in sys.argv[1:]:
        item_l.append(i)

    save_to_json(item_l, filename)
