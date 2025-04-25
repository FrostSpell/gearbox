# Platform: Controller -------------------------------------------------------#
from PlatformModel import PlatformModel
from PlatformView import PlatformView


import tkinter as tk


class PlatformController:
    def __init__(self, root, activities_controller):
        self.root = root
        self.activities_controller = activities_controller
        self.model = PlatformModel()
        self.view = PlatformView(root, self)
        self.view.update_platform_list(self.model.get_platforms())

    def add_platform(self):
        short_name = self.view.short_name_entry.get()
        long_name = self.view.long_name_entry.get()
        url = self.view.url_entry.get()
        if short_name and long_name and url:
            self.model.create_platform(short_name, long_name, url)
            self.view.update_platform_list(self.model.get_platforms())
            self.view.short_name_entry.delete(0, tk.END)
            self.view.long_name_entry.delete(0, tk.END)
            self.view.url_entry.delete(0, tk.END)

    def remove_platform(self):
        selected_platform = self.view.platform_listbox.get(tk.ACTIVE).split(" - ")[0]
        if selected_platform:
            self.model.delete_platform(selected_platform)
            self.view.update_platform_list(self.model.get_platforms())

    def edit_platform(self):
        selected_platform = self.view.platform_listbox.get(tk.ACTIVE).split(" - ")[0]
        new_short_name = self.view.short_name_entry.get()
        new_long_name = self.view.long_name_entry.get()
        new_url = self.view.url_entry.get()
        if selected_platform and new_short_name and new_long_name and new_url:
            self.model.update_platform(selected_platform, new_short_name, new_long_name, new_url)
            self.view.update_platform_list(self.model.get_platforms())
            self.view.short_name_entry.delete(0, tk.END)
            self.view.long_name_entry.delete(0, tk.END)
            self.view.url_entry.delete(0, tk.END)

    def show_activities(self):
        self.view.hide()
        self.activities_controller.show_activities()