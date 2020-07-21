#!/usr/bin/python
# -*- Coding: utf-8 -*-

def get_first(data, key, asc, tgt):
    '''
    keyをグループとした場合の、対象列の最初行の値を取得する

    Params
    ------
    data: dataframe
        対象データ
    key: list(str)
        グループとする列名
    asc: list(bool)
        昇順/降順指定
    tgt: list(str)
        値の取得対象の列名
    '''
    df = data[key+tgt].copy()
    df = data[(data[key].isna().sum(1)==0)
              &(data[tgt].isna().sum(1)==0)]
    df = df.sort_values(by=key, ascending=asc)
    df = df.groupby(key[0])[tgt].take([0])
    df = df.reset_index(level=1, drop=True)
    return df

def get_concated(data, key, tgt, dlm):
    '''
    keyをグループとした場合の、対象列の最初行の値を取得する

    Params
    ------
    data: dataframe
        対象データ
    key: str
        グループとする列名
    tgt: str
        値の取得対象の列名
    dlm: str
        デリミタ
    '''
    df = data[[key, tgt]].copy()
    df = data[(~data[key].isna())
              &(~data[tgt].isna())]
    vals = list()
    for k in set(df[key]):
        subs = df[df[key]==k]
        v = subs[tgt].astype(str).unique()
        v = dlm.join(v)
        vals.append([k, v])
    vals = pd.DataFrame(vals, columns=[key, tgt])
    return vals

if __name__ == "__main__":
    pass
