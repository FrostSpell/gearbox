# Activities: Controller -----------------------------------------------------#
from ActivitiesModel import ActivitiesModel
from ActivitiesView import ActivitiesView
from PlatformController import PlatformController


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