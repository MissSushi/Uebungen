unkomprimiert = ["A","A","A","A","A","8","8","8","9","9","9","9","9","9","9","9","9","9","8"]
komprimiert = ["%","5","A","8","8","8","%","10","9","8"]

"""
laenge(String[]) = len(list)
add(String[], String) = list.append(String)
toString(Integer) = str(Integer)
"""

def erstelleKomprimierung(unkomprimiert):
    komprimiert = []
    count = 1
    for i in range(1, len(unkomprimiert)):
        if unkomprimiert[i] != unkomprimiert[i-1]:
            print(komprimiert)
erstelleKomprimierung(["A","A","A","A","A","8","8","8","9","9","9","9","9","9","9","9","9","9","8"])

