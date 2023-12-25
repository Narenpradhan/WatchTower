import pandas as pd
import json
from datetime import datetime

# Load the JSON files into pandas DataFrames
df1 = pd.read_json('first.json')
df2 = pd.read_json('second.json')
df3 = pd.read_json('third.json')

# Concatenate the DataFrames vertically
combined_df = pd.concat([df1, df2, df3])

# Convert the 'Timestamp' column to datetime format
combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'], unit='s')

# Sort the combined DataFrame based on the 'Timestamp' column in descending order
sorted_combined_df = combined_df.sort_values(by='Timestamp', ascending=False)

# Convert the 'Timestamp' column to the desired format
sorted_combined_df['Timestamp'] = sorted_combined_df['Timestamp'].apply(lambda x: x.strftime("%b %d, %Y"))

# Resetting the index after sorting
sorted_combined_df = sorted_combined_df.reset_index(drop=True)

# Print or save the sorted DataFrame
print(sorted_combined_df)

# Save the sorted DataFrame to a new JSON file without escaping forward slashes
with open('sorted_combined_data.json', 'w') as json_file:
    json_file.write(json.dumps(sorted_combined_df.to_dict(orient='records'), indent=4, default=str))
