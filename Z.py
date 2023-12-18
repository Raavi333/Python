import tkinter as tk
from tkinter import simpledialog, filedialog
import csv
from influxdb_client import InfluxDBClient, Point, WritePrecision
import datetime

def get_file_path():
    return filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

def get_input(prompt):
    value = simpledialog.askfloat("Input", prompt)
    if value is None:
        return None
    return value

def calculate_z():
    # Ask for the file path
    file_path = get_file_path()
    if not file_path:
        result_label.config(text="Calculation canceled.")
        return

    # Input values for variables
    a = get_input("Enter the value of a")
    if a is None:
        result_label.config(text="Calculation canceled.")
        return

    b = get_input("Enter the value of b")
    if b is None:
        result_label.config(text="Calculation canceled.")
        return

    c = get_input("Enter the value of c")
    if c is None:
        result_label.config(text="Calculation canceled.")
        return

        
    d = get_input("Enter the value of d")
    if d is None:
        result_label.config(text="Calculation canceled.")
        return

    e = get_input("Enter the value of e")
    if e is None:
        result_label.config(text="Calculation canceled.")
        return

    f = get_input("Enter the value of f")
    if f is None:
        result_label.config(text="Calculation canceled.")
        return

    g = get_input("Enter the value of g")
    if g is None:
        result_label.config(text="Calculation canceled.")
        return

    h = get_input("Enter the value of h")
    if h is None:
        result_label.config(text="Calculation canceled.")
        return
    
    i = get_input("Enter the value of i")
    if i is None:
        result_label.config(text="Calculation canceled.")
        return
    
    j = get_input("Enter the value of j")
    if j is None:
        result_label.config(text="Calculation canceled.")
        return
    
    k = get_input("Enter the value of k")
    if k is None:
        result_label.config(text="Calculation canceled.")
        return
    
    l = get_input("Enter the value of l")
    if l is None:
        result_label.config(text="Calculation canceled.")
        return
    
    m = get_input("Enter the value of m")
    if m is None:
        result_label.config(text="Calculation canceled.")
        return
    
    n = get_input("Enter the value of n")
    if n is None:
        result_label.config(text="Calculation canceled.")
        return
    
    o = get_input("Enter the value of o")
    if o is None:
        result_label.config(text="Calculation canceled.")
        return
    
    p = get_input("Enter the value of p")
    if p is None:
        result_label.config(text="Calculation canceled.")
        return
    
    q = get_input("Enter the value of q")
    if l is None:
        result_label.config(text="Calculation canceled.")
        return
    

    # Check for cancel option in the middle of input
    if result_label.cget("text") == "Calculation canceled.":
        return

    # Calculate the value of z
    z = (a * b * c) + (d * e * f) / g + (h + i) * (j / k) + l * m * n + (o + p) * q

    # Display the result
    result_label.config(text=f"The value of z is: {z}")

    # Save the time and file location to a separate file
    save_metadata(file_path)

    # Export result to CSV
    export_to_csv(file_path, z)

    # Export result to InfluxDB
    export_to_influxdb(z)

def save_metadata(file_path):
    metadata_file = "metadata.txt"
    with open(metadata_file, "a") as f:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Script executed at: {current_time}\n")
        f.write(f"File location: {file_path}\n")
        f.write("-" * 30 + "\n")

def export_to_csv(file_path, result):
    try:
        # Check if the file already exists
        with open(file_path, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Result'])
            writer.writerow([result])
    except FileExistsError:
        result_label.config(text="File already exists. Please choose a different file.")
    except PermissionError:
        result_label.config(text="Permission denied. Please choose a different file.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def export_to_influxdb(result):
    token = "your_influxdb_token"
    org = "your_influxdb_organization"
    bucket = "your_influxdb_bucket"

    client = InfluxDBClient(url="http://localhost:8086", token=token)

    write_api = client.write_api(write_options=WritePrecision.S)

    current_time = datetime.datetime.utcnow()

    point = Point("z_measurement").field("z_value", result).time(current_time)

    try:
        write_api.write(bucket=bucket, org=org, record=point)
        result_label.config(text="Result exported to InfluxDB successfully.")
    except Exception as e:
        result_label.config(text=f"Error exporting to InfluxDB: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Z Calculator")

# Create a button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate Z", command=calculate_z)
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
