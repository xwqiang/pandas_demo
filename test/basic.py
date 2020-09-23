import pandas as pd
import matplotlib.pyplot as plt

scores = {
    'name': ['johe', 'mike', 'tom', 'jeck'],
    'sex': ['male', 'female', 'male', 'male'],
    'chinese': [88, 83, 90, 78],
    'math': [96, 88, 86, 90],
    'english': [85, 80, 90, 75]
}
df = pd.DataFrame(scores)  # 可传入 index=[...] 作为索引
df = pd.DataFrame(scores, index=scores['name'])  # 可传入 index=[...] 作为索引


def f(score):
    if score >= 90:
        return '优秀'
    elif score >= 60:
        return '及格'
    else:
        return '不及格'


if __name__ == '__main__':
    # df['数学分类'] = df['math'].map(f)  # 对一列进行操作并生成新的一列
    # print(df)
    df['total'] = df.apply(lambda x: x.chinese + x.math + x.english, axis=1)  # 对多列进行操作并生成新的一列
    # df = df.applymap(lambda x: str(x) + ' * ')  # 对所有数据进行操作
    print(df)

    # 支持中文
    # font = {'family': 'DejaVu Sans',
    #         'weight': 'bold',
    #         'size': '16'}
    # plt.rc('font', **font)  # pass in the font dict as kwargs
    # plt.rc('axes', unicode_minus=False)
    # df.plot()  # pandas绘制线性图
    # plt.show()  # 借助matplotlib弹窗显示

    # df.plot.bar()  # pandas绘制柱状图
    # plt.show()

    # df.hist()  # pandas绘制直方图
    # plt.show()
