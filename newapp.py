import pandas as pd

# Read the Excel file
df = pd.read_excel('Skin Care.xlsx')

# Specify the columns to extract unique strings from
columns = ['Region', 'Country', 'Subcategory']

# Get unique strings from the specified columns
unique_strings = []
for column in columns:
    unique_strings.extend(df[column].unique())

# Generate the HTML file
html = '<html>\n'
html += '<head>\n'
html += '<style>\n'
html += 'label { display: block; }\n'
html += '</style>\n'
html += '</head>\n'
html += '<body>\n'
for column in columns:
    html += '<h2>' + column + '</h2>\n'
    for string in df[column].unique():
        html += '<label><input type="checkbox" name="' + column + '" value="' + string + '"> ' + string + '</label>\n'
html += '<button onclick="getSelectedRows()">Proceed</button>\n'
html += '<table id="outputTable">\n'
html += '<thead>\n'
html += '<tr>\n'
for column in columns:
    html += '<th>' + column + '</th>\n'
html += '</tr>\n'
html += '</thead>\n'
html += '<tbody></tbody>\n'
html += '</table>\n'
html += '<script>\n'
html += 'function getSelectedRows() {\n'
html += '    var selectedRows = [];\n'
html += '    var checkboxes = document.querySelectorAll("input[type=checkbox]:checked");\n'
html += '    for (var i = 0; i < checkboxes.length; i++) {\n'
html += '        var column = checkboxes[i].name;\n'
html += '        var value = checkboxes[i].value;\n'
html += '        selectedRows.push({ column: column, value: value });\n'
html += '    }\n'
html += '    var table = document.getElementById("outputTable");\n'
html += '    var tbody = table.getElementsByTagName("tbody")[0];\n'
html += '    tbody.innerHTML = "";\n'
html += '    for (var i = 0; i < selectedRows.length; i++) {\n'
html += '        var row = tbody.insertRow();\n'
html += '        for (var j = 0; j < columns.length; j++) {\n'
html += '            var cell = row.insertCell();\n'
html += '            cell.innerHTML = selectedRows[i].value;\n'
html += '        }\n'
html += '    }\n'
html += '}\n'
html += '</script>\n'
html += '</body>\n'
html += '</html>'

# Save the HTML file
with open('output.html', 'w') as file:
    file.write(html)
