#!/usr /bin/env python
# -*- coding: utf-8 -*-

"""
使用json.dumps 将 json 格式的数据写到文件里
Python--使用json.dumps 将 json 格式的数据写到文件里--with open as f
"""

measurements = [
    {'weight': 392.3, 'color': 'purple', 'temperature': 33.4},
    {'weight': 34.0, 'color': 'green', 'temperature': -3.1},
]


def store(measurements):
    import json
    with open('measurements.json', 'w') as f:
        f.write(json.dumps(measurements))


if __name__ == "__main__":
    store(measurements)