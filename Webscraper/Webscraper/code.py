import pandas as pd

# Load the CSV files into pandas DataFrames
df1 = pd.read_csv('WatchTower/Webscraper/Webscraper/first.csv')
df2 = pd.read_csv('WatchTower/Webscraper/Webscraper/second.csv')
df3 = pd.read_csv('WatchTower/Webscraper/Webscraper/third.csv')

# Concatenate the DataFrames vertically
combined_df = pd.concat([df1, df2, df3])

# Sort the combined DataFrame based on the values in the third column
sorted_combined_df = combined_df.sort_values(by='Timestamp', ascending=False)

# Print or save the sorted DataFrame
print(sorted_combined_df)

# Save the sorted DataFrame to a new CSV file
sorted_combined_df.to_csv('sorted_combined_data.csv', index=False)




# import pandas as pd

# # Sample DataFrames
# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                     'B': ['B0', 'B1', 'B2'],
#                     'C': ['C0', 'C1', 'C2']})

# df2 = pd.DataFrame({'A': ['A0', 'A3', 'A4'],
#                     'B': ['B0', 'B4', 'B5'],
#                     'C': ['C0', 'C4', 'C5']})

# # Concatenate along rows (vertically)
# result_vertical = pd.concat([df1, df2], ignore_index=True)

# # Drop duplicates based on columns 'A', 'B', and 'C'
# result_vertical_no_duplicates = result_vertical.drop_duplicates(subset=['A', 'B', 'C'])

# # Concatenate along columns (horizontally)

# result_horizontal = pd.concat([df1, df2], axis=1)

# # Print the results
# print("Concatenation along rows (vertically):\n", result_vertical_no_duplicates)
# print("\nConcatenation along columns (horizontally):\n", result_horizontal)
