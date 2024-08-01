#!/usr/bin/env python


class Knight():
    def __init__(self, name, title, color):
        # store values in private instance variables
        self.name = name
        self._title = title
        self.color = color

    # decorator creates a property object named 'name'
    # and registers the method it decorates as getter method of the property
    @property
    def name(self):          # public property wraps access to private data
        return self._name

    # decorator creates a property object named 'title'
    # and registers the method it decorates as getter method of the property
    @property
    def title(self):         # public property wraps access to private data
        return self._title

    # decorator creates a property object named 'color'
    # and registers the method it decorates as getter method of the property
    @property
    def color(self):         # public property wraps access to private data
        return self._color

    # decorator references property object named 'color' defined above
    # and registers the method it decorates as setter method of the property
    @color.setter
    def color(self, color):  # public property wraps access to private data
        self._color = color

    @name.setter
    def name(self, nm):  # public property wraps access to private data
        self._name = nm