import pandas as pd

if __name__ == '__main__':
    df1 = pd.read_csv("/Users/xuwuqiang/Downloads/1.lin", sep="\t", encoding="utf-8",
                      names=['name', 'seller', 'clientid', 'sign', 'type', 'source', 'channel', 'flow'], header=0)

    df1 = df1.fillna(value="").applymap(lambda x: str(x).strip())
    df1['uk'] = df1.apply(lambda x: str(x['name']) + str(x.clientid), axis=1)

    df2 = pd.read_csv("/Users/xuwuqiang/Downloads/2.lin", sep="\t", encoding="utf-8", names=range(0, 13), header=0)
    df2 = df2.fillna(value="").applymap(lambda x: str(x).strip())
    df2['uk'] = df2.apply(lambda x: str(x[2]) + str(x[5]), axis=1)

    # print(df1.uk.values)

    # 2 in 1
    for i in df2.uk.values:
        if i in df1.uk.values:
            # print(i)
            df2['flag'] = df2.apply(lambda x: "true", axis=1)
    print(df2)
    # print(df2[2])
    # print(df2[5])
    # print(df.head(2))
    # print(df.name)
    # print(df.name[:4])
    # print(df.values)
    # print(df.name.values)
    # df.fillna(value=0)
    # for index, row in df.iterrows():
    #     print(index, row["name"], row["seller"])
