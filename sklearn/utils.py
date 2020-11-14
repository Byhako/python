import pandas as pd

class Utils:
    def load_from_csv(self, path):
        return pd.read_csv(path)

    def features_target(self, dataset, drop_columns, y):
        x = dataset.drop(drop_columns, axis=1)
        y = dataset[y]
        return x, y

    def model_export(self, clf, score):
        pass
