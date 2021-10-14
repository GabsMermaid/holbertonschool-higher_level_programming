#!/usr/bin/python3
"""
Containsfunction "wrtie_file"
"""


def write_file(filename="", text=""):
    """
    function to write files
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
