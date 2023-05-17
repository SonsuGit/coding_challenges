import re

def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine']
    index = [str(n) for n in range(len(eng))]
    dict_eng = dict(zip(eng, index))
    for i in dict_eng.keys():
        s = re.sub(i, dict_eng[i], s)
    return int(s)