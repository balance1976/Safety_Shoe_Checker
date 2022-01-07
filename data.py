import os
from datetime import datetime

np = os.path.dirname(__file__)

dt1 = datetime.now()
dt2 = dt1.strftime("%m/%d/%Y")



def writescan(code):
    barandtime = "Badge# " + code + ", Date: " + str(dt2)
    with open(np + "\\scannedbadges.txt",'a') as of:
        of.write("\n")
        of.write(barandtime)
        print(barandtime,"added")
