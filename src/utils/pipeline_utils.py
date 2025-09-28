# Imports
import pandas as pd
from pathlib import Path

def save_data(df: pd.DataFrame,path: Path):
    path.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(path,index=False)
    