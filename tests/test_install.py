#
# Copyright (c) 2021 Electronics and Telecommunications Research Institute 
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import unittest


class InstallTest(unittest.TestCase):

    def test_install_qplayer_cpp(self):
        from qplayer_wra import executeQASM
        # check if we can from qplayer_wra import executeQASM
        # Assert that the install was successful.
        self.assertTrue(executeQASM)
        
    def test_install_wrapper(self):
        from qplayer import executeQASM
        # check if we can from qplayer import executeQASM
        # Assert that the install was successful.
        self.assertTrue(executeQASM)

