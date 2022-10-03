import ezgraphics as ez
import random
import totalData as td

win = ez.GraphicsWindow(2500, 1400)
canvas = win.canvas()

DictArray = td.arrayOfDicts
print(DictArray)
"""
for i in range(100):
    myDict = {
        "year": 2015,
        "long": random.random() + 91,
        "lat": random.random() + 29,
        "level": round(random.random() + .3),
    }
    otDict = {
        "year": 2016,
        "long": myDict.get("long"),
        "lat": myDict.get("lat"),
        "level": round(random.random() + .3),
    }
    DictArray.append(myDict)
    DictArray.append(otDict)
"""

for x in DictArray:
    for y in DictArray:
        # print(str(x.get("long")) + " " + str(y.get("long")))
        if abs(x.get("lat") - y.get("lat")) < .1 and x.get("year") != y.get("year"):
            if y.get("level") - x.get("level") > 0:
                canvas.setColor("red")
                canvas.drawPoint((abs(y.get("long"))-91)*2500, (y.get("lat")-29)*1400)
            elif y.get("level") - x.get("level") < 0:
                canvas.setColor("green")
                canvas.drawPoint((abs(y.get("long"))-91)*2500, (y.get("lat")-29)*1400)
        # print("Hello")


win.wait()
