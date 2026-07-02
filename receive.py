import serial
import time

PORT_PT2 = 'COM4' # Update with PT2's port
BAUD_RATE = 9600

def listen_for_traffic():
    try:
        # Open the receiver's serial port
        pt2 = serial.Serial(PORT_PT2, BAUD_RATE, timeout=1)
        print("Listening for incoming traffic on PT2...")
        
        while True:
            # Poll the serial buffer
            if pt2.in_waiting > 0:
                raw_data = pt2.readline()
                
                # Decode bytes to string
                decoded_msg = raw_data.decode('utf-8', errors='ignore').strip()
                
                if decoded_msg:
                    print(f"Decoded Payload: {decoded_msg}")
                    # You can add logic here to process, save, or forward decoded_msg
            
            time.sleep(0.1) # Prevent CPU overload
            
    except KeyboardInterrupt:
        print("Stopped listening.")
    except Exception as e:
        print(f"Reception error: {e}")

# Example execution
if __name__ == "__main__":
    listen_for_traffic()
