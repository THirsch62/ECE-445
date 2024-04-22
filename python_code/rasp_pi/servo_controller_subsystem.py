import time
from utils import *

# dictionary with folding patterns
folding_pattern = {
    "T-shirt/Top": [[1, 4], [3, 6], [2], [5]],
    "Trouser": [[1, 4], [3, 6], [2], [5]],
    "Pullover": [[1, 4], [3, 6], [2], [5]]
}

# TODO
def main(clothing_item):
    for panels in folding_pattern[clothing_item]:
        fold(panels)
