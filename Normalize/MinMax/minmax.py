
import pandas as pd
from dataclasses import dataclass
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


@dataclass
class VehicleDataFrame:
    inputfilename :str

    def toPandasDataFrame(self):
        return pd.read_csv(self.inputfilename)
    

filename = "vehicles.csv"

vehicle = VehicleDataFrame(filename)
vehicle_df = vehicle.toPandasDataFrame()

print(vehicle_df['co2emissions'].describe())
vehicle_df[['co2emissions']].plot(kind = "hist",
                                 figsize= (4, 3))
plt.title("Before MinMax Normalization")


vehicle_df_mm = MinMaxScaler().fit_transform(
    vehicle_df[['co2emissions']])
print("Type :",type(vehicle_df_mm))

#converting to DataFrame
vehicle_df_mm = pd.DataFrame(vehicle_df_mm,
                columns= ['co2emissions'])
print("Type :",type(vehicle_df_mm))
print(vehicle_df_mm.describe())
vehicle_df_mm.plot(kind="hist",
                   figsize= (4, 3))
plt.title("After MinMax Normalization")

plt.show()
