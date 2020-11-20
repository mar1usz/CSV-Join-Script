import pandas as pd
import sys

in1 = sys.argv[1]
in2 = sys.argv[2]
out = sys.argv[3]

df1 = pd.read_csv(in1)
df2 = pd.read_csv(in2)

pd.merge(df1, df2, "outer").to_csv(out, index=False)
