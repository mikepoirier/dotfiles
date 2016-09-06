file = open("/sys/class/thermal/thermal_zone0/temp", "r")

temp = float(file.read())

print("{0:.0f}°C".format(temp / 1000))
