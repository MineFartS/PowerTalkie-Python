import serial
import time

# Update with your specific COM port or /dev interface
PORT_PT1 = 'COM3' 
BAUD_RATE = 9600

def send_payload(payload):
    try:
        # Open the virtual serial port
        pt1 = serial.Serial(PORT_PT1, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for radio wake/stabilization
        
        # Send raw byte stream to PT1
        # (Assuming custom framing if required by the device, otherwise raw bytes)
        pt1.write(payload.encode('utf-8'))
        print(f"Sent to PT1: {payload}")
        
        pt1.close()
    except Exception as e:
        print(f"Transmission error: {e}")

# Example execution
if __name__ == "__main__":
    test_traffic = "PC1_MSG: Hello from the other side!"
    send_payload(test_traffic)
