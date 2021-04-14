# ----- Debug

import io
import sys
_INPUT = """\
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.BISGOD
"""
sys.stdin = io.StringIO(_INPUT)

# ----- Main
import re

class BrainFuck():

    def bf(self, tx:str):
        """Exec BrainF*ck"""
        shift = 0
        maxShift = 0
        arr = []
        out = []
        Error = ""
        for i in range(len(tx)):
            vs = str(tx[i])
            if vs == '+':
                arr[shift] += 1
            elif vs == '-':
                arr[shift] -= 1
            elif vs == '>':
                if len(arr) <= shift+1: arr.append()
                shift += 1
                if shift > maxShift : maxShift = shift
            elif vs == '<':
                shift -= 1
                if shift < 0:
                    Error = "Out of range of array Error"
                    break
            elif vs == '.':
                out.append(arr[shift])
            # elif vs == '[':
            # elif vs == ',':

        result = out
        return result, Error


# ----- Exec

inputs = str(input())
print(BrainFuck().bf(inputs))
