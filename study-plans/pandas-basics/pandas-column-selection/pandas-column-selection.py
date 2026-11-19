import pandas as pd

def select_column(data: dict, column: str) -> dict:
    """
    Returns a dictionary with values as a list and length as an integer.
    """
    df=pd.DataFrame(data)
    series=df[column]
    
    return{
        "values":series.tolist(),
        "length":len(series),
    }
        
