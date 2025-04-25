# Platform: View -------------------------------------------------------------#
from Platform import Platform


import tkinter as tk


class PlatformView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Create a container frame for horizontal layout
        self.field_frame = tk.Frame(root)
        self.field_frame.pack(pady=10)

        # Short Name field
        self.short_name_entry = tk.Entry(self.field_frame)
        self.short_name_entry.pack(side=tk.LEFT, padx=5)
        self.short_name_entry.insert(0, "Short Name")

        # Long Name field
        self.long_name_entry = tk.Entry(self.field_frame)
        self.long_name_entry.pack(side=tk.LEFT, padx=5)
        self.long_name_entry.insert(0, "Long Name")

        # URL field
        self.url_entry = tk.Entry(self.field_frame)
        self.url_entry.pack(side=tk.LEFT, padx=5)
        self.url_entry.insert(0, "URL")

        # Add button
        self.add_button = tk.Button(self.field_frame, text="Add Platform", command=self.controller.add_platform)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Remove button (will stay below as per original code)
        self.remove_button = tk.Button(root, text="Remove Selected Platform", command=self.controller.remove_platform)
        self.remove_button.pack()

        self.edit_button = tk.Button(root, text="Edit Selected Platform", command=self.controller.edit_platform)
        self.edit_button.pack()
        self.platform_listbox = tk.Listbox(root)
        self.platform_listbox.pack()
        self.back_button = tk.Button(root, text="Back", command=self.controller.show_activities)
        self.back_button.pack(pady=10)


    def update_platform_list(self, platforms: Platform):
        self.platform_listbox.delete(0, tk.END)
        for platform in platforms:
            display_text = f"{platform.id} - {platform.name} - {platform.long_name} - {platform.url}"
            self.platform_listbox.insert(tk.END, display_text)

    def hide(self):
        self.short_name_entry.pack_forget()
        self.long_name_entry.pack_forget()
        self.url_entry.pack_forget()
        self.add_button.pack_forget()
        self.remove_button.pack_forget()
        self.edit_button.pack_forget()
        self.platform_listbox.pack_forget()
        self.back_button.pack_forget()