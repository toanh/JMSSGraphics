from JMSSGraphics import *

jmss = Graphics(640, 640, "Image", fps = 60)

input_file = open("image.csv", "r")
data = []
for line in input_file:
    data.append(int(line)/255.0)

i = 0

@jmss.mainloop
def Draw():
    global i
    jmss.drawRawPixels(data, 0, 0, 640, 640)


jmss.run()

input_file.close()
