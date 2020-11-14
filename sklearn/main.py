from utils import Utils

if __name__ == "__main__":
    utils = Utils()

    data = utils.load_from_csv('./datasets/felicidad.csv')

    print(data.shape)