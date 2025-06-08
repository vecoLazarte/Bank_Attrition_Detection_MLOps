import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from pathlib import Path


data_dir = Path("data") / "in"
clientes_path = data_dir / "oot_clientes_sample.csv"
reqs_path = data_dir / "oot_requerimientos_sample.csv"


oot_clientes = pd.read_csv(clientes_path)
oot_requirements = pd.read_csv(reqs_path)
