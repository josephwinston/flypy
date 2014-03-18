from __future__ import print_function

import sys
import unittest
import io

from flypy import jit

@jit
def print_(value):
    print(value)

@jit
def print_to_stream(stream, value):
    print(value, file=stream)

@jit
def print_no_newline(stream, value):
    print(value, end=' ', file=stream)

class TestPrint(unittest.TestCase):

    def test_print(self):
        raise unittest.SkipTest("segfault on OS X?")
        out = sys.stdout
        sys.stdout = temp_out = io.StringIO()
        try:
            #print_(10) # TODO: Int.__str__
            #print_(10.0)
            print_("hello!")
        finally:
            sys.stdout = out

        data = temp_out.getvalue()
        assert data == "10\n10.0\nhello!\n", repr(data)

    #def test_print_stream(self):
    #    temp_out = io.StringIO()
    #    print_to_stream(temp_out, 13.2)
    #    data = temp_out.getvalue()
    #    assert data == "13.2\n", repr(data)

    #def test_print_no_newline(self):
    #    temp_out = io.StringIO()
    #    print_no_newline(temp_out, 14.1)
    #    data = temp_out.getvalue()
    #    assert data == "14.1 ", repr(data)

if __name__ == "__main__":
    unittest.main()
