# -*- coding: utf-8 -*-

from .context import qplayer

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(qplayer.hmm())


if __name__ == '__main__':
    unittest.main()
