import pandas as pd

# Define the path to your Excel file
excel_file_path = r'C:\Users\master\Desktop\gst.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Define a dictionary of GST rates for each product
gst_rates = {
    'laptop': 18,    # GST rate for laptop
    'mouse': 9,      # GST rate for mouse
    'keyboard': 5    # GST rate for keyboard
}

# Calculate GST for each row based on the product's GST rate
df['GST'] = df.apply(lambda row: (row['MRP'] * row['QTY'] * gst_rates.get(row['ITEM'], 0)) / 100, axis=1)

# Create a Pandas Excel writer using the 'xlsxwriter' engine
output_excel_file = r'C:\Users\master\Desktop\gst_with_calculated.xlsx'
excel_writer = pd.ExcelWriter(output_excel_file, engine='xlsxwriter')

# Write the DataFrame to the Excel file
df.to_excel(excel_writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer to save the file
excel_writer.close()

print(f"GST has been calculated and saved to '{output_excel_file}'.")
