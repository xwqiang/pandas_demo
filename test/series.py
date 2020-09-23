from pandas import Series


if __name__ == '__main__':
    s = Series([1, 4, 'ww', 'tt'])
    print(s)
    print(s.index)
    print("--------")
    s2 = Series(['wangxing', 'man', 24], index=['name', 'sex', 'age'])
    print(s2)
    print(s2['name'])
    print("--------")
    sd = {'python': 9000, 'c++': 9001, 'c#': 9000}
    print(sd)
    print(sd['python'])
    print("--------")
    s4 = Series(sd, index=['java', 'c++', 'c#'])
    print(s4)

    s4.index = ['语文','数学','English']
    print(s4)