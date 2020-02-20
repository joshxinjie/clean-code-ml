def train_model(modelClass, X_train, Y_train, X_test, **kwargs):
    model = modelClass(**kwargs)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy = round(model.score(X_train, Y_train) * 100, 2)
    return model, accuracy

def add(first_num, second_num):
    return first_num + second_num

def multiply_by_10(df):
    #return df.mul(10)
    for col in df.columns:
        if df.dtypes[col] != 'object':
            df[col] = df[col] * 10
    return df
