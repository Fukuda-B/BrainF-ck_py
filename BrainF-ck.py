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

    # コンパイラ本体
    async def bf(self, tx:str):
        """Exec BrainF*ck"""
        shift = 0
        maxShift = 0
        arr = []
        out = []
        Error = ""
        for i in range(len(tx)):
            vs = str(tx[i])
            if vs == '+': # インクリメント
                arr[shift] += 1
            elif vs == '-': # デクリメント
                arr[shift] -= 1
            elif vs == '>': # ポインタシフト (+)
                if len(arr) <= shift+1: arr.append()
                shift += 1
                if shift > maxShift : maxShift = shift
            elif vs == '<': # ポインタシフト(-)
                shift -= 1
                if shift < 0:
                    Error = "Out of range of array Error"
                    break
            elif vs == '.':
                out.append(arr[shift])
            elif vs == '[':
                if arr[shift] != 0:
                    c_cnt, res_loop = 1, [] # ループチェッカー, 戻り値
                    s_ptr, e_ptr = sfhit, 0 # 開始ポインタ, 終了ポインタ
                    l_cnt = 0 # ループカウンタ
                    while(c_cnt == 0):
                        if vvs == '[': cnt += 1
                        if vvs == ']': cnt -= 1
                        l_cnt += 1
                    e_ptr = shift + l_cnt

            # elif vs == ',':

        result = out
        return result, Error

    # コメント削除
    async def origin(tx):
        return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '>', '<', '+', '-'], tx))

# ----- Exec

inputs = str(input())
print(BrainFuck().bf(inputs))
