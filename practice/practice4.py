import pandas as pd
import os


def return_counter(data_frame, column_name, limit):
   from collections import Counter    
   print(dict(Counter(data_frame[column_name].values).most_common(limit)))

def return_statistics(data_frame, categorical_column, numerical_column):
    mean = []
    std = []
    field = []
    for i in set(list(data_frame[categorical_column].values)):
        new_data = data_frame[data_frame[categorical_column] == i]
        field.append(i)
        mean.append(new_data[numerical_column].mean())
        std.append(new_data[numerical_column].std())
    df = pd.DataFrame({'{}'.format(categorical_column): field, 'mean {}'.format(numerical_column): mean, 'std in {}'.format(numerical_column): std})
    df.sort_values('mean {}'.format(numerical_column), inplace = True, ascending = False)
    df.dropna(inplace = True)
    return df

def get_boxplot_of_categories(data_frame, categorical_column, numerical_column, limit):
    import seaborn as sns
    from collections import Counter
    keys = []
    for i in dict(Counter(df[categorical_column].values).most_common(limit)):
        keys.append(i)
    print(keys)
    df_new = df[df[categorical_column].isin(keys)]
    sns.set()
    sns.boxplot(x = df_new[categorical_column], y =      df_new[numerical_column])

def main():
    #print(os.getcwd())
    df = pd.read_csv("/Users/izekc/Github/Leetcode-practice/practice/netflix_titles.csv")
    #print(list(df.columns))
    #print("Number of rows:", len(df))
    ##print(df.head())
    #return_counter(df, 'country', 5)
    #df['director'].dropna(inplace = True)
    #return_counter(df, 'director', 5)
    #df_d1 = df[df['director'] =='Raúl Campos, Jan Suter']
    #print(set(df_d1['title']))
    #print(set(df_d1['country']))
    df = df[df['type'] == 'Movie']
    df['duration'] = df['duration'].map(lambda x: x.rstrip('min')).astype(int)
    #print(set(df['duration']))

    stats = return_statistics(df, 'listed_in', 'duration')
    #print(stats.head(15))


    get_boxplot_of_categories(df, 'listed_in', 'duration', 5)

if __name__ == "__main__":
    main()