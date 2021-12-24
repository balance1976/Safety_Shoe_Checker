import os

np = os.path.dirname(__file__)
def writescan(code):
    with open(np + "\\scannedbadges.txt",'a') as of:
        of.write("\n")
        of.write(code)
