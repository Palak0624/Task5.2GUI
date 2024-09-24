import tkinter as tk
from gpiozero import PWMLED

led1 = PWMLED(27)  
led2 = PWMLED(22)  
led3 = PWMLED(17)   

def reset():
    led1.value = 0
    led2.value = 0
    led3.value = 0

reset()

def adjust(led, value):
    brightness = int(value) / 100  
    if led == 1:
        led1.value = brightness
    elif led == 2:
        led2.value = brightness
    elif led == 3:
        led3.value = brightness


def quit_led():
    reset()
    root.quit()


root = tk.Tk()
root.title("LED Intensity PWM ")

tk.Label(root, text="Green LED ").pack()
slider1 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda v: adjust(1, v))
slider1.pack()

tk.Label(root, text="Red LED ").pack()
slider2 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda v: adjust(2, v))
slider2.pack()

tk.Label(root, text="White LED ").pack()
slider3 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda v: adjust(3, v))
slider3.pack()


exit_button = tk.Button(root, text="Exit", command=quit_led)
exit_button.pack()

root.mainloop()
