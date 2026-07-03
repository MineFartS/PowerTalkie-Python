from . import PowerTalkie

pt2 = PowerTalkie(port="COM4")

for data in pt2.receive():
    print(f"Received: {data}")
