from enum import Enum
from ynet_report import YnetReport

class Paper(str, Enum):
    ynet = "ynet"
    haaretz = "haaretz"
    israelhayom = "israelhayom"

paper_to_obj = {'ynet': YnetReport}
