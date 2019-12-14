#!/usr/bin/python
import sys 
import socket
import math
from Tkinter import *

# Client Parameters
HEIGHT, WIDTH = 500, 800   # Canvas Dimensions
MARGIN = 20                # Margins round the axes.
SCALE = 3                  # Scale = 3 pixels per meter.
ballRadius = 5             # Ball radius in pixels.

MODE_FREEZE = 1 
MODE_RUN = 5 

# Variable and Callback for the Fire Button
fireCommand = False
def cannonFire():
    global fireCommand
    fireCommand = True

# Process the command line arguments.
if ( len(sys.argv) == 2) :
    trick_varserver_port = int(sys.argv[1])
else :
    print( "Usage: vsclient <port_number>")
    sys.exit()

# Create a Canvas to draw on.
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("CannonBall Display")
canvas.pack()

# Add a FIRE button
buttonFrame = Frame()
buttonFrame.pack(side=BOTTOM)
fireButton = Button(buttonFrame,text="fire",command=cannonFire)
fireButton.pack(side=LEFT)

# Add an Initial Speed Scale
speedScale = Scale(buttonFrame, from_=5, to=50, label="Initial Speed", orient=HORIZONTAL)
speedScale.pack(side=LEFT)
speedScale.set(50)

# Add an Initial Angle Scale
angleScale = Scale(buttonFrame, from_=5, to=80, label="Initial Angle", orient=HORIZONTAL)
angleScale.pack(side=LEFT)
angleScale.set(30)

# Create coordinate axes on the canvas.
xAxis = canvas.create_line(MARGIN,HEIGHT-MARGIN,WIDTH,HEIGHT-MARGIN)
yAxis = canvas.create_line(MARGIN,HEIGHT-MARGIN,MARGIN,0)

# Create an oval object to represent the cannonball.
cannonBall = canvas.create_oval(0,0,ballRadius,ballRadius, fill="orange")

# Create a text field on the canvas for the simulation mode display.
modeText = canvas.create_text(WIDTH/2, 20, text="--unknown-mode--")

impactTimeText = canvas.create_text(WIDTH/2, 40, text="")
impactPosText =  canvas.create_text(WIDTH/2, 60, text="")

# Connect to the variable server.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect( ("localhost", trick_varserver_port) )
insock = client_socket.makefile("r")

# Request the cannon ball position.
client_socket.send( "trick.var_set_client_tag(\"myvsclient\") \n")
client_socket.send( "trick.var_debug(3)\n" )
client_socket.send( "trick.var_pause()\n" )
client_socket.send( "trick.var_ascii()\n" )
client_socket.send( "trick.var_add(\"dyn.cannon.pos[0]\") \n" +
                    "trick.var_add(\"dyn.cannon.pos[1]\") \n" +
                    "trick.var_add(\"trick_sys.sched.mode\")\n" +
                    "trick.var_add(\"dyn.cannon.impact\") \n" +
                    "trick.var_add(\"dyn.cannon.impactTime\") \n" )
client_socket.send( "trick.var_unpause()\n" )

# Repeatedly read and process the responses from the variable server.
while(True):
    line = insock.readline()
    if line == '':
        break

    # Split the response line into value fields.
    field = line.split("\t")

    # Update Ball Position
    x,y = float(field[1]), float(field[2])
    cx,cy = (x*SCALE+MARGIN), (HEIGHT-y*SCALE-MARGIN)
    canvas.coords(cannonBall,cx-ballRadius,cy-ballRadius,cx+ballRadius,cy+ballRadius)

    # Update Sim Mode
    simMode = int(field[3])
    if simMode == MODE_FREEZE:
        canvas.itemconfigure(modeText, fill="blue", text="FREEZE")
    elif simMode == MODE_RUN:
        canvas.itemconfigure(modeText, fill="red", text="RUN")
    else:
        canvas.itemconfigure(modeText, text="--unknown-mode--")

    impact = int(field[4])
    if simMode == MODE_RUN:
        if impact:
            canvas.itemconfigure(impactTimeText, text="Impact time = " + field[5])
            canvas.itemconfigure(impactPosText, text="Impact pos  = (" + field[1] + "," + field[2] + ")")
            client_socket.send( "trick.exec_freeze()\n")

    # Command the sim from Freeze to Run, when the "Fire" button is pressed.
    if simMode == MODE_FREEZE:
        if fireCommand:
            fireCommand = False
            fireButton.config(state=DISABLED)
            client_socket.send( "dyn.cannon.init_speed = " + str(speedScale.get()) + " \n")
            client_socket.send( "dyn.cannon.init_angle = " + str(angleScale.get()*(math.pi/180.0)) + " \n")
            client_socket.send( "trick.cannon_init( dyn.cannon )\n")
            client_socket.send( "trick.exec_run()\n")

    tk.update()

# Keep the window open, when the data stops.
tk.mainloop()


