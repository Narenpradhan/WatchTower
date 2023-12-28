import pandas as pd
import json
from datetime import datetime

#load the JSON files into pandas DataFrames
df1 = pd.read_json('first.json')
df2 = pd.read_json('second.json')
df3 = pd.read_json('third.json')

#concatenate the DataFrames vertically
combined_df = pd.concat([df1, df2, df3])

#convert the 'Timestamp' column to datetime objects
combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'], format='%b %d, %Y')

# Sort the combined DataFrame based on the 'Timestamp' column using sorted()
sorted_combined_df = pd.DataFrame(sorted(combined_df.to_dict(orient='records'), key=lambda x: x['Timestamp'], reverse=True))

#convert the datetime object into strings
sorted_combined_df['Timestamp'] = sorted_combined_df['Timestamp'].dt.strftime('%b %d, %Y')

#resetting the index after sorting
sorted_combined_df = sorted_combined_df.reset_index(drop=True)

# Print or save the sorted DataFrame
print(sorted_combined_df)

#save the sorted DataFrame to a new JSON file
with open('combined_data.json', 'w') as json_file:
    json_file.write(json.dumps(sorted_combined_df.to_dict(orient='records'), indent=4, default=str))
