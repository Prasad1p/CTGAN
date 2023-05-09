import ctgan
from ctgan import CTGAN
import table_evaluator
from input.data import importdata


class CTGANmodelfit():
    
    def __init__(self) -> None:
        pass


    def model_fit(data,cat_features,epochs):
        model = CTGAN()
        model.fit(data, cat_features, epochs)
        return None


if __name__ == "main":
    # print('something')
    # df = importdata().load_data("rep1bed.csv")
    # print(df)
    # categorical_features =['Chromosome']
    # model = CTGANmodelfit.model_fit(df,categorical_features,epochs=5000)