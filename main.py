from machine import Pin, time_pulse_us
import utime

# Constants
SPEED_OF_SOUND_CM_PER_US = 0.0343 / 2  # divide by 2 for round trip
THRESHOLD_CM = 70

# Left Sensor Pins
left_trig = Pin(2, Pin.OUT)
left_echo = Pin(3, Pin.IN)
left_led = Pin(10, Pin.OUT)

# Right Sensor Pins
right_trig = Pin(4, Pin.OUT)
right_echo = Pin(5, Pin.IN)
right_led = Pin(11, Pin.OUT)

def measure_distance(trig, echo):
    trig.low()
    utime.sleep_us(2)
    trig.high()
    utime.sleep_us(10)
    trig.low()
    
    duration = time_pulse_us(echo, 1, 30000)  # timeout 30ms
    if duration < 0:
        return None
    distance = duration * SPEED_OF_SOUND_CM_PER_US
    return distance

while True:
    # Measure left distance
    left_distance = measure_distance(left_trig, left_echo)
    if left_distance is not None and left_distance <= THRESHOLD_CM:
        left_led.high()
        print("Left-side vehicle detected in blind spot")
    else:
        left_led.low()
    
    # Measure right distance
    right_distance = measure_distance(right_trig, right_echo)
    if right_distance is not None and right_distance <= THRESHOLD_CM:
        right_led.high()
        print("Right-side vehicle detected in blind spot")
    else:
        right_led.low()
    
    utime.sleep(0.5)  # small delay to avoid flooding serial output
