import random
from database import DatabaseManager
import tkinter as tk

class Machine:
    def __init__(self, machine_cost, maintenance_cost, scrap, failure_rate, OutputArea):
        self.machine_cost = machine_cost
        self.maintenance_cost = maintenance_cost
        self.scrap = scrap
        self.failure_rate = failure_rate
        self.OutputArea = OutputArea
        self.maintenance_type = None
        self.db_manager = DatabaseManager()

    def printReport(self, data):
        with open("Machine_Report.txt", "a") as f:
            f.write(data)

    def maintenance(self, years):
        result = "Minimum Retail Price of New Machine: " + str(self.machine_cost) + "\n"
        n = 1
        cumulative_running_cost = 0

        while n <= years:
            cumulative_running_cost += self.maintenance_cost
            net_cost = cumulative_running_cost - self.scrap
            dc = self.machine_cost - self.scrap
            total_operation_cost = dc + cumulative_running_cost
            average_annual_cost = total_operation_cost / n

            random_value = random.random()
            if random_value < self.failure_rate:
                result += "Year " + str(n) + "\n"
                result += "Machine failure\n"

                breakdown = 2 * self.maintenance_cost

                result += "Net Buying Cost of the Machine: " + str(net_cost) + "\n"
                result += "Cost of Fixing the Old machine: " + str(breakdown) + "\n"

                if breakdown >= net_cost:
                    result += "It's more cost-effective to Replace the Machine.\n"
                    result += "REPLACEMENT POLICY INITIATED\n\n"
                    self.maintenance_type = 'Replacement Policy'
                    self.OutputArea.insert(tk.END, result)
                    return
                else:
                    result += "It's not cost-effective to replace the Machine.\n"
                    result += "Repair the Old Machine\n"
                    result += "SUCCESSFULLY INITIATED BREAKDOWN MAINTENANCE\n\n"
                    self.maintenance_type = 'Breakdown Repair'
                    
            elif self.maintenance_cost > self.machine_cost:
                result += "Year " + str(n) + "\n"
                result += "Maintenance cost exceeds Machine Cost!\n"
                result += "Minimum Retail Price of New Machine: " + str(self.machine_cost) + "\n"
                result += "Resale Value: " + str(self.scrap) + "\n"
                result += "Net Buying Cost of the Machine: " + str(net_cost) + "\n"
                self.maintenance_type = 'Reactive Maintenance'
                result += "REACTIVE REPLACEMENT INITIATED\n\n"
                break
            
            else:
                result += "Year " + str(n) + "\n"
                result += "Maintenance Cost " + str(self.maintenance_cost) + "\n"
                result += "Operational Cost " + str(cumulative_running_cost) + "\n"
                result += "Resale Value: " + str(self.scrap) + "\n"
                result += "Depreciation: " + str(dc) + "\n"
                result += "Average Annual Cost: " + str(average_annual_cost) + "\n"
                result += "PREVENTIVE MAINTENANCE SUCCESSFULL\n\n"
                self.maintenance_type = 'Preventive Maintenance'

            self.maintenance_cost *= 1.3
            self.scrap *= 0.8

            n += 1
            self.db_manager.insert_record(n, self.maintenance_cost, self.scrap, cumulative_running_cost, total_operation_cost, average_annual_cost, self.maintenance_type)
            
        self.OutputArea.insert(tk.END, result)
        self.printReport(result)
        self.db_manager.close()

