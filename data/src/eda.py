import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent.parent / "raw" / "neo_2025_to_now.csv"
df = pd.read_csv(file_path)
print(df.head(20))
