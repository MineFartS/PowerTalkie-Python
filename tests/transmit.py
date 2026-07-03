from powertalkie import PowerTalkie

pt1 = PowerTalkie(port="COM3")

pt1.transmit("test123".encode())
