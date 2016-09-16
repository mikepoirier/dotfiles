file = open("/sys/class/thermal/thermal_zone0/temp", "r")

temp = float(file.read())

celsius = temp / 1000
fahrenheit = celsius * (9/5) + 32

print("{0:.0f}°C({1:.0f}°F)".format(celsius, fahrenheit))
