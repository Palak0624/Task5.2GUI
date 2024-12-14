import tkinter as tk  # Importing tkinter for GUI
from gpiozero import PWMLED  # Importing PWMLED from gpiozero library to control LEDs

# Initializing PWM-controlled LEDs on GPIO pins 27, 22, and 17
led1 = PWMLED(27)  
led2 = PWMLED(22)  
led3 = PWMLED(17)   

# Function to reset the LEDs (turns them off)
def reset():
    led1.value = 0  # Turn off LED1 (Green)
    led2.value = 0  # Turn off LED2 (Red)
    led3.value = 0  # Turn off LED3 (White)

reset()  # Call the reset function to ensure LEDs are off at the start

# Function to adjust the brightness of the LEDs based on the slider values
def adjust(led, value):
    brightness = int(value) / 100  
    if led == 1:
        led1.value = brightness 
    elif led == 2:
        led2.value = brightness  
    elif led == 3:
        led3.value = brightness  

# Function to reset LEDs and quit the application
def quit_led():
    reset()  # Reset LEDs to off
    root.quit()  # Close the GUI window

# Create the Tkinter window for the GUI
root = tk.Tk()
root.title("LED Intensity PWM ")  # Set the title of the window

# Create and pack a label and slider for the Green LED
tk.Label(root, text="Green LED ").pack()
slider1 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda v: adjust(1, v)) 
slider1.pack()

# Create and pack a label and slider for the Red LED
tk.Label(root, text="Red LED ").pack()
slider2 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda v: adjust(2, v)) 
slider2.pack()

# Create and pack a label and slider for the White LED
tk.Label(root, text="White LED ").pack()
slider3 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda v: adjust(3, v))  
slider3.pack()

# Create and pack an Exit button that calls quit_led when clicked
exit_button = tk.Button(root, text="Exit", command=quit_led) 
exit_button.pack()

# Start the Tkinter event loop 
root.mainloop()
