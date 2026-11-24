import pandas as pd

def iloc_selection(data: dict, row: int, col: int) -> list:
    """
    Returns [element, row_values, col_values], with both value sequences as lists.
    """
    df=pd.DataFrame(data)
    element=df.iloc[row, col];
    row_value=df.iloc[row,:].tolist()
    col_value=df.iloc[:,col].tolist()
    return [element,row_value,col_value]