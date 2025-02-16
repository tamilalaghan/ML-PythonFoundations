Execution 

```py
import pandas as pd
from dataclasses import dataclass
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

@dataclass
class BikesDataFrame:
    inputfilename :str

    def toPandasDataFrame(self):
        return pd.read_csv(self.inputfilename)
    

filename = "bikes.csv"

bike_rental = BikesDataFrame(filename)
bike_rental_df = bike_rental.toPandasDataFrame()

# Print Data Frames ( Info )
print ( bike_rental_df.info() )

```

Outcome
Print the DataFrame Info
![alt text](image.png)

```py
import pandas as pd
from dataclasses import dataclass
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

@dataclass
class BikesDataFrame:
    inputfilename :str

    def toPandasDataFrame(self):
        return pd.read_csv(self.inputfilename)
    

filename = "bikes.csv"

bike_rental = BikesDataFrame(filename)
bike_rental_df = bike_rental.toPandasDataFrame()

# Print Data Frames ( Info )
print ( bike_rental_df.info() )

# Print Data Frame Description
print( bike_rental_df.describe() )

```

Print the DataFrame Description
![alt text](image-1.png)