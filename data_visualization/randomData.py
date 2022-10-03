import ezgraphics as ez
import random

x = 1690
y = 570

win = ez.GraphicsWindow(x, y)
canvas = win.canvas()

DictArray = []

for i in range(2000):
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

for s1 in DictArray:
    for s2 in DictArray:
        if s1.get("long") == s2.get("long") and s1.get("lat") == s2.get("lat") and s1.get("year") != s2.get("year"):
            if s2.get("level") - s1.get("level") > 0.1 and \
                    560 < (s1.get("long")-91)*x < 600 and 240 < (s1.get("lat")-29)*y < 300:
                canvas.setColor("red")
                canvas.drawOval((s1.get("long")-91)*x, (s1.get("lat")-29)*y, 5, 5)
                canvas.drawOval((s1.get("long") - 91) * x + 5, (s1.get("lat") - 29) * y + 3, 5, 5)
                canvas.drawOval((s1.get("long") - 91) * x - 2, (s1.get("lat") - 29) * y + 2, 5, 5)
                canvas.drawOval((s1.get("long") - 91) * x - 20, (s1.get("lat") - 29) * y + 2, 5, 5)
                canvas.drawOval((s1.get("long") - 91) * x - 10, (s1.get("lat") - 29) * y + 5, 5, 5)
                canvas.drawOval((s1.get("long") - 91) * x - 2, (s1.get("lat") - 29) * y + 6, 5, 5)
                canvas.drawOval((s1.get("long") - 91) * x - 10, (s1.get("lat") - 29) * y + 20, 5, 5)
                canvas.drawOval((s1.get("long") - 91) * x + 10, (s1.get("lat") - 29) * y + 3, 5, 5)
            elif s2.get("level") - s1.get("level") < -0.1 and \
                (521 < (s1.get("long") - 91) * x < 976 and 223 < (s1.get("lat") - 29) * y < 590):
                canvas.setColor("green")
                canvas.drawOval((s1.get("long")-91)*x, (s1.get("lat")-29)*y, 5, 5)


win.wait()
