#!/usr/bin/python3
"""
Contain class "Student"
"""


class Student:
    """Representation of student"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation of Student instance
        with specified attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
