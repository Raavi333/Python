import tkinter as tk
from tkinter import simpledialog, filedialog
import pandas as pd
import csv
from influxdb_client import InfluxDBClient, Point, WritePrecision
import datetime

def get_file_path():
    return filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])

def get_selected_columns(columns):
    selected_columns = simpledialog.askstring("Select Columns", "Enter column names separated by commas:")
    if selected_columns:
        return [col.strip() for col in selected_columns.split(',')]
    else:
        return columns

def calculate_z_from_excel(file_path, selected_columns):
    try:
        # Read Excel file using pandas
        df = pd.read_excel(file_path)

        # Collect values for selected columns
        variable_values = {column: df[column].tolist() for column in selected_columns}

        # Example calculation using the original formula
        z_values = [(variable_values['a'][i] * variable_values['b'][i] * variable_values['c'][i] +
                     variable_values['d'][i] * variable_values['e'][i] * variable_values['f'][i] / variable_values['g'][i] +
                     (variable_values['h'][i] + variable_values['i'][i]) * variable_values['j'][i] / variable_values['k'][i] +
                     variable_values['l'][i] * variable_values['m'][i] * variable_values['n'][i] +
                     (variable_values['o'][i] + variable_values['p'][i]) * variable_values['q'][i])
                    for i in range(len(df))]

        # Display the result or save it to a new Excel file
        result_label.config(text=f"The calculated values of z are: {z_values}")
    except Exception as e:
        result_label.config(text=f"Error reading Excel file: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Z Calculator")

def browse_excel_file():
    file_path = get_file_path()
    if file_path:
        selected_columns = get_selected_columns(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'])
        calculate_z_from_excel(file_path, selected_columns)

# Create a button to trigger browsing for an Excel file
browse_button = tk.Button(root, text="Browse Excel File", command=browse_excel_file)
browse_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
