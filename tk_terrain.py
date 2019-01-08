import random
import time
import tkinter as tk
from noise import RandomNoise


"""
CANVAS EXAMPLE
"""
def render(smoothing_passes, LAND=False):
    p = smoothing_passes
    colours = random_noise_obj.smoothNoise2d(smoothing_passes=p)

    # Gen hexadeciamal color code if LAND is set. Else, grey scale is used.
    for x in range(0, len(colours)):
        for y in range(0, len(colours[x])):
            col = int(colours[x][y] * 255)
            if LAND:
                if col in range(0,int(255 * water_amount)): # Water
                    final = f'#0000{col:02X}'
                elif col in range(int(255 * (water_amount)), int(255 * (water_amount+sand_amount))): # Sand
                    final = f'#{col:02X}{col:02X}00'
                elif col in range(int(255 * (water_amount+sand_amount)), int(255 * (water_amount+sand_amount+land_amount))): # Land
                    final = f'#00{col:02X}00'
                elif col in range(int(255 * (water_amount+sand_amount+land_amount)), 255): # Mountain
                    final = f'#{col:02X}{col:02X}{col:02X}'
                else:
                    final = f'#{col:02X}{col:02X}{col:02X}'
            else:
                final = f'#{col:02X}{col:02X}{col:02X}'

            canvas.create_rectangle(x*sq, y*sq, (x*sq)+sq, (y*sq)+sq,
            fill=final, width=0, tags=(f'RCT{p}'))

        root.update()
        canvas.delete(f'RCT{p-2}')

# Tk code
root = tk.Tk()
w = int(root.winfo_screenwidth() // 1.5)
h = int(root.winfo_screenheight() // 1.5)
sq = 10
FPS = 60
color = True
smoothing_passes = 30

random_noise_obj = RandomNoise(w//sq, h//sq, 255, smoothing_passes)
random_noise_obj.randomize()

canvas = tk.Canvas(root, height=h, width=w, bg='black', highlightthickness=0)
canvas.pack()

smoothingl = tk.Label(root, text=f'Size: {w//sq}x{h//sq} | Smoothing pass: 0/{smoothing_passes}')
smoothingl.pack()

# Fraction of 1.0
# These values determine the amount of each element in the render
water_amount = 0.46
sand_amount = 0.007
land_amount = 0.44

# DEBUG
print('water_range', 0,int(255*water_amount))
print('sand_range', int(255*(water_amount)), int(255*(water_amount+sand_amount)))
print('land_range', int(255*(water_amount+sand_amount)), int(255*(water_amount+sand_amount+land_amount)))
print('mountain_range', int(255*(water_amount+sand_amount+land_amount)), 255)

step = 1
for p in range(0, smoothing_passes, 1):
    render(p, color)
    smoothingl.config(text=f'Size: {w//sq}x{h//sq} | Smoothing pass: {p+1}/{smoothing_passes}')
    time.sleep(1/FPS)

root.mainloop()
