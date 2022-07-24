# -*- coding:utf-8 -*-
import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./', 'test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)
