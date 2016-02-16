import math

w = int(raw_input("Horizontal Pixels: "))
h = int(raw_input("Vertical Pixels: "))
d = float(raw_input("Diagonal Size (inches): "))
p = int(w*h)
mp = float(float(p)/1000000)
ppi = float((math.sqrt(w*w+h*h)/d))
dp = float(w/(math.sqrt(w*w+h*h)/(d*25.4))/w)
print("Pixels Per Inch (PPI): " + str(round(ppi,2)))
print("Dot Pitch: " + str(round(dp,4)) + "mm")
print("Pixels: " + str("{:,}".format(p)) + " (" + str(round(mp,1)) + " MegaPixels)")
if int(ppi) == 120:
    print("This is a LDPI (low pixel density) display.")
if int(ppi) > 120 and int(ppi) <= 160:
    print("This is a MDPI (medium pixel density) display.")
if int(ppi) > 160 and int(ppi) <= 213:
    print("This is a TVDPI (medium high pixel density) display.")
if int(ppi) > 213 and int(ppi) <= 240:
    print("This is a HDPI (high pixel density) display.")
if int(ppi) > 240 and int(ppi) <= 320:
    print("This is a XHDPI (extra high pixel density) display.")
if int(ppi) > 320 and int(ppi) <= 480:
    print("This is a XXHDPI (extra extra high pixel density) display.")
if int(ppi) > 480 and int(ppi) <= 640:
    print("This is a XXXHDPI (extra extra extra high pixel density) display.")
print('Press "Enter" to exit.')
raw_input()
