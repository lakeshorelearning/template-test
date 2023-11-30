import os
from log import logger

class Configuration:

    def __init__(self) -> None:
        
        for name, value in os.environ.items():
            if "CONFIG_" in name:
                setattr(self, name.replace("CONFIG_", "").lower(),value)
        
            