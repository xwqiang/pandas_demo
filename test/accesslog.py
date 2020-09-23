import pandas as pd

if __name__ == '__main__':
    # df1 = pd.read_csv("/Users/xuwuqiang/Downloads/access-20200922.log", sep="|", encoding="utf-8", names=range(0, 13),
    #                   header=0)
    df2 = pd.read_csv("/Users/xuwuqiang/Downloads/access-20200921.log", sep="|", encoding="utf-8", names=range(0, 13),
                      header=0)

    print("------------1------------")
    # 合并
    # df = pd.concat([df1, df2],  sort=False)

    # 统计有多少种不同的值
    # print(df1[5].nunique())
    # print(df1[5].unique())

    print("------------2------------")
    # print(df[5])
    print("------------3------------")
    # print(df2.groupby(by=5,as_index=False).size())
    # print(df2.groupby(by=5,as_index=False).count())
    # 类似于sql：select x1,count(distinct x1),count(distinct x2),count(distinct x3) from table group by x1
    # print(df2.groupby(by=5,as_index=False).nunique())
    # print(df2.groupby(by=[5, 6], as_index=False).size())

    print("------------4------------")
    # print(df1[5].describe())
    print("------------5 按照小时统计接口调用量------------")
    df2['hour'] = df2.apply(lambda x: str(x[0])[:13], axis=1)  # 对多列进行操作并生成新的一列
    # print(df2.filter(items=[0, 5, 'hour']))
    # print(df2.filter(items=[0, 5, 'hour'])[df2[5].isin(['statusService:get','commentService:get'])])
    print(df2.filter(items=[0, 5, 'hour'])[df2[5].isin(['statusService:get','commentService:get'])].groupby(by=['hour',5]).size())
