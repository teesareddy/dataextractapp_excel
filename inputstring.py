import pandas as pd

# Load the Excel file
df = pd.read_excel('Skin Care.xlsx')

# Specify the columns from which you want to extract unique strings
columns_to_extract = ['Region', 'Country', 'Subcategory']

# Extract unique strings from specified columns
unique_strings = [df[column].unique() for column in columns_to_extract]

# Create a new DataFrame with the unique strings
output_df = pd.DataFrame(list(zip(*unique_strings)), columns=columns_to_extract)

# Save the unique strings to an Excel file
output_df.to_excel('unique_strings.xlsx', index=False)

# Get user input for selected strings
selected_regions = input("Enter selected regions (comma-separated): ").split(',')
selected_countries = input("Enter selected countries (comma-separated): ").split(',')
selected_subcategories = input("Enter selected subcategories (comma-separated): ").split(',')

# Filter the main DataFrame based on selected values
filtered_data = df[(df['Region'].isin(selected_regions)) &
                   (df['Country'].isin(selected_countries)) &
                   (df['Subcategory'].isin(selected_subcategories))]

# Save the filtered data to an Excel file
filtered_data.to_excel('output_file.xlsx', index=False)