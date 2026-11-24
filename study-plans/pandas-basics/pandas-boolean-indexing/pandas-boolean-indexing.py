import pandas as pd

def boolean_filter(data: dict, column: str, threshold: float) -> dict:
    """
    Returns filtered_data as a dictionary of lists and count as an integer.
    """
    pass
    df=pd.DataFrame(data)
    mask=df[column]>threshold
    filter=df[mask]
    return{
        "filtered_data":filter.to_dict("list"),
        "count":len(filter)
    }