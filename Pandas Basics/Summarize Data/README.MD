Execute One

```py
import pandas as pd
from dataclasses import dataclass

@dataclass
class Summarize:
    filename : str
    
    def panadasDataFrame(self):
        return pd.read_csv(self.filename)


washers = Summarize("washers.csv")
washers_df = washers.panadasDataFrame()
print(washers_df.head())

```

Outcome
![alt text](image.png)

Execute Two

```py
import pandas as pd
from dataclasses import dataclass

@dataclass
class Summarize:
    filename : str
    
    def panadasDataFrame(self):
        return pd.read_csv(self.filename)


washers = Summarize("washers.csv")
washers_df = washers.panadasDataFrame()
#print(washers_df.head())
print(washers_df.info())
```

Outcome
![alt text](image-1.png)

Execute Three

```py
import pandas as pd
from dataclasses import dataclass

@dataclass
class Summarize:
    filename : str
    
    def panadasDataFrame(self):
        return pd.read_csv(self.filename)


washers = Summarize("washers.csv")
washers_df = washers.panadasDataFrame()
# print(washers_df.head())
# print(washers_df.info())
print("********** String Data ***********")
print(washers_df[['BrandName']].describe())
print("**********Numeric Data************")
print(washers_df[['Volume']].describe())
```

Outcome
![alt text](image-3.png)

Execute Four

```py
# Execute Four

import pandas as pd
from dataclasses import dataclass

@dataclass
class Summarize:
    filename : str
    
    def panadasDataFrame(self):
        return pd.read_csv(self.filename)


washers = Summarize("washers.csv")
washers_df = washers.panadasDataFrame()

print("********** Value Counts ***********")
print(washers_df[['BrandName']].value_counts())

```
Outcome
![alt text](image-4.png)