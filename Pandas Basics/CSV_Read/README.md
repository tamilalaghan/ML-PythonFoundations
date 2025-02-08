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


Execute Two
```py
#Execute Two
@dataclass
class PandasDataFrame:
      inputdict : dict

      def toPandasDataFrame(self):
            return pd.DataFrame(self.inputdict)


gadget = {
           "Device_Name" : ["Cellphone","Laptop"],
           "Brand_Name"  : ["Apple","Acer"],
           "Price_USD"   : [2400,2800]  }
print(type(gadget))

gadget_df = PandasDataFrame(gadget)
print(type(gadget_df.toPandasDataFrame()))
print(gadget_df.toPandasDataFrame())
```
Outcome
![alt text](image-2.png)


Execute Three

```py
import pandas as pd
from dataclasses import dataclass

#Execute Three
@dataclass
class PandasDataFrame:
      listrows : list
      listheader : list

      def toPandasDataFrame(self):
            return pd.DataFrame(self.listrows, columns = self.listheader)


gadget_rowsList = [
                    ["Laptop","Acer",2800],
                    ["Cellphone","Apple",2400] ]

gadget_dataHeader = ["Device_Name","Brand_Name","Price_USD"]
print(type(gadget_rowsList), type(gadget_dataHeader))

gadget_df = PandasDataFrame(gadget_rowsList,gadget_dataHeader)
print(type(gadget_df.toPandasDataFrame()))
print(gadget_df.toPandasDataFrame())

```
![alt text](image-3.png)