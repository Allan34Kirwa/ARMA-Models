from ARMAModels.library import wrangle
from ARMAModels.connect import nairobi

# Use my wrangle function to read the data from the nairobi collection into the Series y.
y = wrangle(nairobi, resample_rule="1H")
y.head()
