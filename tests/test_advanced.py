# -*- coding: utf-8 -*-
from .context import scanning_task
import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(scanning_task.main())

if __name__ == '__main__':
    unittest.main()