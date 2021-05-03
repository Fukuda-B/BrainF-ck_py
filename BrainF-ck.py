"""
BrainF-ck.py

[ Compiler specification ]
Based on Brainfuck (bf20041219),

Characteristic behavior
Incrementing 255 will set it to 0.
Decrementing 0 will set it to 255.

"""


# ----- Debug

import io
import sys
_INPUT = """\
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.

"""
sys.stdin = io.StringIO(_INPUT)

# ----- Main
class BrainFuck():
    
    def __init__(self, code, option):
        self.parsed = "" # parsed code
        self.code = BrainFuck.origin(self, code) # no comment code
        self.option = option # debug option
        self.out = [] # output string
        self.error = "" # output error
        self.arr = [0] # memory value
        self.maxShift = 0 # max pointer position
        self.shift = 0 # pointer position
        self.i = 0 # counter
        self.debug = [] # debug result

    def bf_main(self, code:str):
        """ Exec BrainF*ck """
        i, tx, arr, shift = \
            0, code, self.arr, self.shift
        while 1:
            if self.option: self.debug.append(f'{tx[i]}" @{self.shift} {self.arr}"') # debug
            if not tx[i] == '[' and not tx[i] == ']': self.parsed += tx[i]

            vs = str(tx[i])
            if vs == '+': self.arr[self.shift] = (self.arr[self.shift]+1) if self.arr[self.shift] < 255 else 0 # 255未満ならインクリメント、255以上なら0
            elif vs == '-': self.arr[self.shift] = (self.arr[self.shift]-1) if self.arr[self.shift] > 0 else 255 # 0より大きい場合はデクリメント、0未満なら255
            elif vs == '>': # ポインタをインクリメント (+)
                if len(self.arr) <= self.shift+1: self.arr.append(0)
                self.shift += 1
                if self.shift > self.maxShift: self.maxShift = self.shift
            elif vs == '<': # ポインタをデクリメント(-)
                self.shift -= 1
                if self.shift < 0:
                    self.error = 'Out of range of array Error'
                    break
            elif vs == '.': # 出力の追加
                self.out.append(self.arr[self.shift])
            elif vs == '[':
                c_cnt, l_cnt = 1, 1
                while(c_cnt != 0):
                    vvs = tx[i+l_cnt]
                    if vvs == '[': c_cnt += 1
                    if vvs == ']': c_cnt -= 1
                    l_cnt += 1
                    if i+l_cnt > len(tx):
                        self.error = ' ] are missing.'
                        break

                while self.arr[self.shift] != 0:
                    self.arr = BrainFuck.bf_main(self, tx[i+1:i+l_cnt-1])
                print(l_cnt ,self.i, len(tx))
            i += 1
            if i >= len(tx):
                self.i += i
                break
        return self.arr

    # self, ソースコード, デバッグオプション
    def bf(self):
        """Exec BrainF*ck"""
        res = BrainFuck.bf_main(self, self.code)

    # コメント削除
    def origin(self, tx):
        return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '>', '<', '+', '-'], tx))

# ----- Exec

inputs = str(input())
bfc = BrainFuck(inputs, 1)
bfc.bf()
print(bfc.out)


# -----
if __name__ == '__main__':
    pass
