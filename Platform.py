#-----------------------------------------------------------------------------#
# Platform 
#-----------------------------------------------------------------------------#
# Platform: Schema -----------------------------------------------------------#
class Platform:
    def __init__(self, id: int, name: str, long_name: str, url:str):
        self.id: int         = id
        self.name: str       = name
        self.long_name: str  = long_name
        self.url: str        = url

    def __str__(self):
        return f"Plataform #{self.id}: {self.name} ({self.long_name})"
