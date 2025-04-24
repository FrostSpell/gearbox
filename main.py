import tkinter as tk
import sqlite3

#-----------------------------------------------------------------------------#
# Activities 
#-----------------------------------------------------------------------------#
# Activities: Model ----------------------------------------------------------#
class ActivitiesModel:
    def __init__(self):
        pass  # Por enquanto, não há necessidade de armazenar dados

# Activities: View -----------------------------------------------------------#
class ActivitiesView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.label = tk.Label(root, text="Activities")
        self.label.pack(pady=20)
        self.navigate_button = tk.Button(root, text="Go to Platforms", command=self.controller.show_platforms)
        self.navigate_button.pack(pady=10)

# Activities: Controller -----------------------------------------------------#
class ActivitiesController:
    def __init__(self, root):
        self.root = root
        self.model = ActivitiesModel()
        self.view = ActivitiesView(root, self)

    def show_platforms(self):
        self.view.label.pack_forget()
        self.view.navigate_button.pack_forget()
        self.platform_controller = PlatformController(self.root, self)

    def show_activities(self):
        self.platform_controller.view.hide()
        self.view.label.pack(pady=20)
        self.view.navigate_button.pack(pady=10)

#-----------------------------------------------------------------------------#
# Platform 
#-----------------------------------------------------------------------------#
# Platform: Model ------------------------------------------------------------#
class PlatformModel:
    def __init__(self):
        self.platforms = []
        self.conn = sqlite3.connect('data.db')
        self.create_table()
        self.load_platforms()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS platforms (
                            id INTEGER PRIMARY KEY,
                            short_name TEXT NOT NULL,
                            long_name TEXT NOT NULL,
                            url TEXT NOT NULL)''')
        self.conn.commit()

    def add_platform(self, short_name, long_name, url):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO platforms (short_name, long_name, url) VALUES (?, ?, ?)', (short_name, long_name, url))
        self.conn.commit()
        self.load_platforms()

    def remove_platform(self, short_name):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM platforms WHERE short_name = ?', (short_name,))
        self.conn.commit()
        self.load_platforms()

    def update_platform(self, old_short_name, new_short_name, new_long_name, new_url):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE platforms SET short_name = ?, long_name = ?, url = ? WHERE short_name = ?', (new_short_name, new_long_name, new_url, old_short_name))
        self.conn.commit()
        self.load_platforms()

    def load_platforms(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT short_name, long_name, url FROM platforms')
        self.platforms = [row for row in cursor.fetchall()]

    def get_platforms(self):
        return self.platforms

# Platform: View -------------------------------------------------------------#
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


    def update_platform_list(self, platforms):
        self.platform_listbox.delete(0, tk.END)
        for platform in platforms:
            display_text = f"{platform[0]} - {platform[1]} - {platform[2]}"
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

# Platform: Controller -------------------------------------------------------#
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
            self.model.add_platform(short_name, long_name, url)
            self.view.update_platform_list(self.model.get_platforms())
            self.view.short_name_entry.delete(0, tk.END)
            self.view.long_name_entry.delete(0, tk.END)
            self.view.url_entry.delete(0, tk.END)

    def remove_platform(self):
        selected_platform = self.view.platform_listbox.get(tk.ACTIVE).split(" - ")[0]
        if selected_platform:
            self.model.remove_platform(selected_platform)
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

#-----------------------------------------------------------------------------#
# Main 
#-----------------------------------------------------------------------------#
def main():
    root = tk.Tk()
    root.title("Activities Application")
    root.geometry("1280x720")  # Redimensionando a janela para 1280x720
    app = ActivitiesController(root)  # Página inicial agora é Activities
    root.mainloop()

if __name__ == "__main__":
    main()
