#Pandas Practice
import pandas as pd
a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"])
df = pd.DataFrame(myvar)
print(df.info())
