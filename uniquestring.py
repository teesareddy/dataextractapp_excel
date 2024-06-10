import pandas as pd

# Load the Excel file
df = pd.read_excel('Skin Care.xlsx')

# Specify the columns from which you want to extract unique strings
columns_to_extract = ['Region', 'Country', 'Subcategory']

# Extract unique strings from specified columns
unique_strings = [df[column].unique() for column in columns_to_extract]

# Create a new DataFrame with the unique strings
output_df = pd.DataFrame(list(zip(*unique_strings)), columns=columns_to_extract)

# Convert the DataFrame to HTML
output_html = output_df.to_html()

# Write the output to a new HTML file
with open('output_file.html', 'w') as file:
    file.write(output_html)