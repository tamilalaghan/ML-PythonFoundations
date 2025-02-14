
import pandas as pd
from dataclasses import dataclass
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


@dataclass
class VehicleDataFrame:
    inputfilename :str

    def toPandasDataFrame(self):
        return pd.read_csv(self.inputfilename)
    

filename = "vehicles.csv"

vehicle = VehicleDataFrame(filename)
vehicle_df = vehicle.toPandasDataFrame()

print(vehicle_df['co2emissions'].describe())
vehicle_df[['co2emissions']].plot(kind = "hist")
plt.title("Before ZScore Normalization")


vehicle_df_zs = StandardScaler().fit_transform(
    vehicle_df[['co2emissions']])
print("Type :",type(vehicle_df_zs))

#converting to DataFrame
vehicle_df_zs = pd.DataFrame(vehicle_df_zs,
                columns= ['co2emissions'])
print("Type :",type(vehicle_df_zs))
print(vehicle_df_zs.describe())
vehicle_df_zs.plot(kind="hist")
plt.title("After ZScore Normalization")

plt.show()
