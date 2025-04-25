#-----------------------------------------------------------------------------#
# Platform 
#-----------------------------------------------------------------------------#
# Platform: Schema -----------------------------------------------------------#
class Platform:
    def __init__(self, id, name, long_name, url):
        self.id         = id
        self.name       = name
        self.long_name  = long_name
        self.url        = url

    def __str__(self):
        return f"Plataform #{self.id}: {self.name} ({self.long_name})"
