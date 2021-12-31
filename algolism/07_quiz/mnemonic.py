"""
Input：568-379-8466、Output:[..., 'LOVEPYTHON', ...]
"""

from typing import List

NUM_ALPHABET_MAPPING={
    0:'+',
    1:'@',
    2:'ABC',
    3:'DEF',
    4:'GHI',
    5:'JKL',
    6:'MNO',
    7:'PQRS',
    8:'TUV',
    9:'WXYZ'
}

def phone_mnemonic_v1(phone_number: str) -> List[str]:
    phone_number = [int(s) for s in phone_number.replace('-','')]
    # print(phone_number)
    tmp = [''] * len(phone_number)
    candidate = []
    
    def find_candidate_alphabet(digit=0):
        if digit == len(phone_number):
            candidate.append(''.join(tmp))
        else: 
            for char in NUM_ALPHABET_MAPPING[phone_number[digit]]:
                tmp[digit] = char
                find_candidate_alphabet(digit+1)
    find_candidate_alphabet()
    return candidate


if __name__ == '__main__':
    pn = '568-379-8466'
    # pn ='23'
    for s in phone_mnemonic_v1(pn):
        if s == 'LOVEPYTHON':
            print(s)