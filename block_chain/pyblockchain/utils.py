import collections

def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(sorted(unsorted_dict.items(), key=lambda d:d[0]))

def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25}Chain{i}{"="*25}')
        for k, v in chain.items():
            if k == 'transaction':
                print(k)
                for d in v:
                    print(f'{"-"*40}')
                    for kk, vv in d.items():
                        print(f'{kk:30}{vv}')
            else:
                print(f'{k:15}{v}')
    print(f'{"*"*25}')


if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 2, 'a': 1}
    
    print(sorted_dict_by_key(dict1))
    print(sorted_dict_by_key(dict2))
    
    # if dict1 == dict2:
    #     print('true')
    # else:
    #     print('False')
    
    # print(collections.OrderedDict(dict1))
    # print(collections.OrderedDict(dict2))
    
    # if collections.OrderedDict(dict1) == collections.OrderedDict(dict2):
    #     print('true')
    # else:
    #     print('False')
        
    # print(dict2)
    # print(dict2.items())
    # print(sorted(dict2.items()))



