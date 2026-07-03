from dataclasses import dataclass
from serial import Serial
from time import sleep

@dataclass
class PowerTalkie:

    port: str

    @property
    def _conn(self):
        try:
            return Serial(self.port, 9600, timeout=1)
        finally:
            sleep(2)

    def transmit(self, data:bytes):
        with self._conn as conn:
            conn.write(data)
            print(f"Sent: {data}")
    
    def receive(self):
        with self._conn as conn:
            while True:
                if conn.in_waiting > 0:
                    yield conn.readline().decode('utf-8', errors='ignore').strip()
                sleep(0.1)

