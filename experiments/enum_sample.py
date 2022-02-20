# import enum and auto
from enum import Enum, auto
  
# Using enum.auto() method
class language(Enum):
    Java = auto()
    Python = auto()
    HTML = auto()
  
print(list(language))
