# Blindspot-Monitoring-simulation-in-Wokwi

SIMULATION LINK : https://wokwi.com/projects/431805766670650369


Here's a MicroPython program for your Blind Spot Monitoring System using two ultrasonic sensors and two red LEDs, connected to a Raspberry Pi Pico W. This script will:

Continuously check distance from both sensors.
If an object is detected within 70 cm, the respective red LED turns ON.
It prints a message like "Left-side vehicle detected in blind spot" or "Right-side vehicle detected in blind spot" to the serial monitor.
✅ Wiring Reference
Left Sensor (HC-SR04):

Trig → GP2
Echo → GP3
LED (Left Red) → GP10
Right Sensor (HC-SR04):

Trig → GP4
Echo → GP5
LED (Right Red) → GP11
📌 Use 330Ω resistor for each LED. Use voltage divider for Echo pin if needed (HC-SR04 Echo is 5V; Pico W GPIO is 3.3V).
📌 Notes:
You can test it by placing objects within 70 cm of each sensor.
You can increase or decrease THRESHOLD_CM to change sensitivity.
Make sure the ground (GND) is shared between the Pico W and both sensors.
🧠 Microcontroller: Raspberry Pi Pico W

🖱️ Ultrasonic Sensor (HC-SR04) Connections:
🔹 Left Side Sensor:
HC-SR04 Pin	Connects To Pico W	Pin Number
VCC	5V (VBUS)	40
GND	GND	38
Trig	GPIO2	4
Echo	GPIO3	5

🔹 Right Side Sensor:
HC-SR04 Pin	Connects To Pico W	Pin Number
VCC	5V (VBUS)	40 (or use a common 5V line)
GND	GND	38 (or common GND)
Trig	GPIO4	6
Echo	GPIO5	7
⚠️ Echo pin protection: The Echo output is 5V. Use a voltage divider with resistors (1kΩ + 2kΩ recommended) to step down to ~3.3V before connecting to Pico W GPIO pins.
💡 LED Connections:

🔺 Left Red LED:
LED Terminal	Connects To Pico W	Notes
Anode (+)	GPIO10	Use 330Ω resistor
Cathode (-)	GND	Common ground

🔺 Right Red LED:
LED Terminal	Connects To Pico W	Notes
Anode (+)	GPIO11	Use 330Ω resistor
Cathode (-)	GND	Common ground
🔌 Quick Pin Summary

