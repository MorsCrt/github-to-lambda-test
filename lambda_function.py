import pandas as pd

def lambda_handler(event,context):
    d = {'col1':[1,2]}
    df = pd.DataFrame(data=d)
    print(df)
    print("Done")
    