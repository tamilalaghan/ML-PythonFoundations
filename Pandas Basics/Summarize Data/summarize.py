# Execute One, Two, Three
# import pandas as pd
# from dataclasses import dataclass

# @dataclass
# class Summarize:
#     filename : str
    
#     def panadasDataFrame(self):
#         return pd.read_csv(self.filename)


# washers = Summarize("washers.csv")
# washers_df = washers.panadasDataFrame()
# print(washers_df.head())

# print(washers_df.info())

# print("********** String Data ***********")
# print(washers_df[['BrandName']].describe())
# print("**********Numeric Data************")
# print(washers_df[['Volume']].describe())


# # Execute Four,Five

# import pandas as pd
# from dataclasses import dataclass

# @dataclass
# class Summarize:
#     filename : str
    
#     def panadasDataFrame(self):
#         return pd.read_csv(self.filename)


# washers = Summarize("washers.csv")
# washers_df = washers.panadasDataFrame()

# # print("********** Value Counts ***********")
# # print(washers_df[['BrandName']].value_counts())

# print("********** Value Counts Percentage ***********")
# print(washers_df[['BrandName']].value_counts(normalize=True))


# # Execute Six

# import pandas as pd
# from dataclasses import dataclass

# @dataclass
# class Summarize:
#     filename : str
    
#     def panadasDataFrame(self):
#         return pd.read_csv(self.filename)


# washers = Summarize("washers.csv")
# washers_df = washers.panadasDataFrame()

# print("********** Mean Overall ***********")
# print(washers_df[['Volume']].mean())

# print("********** Groupby ***********")
# print(washers_df.groupby('BrandName')[['Volume']].mean())

# Execute Seven

import pandas as pd
from dataclasses import dataclass

@dataclass
class Summarize:
    filename : str
    
    def panadasDataFrame(self):
        return pd.read_csv(self.filename)


washers = Summarize("washers.csv")
washers_df = washers.panadasDataFrame()


print("********** Groupby and Agg ***********")
print(washers_df.groupby('BrandName')[['Volume']]
      .agg(['mean','median','min','max']))