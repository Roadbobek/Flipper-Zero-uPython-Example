# uPython siren.py v1.12.0

import flipperzero as f0
import time

def police_siren():
    f0.speaker_stop()
    f0.vibro_set(False)
    
    led_toggle = False
    print("SIREN v1.12.0")

    try:
        while True:
            # --- WAIL MODE ---
            for i in range(0, 20):
                freq = 400 + (i * 45)
                f0.light_set(f0.LIGHT_BACKLIGHT, i * 12)
                
                # Faster flash: Toggles every 2 steps (~140ms)
                # This is the "Middle" speed you requested
                if i % 2 == 0:
                    led_toggle = not led_toggle
                    f0.light_set(f0.LIGHT_RED, 255 if led_toggle else 0)
                    f0.light_set(f0.LIGHT_BLUE, 0 if led_toggle else 255)
                    f0.light_set(f0.LIGHT_GREEN, 0)
                    f0.vibro_set(led_toggle)

                f0.speaker_stop()
                f0.speaker_start(float(freq), 0.8)
                time.sleep_ms(70) 

            for i in range(20, 0, -1):
                freq = 400 + (i * 45)
                f0.light_set(f0.LIGHT_BACKLIGHT, i * 12)
                
                if i % 2 == 0:
                    led_toggle = not led_toggle
                    f0.light_set(f0.LIGHT_RED, 255 if led_toggle else 0)
                    f0.light_set(f0.LIGHT_BLUE, 0 if led_toggle else 255)
                    f0.vibro_set(led_toggle)

                f0.speaker_stop()
                f0.speaker_start(float(freq), 0.8)
                time.sleep_ms(70)

            # --- YELP MODE ---
            for _ in range(12):
                f0.light_set(f0.LIGHT_RED, 255)
                f0.light_set(f0.LIGHT_BLUE, 0)
                f0.light_set(f0.LIGHT_BACKLIGHT, 255)
                f0.canvas_set_color(f0.CANVAS_WHITE)
                f0.canvas_draw_box(0, 0, 128, 64)
                f0.canvas_update()
                
                f0.speaker_stop()
                f0.speaker_start(1400.0, 1.0)
                f0.vibro_set(True)
                time.sleep_ms(45) 
                
                f0.light_set(f0.LIGHT_RED, 0)
                f0.light_set(f0.LIGHT_BLUE, 255)
                f0.light_set(f0.LIGHT_BACKLIGHT, 0)
                f0.canvas_clear()
                f0.canvas_update()
                
                f0.speaker_stop()
                f0.speaker_start(850.0, 1.0)
                f0.vibro_set(False)
                time.sleep_ms(45)

    except Exception as e:
        print("Error:", e)
    finally:
        # Full Hardware Reset
        f0.speaker_stop()
        f0.vibro_set(False)
        f0.light_set(f0.LIGHT_RED, 0)
        f0.light_set(f0.LIGHT_BLUE, 0)
        f0.light_set(f0.LIGHT_GREEN, 0)
        f0.light_set(f0.LIGHT_BACKLIGHT, 127)
        f0.canvas_clear()
        f0.canvas_update()
        print("Siren Stopped.")

if __name__ == "__main__":
    police_siren()