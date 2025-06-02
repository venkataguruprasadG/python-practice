import random
from dataclasses import dataclass

# Define a simple class to simulate IoT protocol security features
@dataclass
class IoTProtocol:
    name: str
    encryption: bool
    authentication: str
    lightweight: bool
    secure_join: bool
    integrity_check: bool

    def security_score(self):
        score = 0
        score += 1 if self.encryption else 0
        score += 1 if self.authentication in ["Basic", "Cert", "Token", "PSK", "DevKey", "LinkKey"] else 0
        score += 1 if self.lightweight else 0
        score += 1 if self.secure_join else 0
        score += 1 if self.integrity_check else 0
        return score

# Define various protocols
protocols = [
    IoTProtocol("MQTT", encryption=True, authentication="Basic", lightweight=True, secure_join=False, integrity_check=False),
    IoTProtocol("CoAP", encryption=True, authentication="PSK", lightweight=True, secure_join=True, integrity_check=True),
    IoTProtocol("Zigbee", encryption=True, authentication="LinkKey", lightweight=True, secure_join=False, integrity_check=True),
    IoTProtocol("LoRaWAN", encryption=True, authentication="DevKey", lightweight=True, secure_join=True, integrity_check=True),
    IoTProtocol("BLE", encryption=True, authentication="JustWorks", lightweight=True, secure_join=False, integrity_check=False),
    IoTProtocol("HTTPS", encryption=True, authentication="Cert", lightweight=False, secure_join=True, integrity_check=True)
]

# Evaluate and rank protocols
ranked_protocols = sorted(protocols, key=lambda x: x.security_score(), reverse=True)

# Print the analysis
print(f"{'Protocol':<10} | {'Enc':<3} | {'Auth':<10} | {'Lite':<5} | {'Join':<5} | {'Integrity':<9} | {'Score'}")
print("-" * 70)
for p in ranked_protocols:
    print(f"{p.name:<10} | {str(p.encryption):<3} | {p.authentication:<10} | {str(p.lightweight):<5} | "
          f"{str(p.secure_join):<5} | {str(p.integrity_check):<9} | {p.security_score()}")
