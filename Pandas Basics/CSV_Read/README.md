csv_read

Execute One 
```py
import pandas as pd

bricks_df = pd.read_csv("brics.csv")
print(bricks_df)
```
Outcome
![alt text](image.png)

____________________________________________________________________________________________________
____________________________________________________________________________________________________

pandas_series_dataframe

Execute One
```py
import pandas as pd

#Execute One

class PandasSeries:
    def __init__(self,list):
        self.list = list
    
    def toPandasSeries(self):
        pd_series = pd.Series(self.list)
        return pd_series

somelist = ["Hi","Pandas",123]
print(type(somelist))
pdSeries = PandasSeries(somelist)
print( type(pdSeries.toPandasSeries()) )

```

Outcome
![alt text](image-1.png)