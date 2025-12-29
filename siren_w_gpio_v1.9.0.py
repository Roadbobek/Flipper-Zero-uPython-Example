# uPython siren_with_gpio.py v1.9.0

# Wiring !!!

#  Red LED (+)	    (RESISTOR)     Pin 15 (C0)	      GPIO_PIN_PC0
#  Blue LED (+)	    (RESISTOR)     Pin 16 (C1)	      GPIO_PIN_PC1
#  Both LEDs (-)                   Pin ANY (GND)	  Ground

# Always use a small resistor with LEDs to prevent them from
# burning out or drawing too much current from your Flipper!

# I recomend using a 220 Ohm resistor with the red LED,
# and a 110 Ohm resistor with the blue LED.

# But if you want to play it safe but get them very bright, use these standard resistor values:
# For the RED LED: Use a 150 Ohm or 220 Ohm resistor.
# For the BLUE LED: Use a 47 Ohm or 100 Ohm resistor.

# If the resistors become quiet warm then it's not enough resistance, go up.

# DO NOT GO UNDER THESE VALUES!


import flipperzero as f0
import time

print("Starting Siren...")

def police_siren():
    # GPIO LED PIN CONFIGURATIOM
    RED_PIN = f0.GPIO_PIN_PC0   # Pin 15 (C1)
    BLUE_PIN = f0.GPIO_PIN_PC1  # Pin 16 (C0)
    
    f0.gpio_init_pin(RED_PIN, f0.GPIO_MODE_OUTPUT_PUSH_PULL)
    f0.gpio_init_pin(BLUE_PIN, f0.GPIO_MODE_OUTPUT_PUSH_PULL)
    
    f0.speaker_stop()
    led_toggle = False
    print("Siren Started...")


    while True:
        # --- WAIL MODE ---
        for i in range(0, 20):
            freq = 400 + (i * 45)
            
            if i % 2 == 0:
                led_toggle = not led_toggle
                f0.light_set(f0.LIGHT_RED, 255 if led_toggle else 0)
                f0.light_set(f0.LIGHT_BLUE, 0 if led_toggle else 255)
                
                # VERIFIED GPIO SET FUNCTION
                f0.gpio_set_pin(RED_PIN, led_toggle)
                f0.gpio_set_pin(BLUE_PIN, not led_toggle)
            
            f0.speaker_stop()
            # Use float() just to be safe with speaker_start
            f0.speaker_start(float(freq), 0.8)
            time.sleep_ms(70) 

        # --- YELP MODE ---
        for _ in range(12):
            f0.light_set(f0.LIGHT_RED, 255)
            f0.light_set(f0.LIGHT_BLUE, 0)
            f0.gpio_set_pin(RED_PIN, True)
            f0.gpio_set_pin(BLUE_PIN, False)
            
            f0.speaker_stop()
            f0.speaker_start(1400.0, 1.0)
            time.sleep_ms(45) 
            
            f0.light_set(f0.LIGHT_RED, 0)
            f0.light_set(f0.LIGHT_BLUE, 255)
            f0.gpio_set_pin(RED_PIN, False)
            f0.gpio_set_pin(BLUE_PIN, True)
            
            f0.speaker_stop()
            f0.speaker_start(850.0, 1.0)
            time.sleep_ms(45)

    # Full Cleanup
    f0.speaker_stop()
    f0.gpio_set_pin(RED_PIN, False)
    f0.gpio_set_pin(BLUE_PIN, False)
    f0.light_set(f0.LIGHT_RED, 0)
    f0.light_set(f0.LIGHT_BLUE, 0)
    # VERIFIED DEINIT FUNCTION
    f0.gpio_deinit_pin(RED_PIN)
    f0.gpio_deinit_pin(BLUE_PIN)
    print("Cleanup Done.")

if __name__ == "__main__":
    police_siren()