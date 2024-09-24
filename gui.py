import tkinter as tk
from tkinter import messagebox, scrolledtext
from main import Machine

def simulate():
    try:
        machine_cost = float(cost_of_machine_entry.get())  
        maintenance_cost = float(maintenance_cost_entry.get())
        scrap = float(scrap_entry.get())
        failure_rate = float(failure_rate_entry.get())
        years = int(years_entry.get())

        if machine_cost <= 0 or maintenance_cost <= 0 or scrap < 0 or failure_rate < 0 or failure_rate > 1 or years <= 0:
            raise ValueError

        OutputArea.delete(1.0, tk.END)
        mach = Machine(machine_cost, maintenance_cost, scrap, failure_rate, OutputArea)
        report_data = mach.maintenance(years)
        
        if generate_report_var.get():
            mach.printReport(report_data)
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values and ensure all values are positive.")

root = tk.Tk()
root.title("Maintenance Simulator")

input_frame = tk.Frame(root, width=800, height=600)
input_frame.pack()

tk.Label(input_frame, text="Cost of Machine:").grid(column=0, row=0, sticky="w", pady=5)
cost_of_machine_entry = tk.Entry(input_frame, width=20)
cost_of_machine_entry.grid(column=1, row=0, padx=5, pady=5)

tk.Label(input_frame, text="Maintenance Cost:").grid(column=0, row=1, sticky="w", pady=5)
maintenance_cost_entry = tk.Entry(input_frame, width=20)
maintenance_cost_entry.grid(column=1, row=1, padx=5, pady=5)

tk.Label(input_frame, text="Scrap/Resale Value:").grid(column=0, row=2, sticky="w", pady=5)
scrap_entry = tk.Entry(input_frame, width=20)
scrap_entry.grid(column=1, row=2, padx=5, pady=5)

tk.Label(input_frame, text="Failure Rate (0-1):").grid(column=0, row=3, sticky="w", pady=5)
failure_rate_entry = tk.Entry(input_frame, width=20)
failure_rate_entry.grid(column=1, row=3, padx=5, pady=5)

tk.Label(input_frame, text="Number of Years:").grid(column=0, row=4, sticky="w", pady=5)
years_entry = tk.Entry(input_frame, width=20)
years_entry.grid(column=1, row=4, padx=5, pady=5)

generate_report_var = tk.BooleanVar()
generate_report_checkbox = tk.Checkbutton(input_frame, text="Generate Report", variable=generate_report_var)
generate_report_checkbox.grid(column=0, row=5, columnspan=2, pady=5)

OutputArea = scrolledtext.ScrolledText(root, width=60, height=15)
OutputArea.pack(padx=10, pady=10)

simulate_button = tk.Button(root, text="Simulate", command=simulate)
simulate_button.pack(pady=10)

root.mainloop()
