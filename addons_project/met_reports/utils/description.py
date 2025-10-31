# -*- coding: utf-8 -*-


def formatted_description(name):
    return name.split("\n", 1)[1] if name and "\n" in name else ""
