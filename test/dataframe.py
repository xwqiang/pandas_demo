from pandas import Series, DataFrame

if __name__ == '__main__':
    data = {"name": ['google', 'baidu', 'yahoo'], "marks": [100, 200, 300], "price": [1, 2, 3]}
    f1 = DataFrame(data)
    print(DataFrame(f1))

    # 顺序可以被规定
    f2 = DataFrame(data, columns=['name', 'price', 'marks'])
    print(f2)

    # 数据的索引也能够自定义
    f3 = DataFrame(data, columns=['name', 'marks', 'price'], index=['a', 'b', 'c'])
    print(f3)

    # 字典套字典
    newdata = {'lang': {'first': 'python', 'second': 'java'}, 'price': {'first': 5000, 'second': 2000}}
    f4 = DataFrame(newdata)
    print(f4)

    newdata = {"lang": {"firstline": "python", "secondline": "java"}, "price": {"firstline": 8000}}
    f4 = DataFrame(newdata)
    print(f4)

    newdata1 = {'username': {'first': 'wangxing', 'second': 'dadiao'}, 'age': {'first': 24, 'second': 25}}
    f6 = DataFrame(newdata1, columns=['username', 'age', 'sex'])
    print(f6)

    ssex = Series(['男', '女'], index=['first', 'second'])
