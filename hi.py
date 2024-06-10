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
output_html = output_df.to_html(index=False, escape=False, formatters={
    'Region': lambda x: f'<input type="checkbox" id="region_{x}">{x}',
    'Country': lambda x: f'<input type="checkbox" id="country_{x}">{x}',
    'Subcategory': lambda x: f'<input type="checkbox" id="subcategory_{x}">{x}'
})

# Add the HTML structure
html_content = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Skin Care Data</title>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
    </style>
</head>
<body>
    {output_html}
    <br>
    <button onclick="generateOutput()">Proceed</button>
    <div id="output"></div>

    <script>
        function generateOutput() {{
            var selectedRegions = [];
            var selectedCountries = [];
            var selectedSubcategories = [];

            // Get the selected checkboxes
            var regionCheckboxes = document.querySelectorAll('input[id^="region_"]');
            var countryCheckboxes = document.querySelectorAll('input[id^="country_"]');
            var subcategoryCheckboxes = document.querySelectorAll('input[id^="subcategory_"]');

            // Collect the selected values
            regionCheckboxes.forEach(function(checkbox) {{
                if (checkbox.checked) {{
                    selectedRegions.push(checkbox.id.split('_')[1]);
                }}
            }});
            countryCheckboxes.forEach(function(checkbox) {{
                if (checkbox.checked) {{
                    selectedCountries.push(checkbox.id.split('_')[1]);
                }}
            }});
            subcategoryCheckboxes.forEach(function(checkbox) {{
                if (checkbox.checked) {{
                    selectedSubcategories.push(checkbox.id.split('_')[1]);
                }}
            }});

            // Filter the main DataFrame based on selected values
            var filteredData = df[(df['Region'].isin(selectedRegions)) &
                                  (df['Country'].isin(selectedCountries)) &
                                  (df['Subcategory'].isin(selectedSubcategories))];

            // Save the filtered data to an Excel file
            filteredData.to_excel('output_file.xlsx', index=False);
        }}
    </script>
</body>
</html>
'''

# Write the HTML content to a file
with open('output_file.html', 'w') as file:
    file.write(html_content)