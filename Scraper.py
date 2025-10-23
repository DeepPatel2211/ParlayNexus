import nfl_data_py as nfl
import pandas as pd

nfl.import_pbp_data(2004,downcast=True, cache=False, alt_path=None)

print("hello")