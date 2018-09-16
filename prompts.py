import datetime
import os

class AddEntry:

    def __init__(self):
        pass

    def clear(self):
        """This is a method that clears the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def task_date(self):
        """Takes an input from the user and makes sure its in the write format"""
        while True:
            try:
                task_date = input("What is the date of the task? Please use DD/MM/YYYY: ")
                datetime.datetime.strptime(task_date, '%d/%m/%Y')
                return task_date
            except ValueError:
                self.clear()
                print("Enter the correct format.\n")

    def employee(self):
        """Takes an input from the user and makes sure its in the write format"""
        employee_name = input("Enter your name: ").lower()
        return employee_name

    def task_name(self):
        """Takes a task title from the user"""
        task_name = input("What is the title of the task?: ").lower()
        return task_name

    def time_spent(self):
        """Takes an input from the user, the input can only be numbers"""
        while True:
            try:
                time_spent = int(input("How many minutes did you work on it?: "))
                return time_spent
            except ValueError:
                self.clear()
                print("Please enter the amount of minutes in numbers.\n")

    def notes(self):
        """Takes additional notes from the user as input"""
        notes = input("Do you have any additional notes?: ").lower()
        return notes

