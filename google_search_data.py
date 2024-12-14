import pandas as pd

# Read the Excel file
longest_options = []
shortest_options = []
df = pd.read_excel('google_search_data.xlsx')

for index, row in df.iterrows():
    print(row['longest option'])
    longest_options.append(row['longest option'])

for index, row in df.iterrows():
    print(row['shortest option'])
    shortest_options.append(row['shortest option'])

longest_str = max(longest_options,key=len)
shortest_str = min(shortest_options,key=len)



print(longest_options)

print('longtest string : ' + longest_str)

print(shortest_options)

print('shortest string : ' + shortest_str)



