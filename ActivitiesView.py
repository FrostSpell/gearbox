# Activities: View -----------------------------------------------------------#
import tkinter as tk


class ActivitiesView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.label = tk.Label(root, text="Activities")
        self.label.pack(pady=20)
        self.navigate_button = tk.Button(root, text="Go to Platforms", command=self.controller.show_platforms)
        self.navigate_button.pack(pady=10)