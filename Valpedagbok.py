import tkinter as tk
root.protocol("WM_DELETE_WINDOW", root.destroy)


class Puppy:
    def __init__(self, name, weight, date):
        self.name = name
        self.weight = weight
        self.date = date

class PuppyTracker:
    def __init__(self):
        self.puppies = []

    def add_puppy(self):
        name = self.name_entry.get()
        weight = self.weight_entry.get()
        date = self.date_entry.get()
        puppy = Puppy(name, weight, date)
        self.puppies.append(puppy)

    def create_widgets(self):
        # Name entry
        name_label = tk.Label(text="Navn:")
        name_label.grid(column=0, row=0)
        self.name_entry = tk.Entry()
        self.name_entry.grid(column=1, row=0)

        # Weight entry
        weight_label = tk.Label(text="Vekt (gram):")
        weight_label.grid(column=0, row=1)
        self.weight_entry = tk.Entry()
        self.weight_entry.grid(column=1, row=1)

        # Date entry
        date_label = tk.Label(text="Dato:")
        date_label.grid(column=0, row=2)
        self.date_entry = tk.Entry()
        self.date_entry.grid(column=1, row=2)

        # Add button
        add_button = tk.Button(text="Legg til", command=self.add_puppy)
        add_button.grid(column=0, row=3)

        # View button
        view_button = tk.Button(text="Vis valper", command=self.view_puppies)
        view_button.grid(column=0, row=4)

    def view_puppies(self):
        window = tk.Toplevel()
        window.title("Oversikt over valper")
        
        for puppy in self.puppies:
            label = tk.Label(window, text=f"{puppy.name} ({puppy.weight} gram) - {puppy.date}")
            label.pack()

    def save_data(self):
      with open('puppy_data.txt', 'w') as f:
          for puppy in self.puppies:
              f.write(f"{puppy.name},{puppy.weight},{puppy.date}\n")

    def load_data(self):
      try:
          with open('puppy_data.txt', 'r') as f:
              for line in f.readlines():
                  name, weight, date = line.strip().split(',')
                  puppy = Puppy(name, weight, date)
                  self.puppies.append(puppy)
      except FileNotFoundError:
          pass

    def run(self):
        window = tk.Tk()
        window.title("Valpesporing")
        
        self.create_widgets()

        # Load data from file if it exists
        self.load_data()

        # Save data when the window is closed
        window.protocol("WM_DELETE_WINDOW", self.save_data)
        
        window.mainloop()

tracker = PuppyTracker()
tracker.run()

