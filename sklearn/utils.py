import pandas as pd
import joblib

class Utils:
    def load_from_csv(self, path):
        return pd.read_csv(path)

    def features_target(self, dataset, drop_columns, y):
        x = dataset.drop(drop_columns, axis=1)
        y = dataset[y]
        return x, y

    def model_export(self, modelo, score):
        print(f'Best Score: {score}')
        joblib.dump(modelo, './models/best_model.pkl')
