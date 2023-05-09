##Loading the data
import pandas as pd
# data = pd.read_csv('rep1bed.csv')
# print(data)

class importdata():
    
    def __init__(self,data):
        self.data = data

    @classmethod
    def load_data(path):
        df =pd.read_csv(path)
        return df
    

if __name__ == "main":
    df = importdata().load_data(path= "rep1bed.csv")
    print(df)
