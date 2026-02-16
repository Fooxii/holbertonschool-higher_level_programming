#!/usr/bin/python3
"""
Docstring for python-serialization.task_02_csv
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Docstring for convert_csv_to_json

    :param csv_filename: Description
    """
    try:
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open("data.json", 'w') as jsonfile:
            json.dump(data, jsonfile)

        return True

    except Exception:
        return False
