from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    df = df.dropna()

    le = LabelEncoder()
    if 'label' in df.columns:
        df['label'] = le.fit_transform(df['label'])

    return df