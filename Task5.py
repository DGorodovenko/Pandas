import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
}

df = pd.DataFrame(data)
df["City"] = ["London", "New York", "Tokyo", "Berlin"]


def modify(df_):
    df_['Country'] = ['UK', 'USA', 'Japan', 'Germany']
    df_ = df_.drop('City', axis=1)
    #Increase the ages of all people by 1.
    df_['Age'] = df_['Age'] + 1
    df_.loc[len(df_.index)] = ['Eva', 45, 'Germany']
    #Delete the row with index 2.
    df_ = df_.drop(2, axis=0)
    #Modify the row with index 1 to have the name "Robert" and age 32.
    df_.loc[1, ['Name', 'Age']] = ['Robert', 32]
    return df_


df_modified = modify(df)
print(df_modified)
