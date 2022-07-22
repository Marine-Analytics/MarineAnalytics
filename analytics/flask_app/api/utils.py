from sklearn.preprocessing import LabelEncoder

def data_preprocessing(df):

    df['vibro_danger'] = df.apply(lambda x: 1 if x['vibro'] < 1020 else 0, axis=1)
    df['oxygen_danger'] = df.apply(lambda x: 1 if x['oxygen'] > 390 else 0, axis=1)
    df['temperature_danger'] = df.apply(lambda x: 1 if x['temperature'] <= 4 else 0, axis=1)

    return df