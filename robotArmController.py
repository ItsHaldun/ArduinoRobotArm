from serialArduino import serialArduino
from time import sleep
import tkinter as tk

servoAngles = [90,90,90,90]

def testCode():
  try:
    while True:
      serArduino.write('<90,90,90,90>')
      sleep(3)
      serArduino.write('<0,90,90,90>')
      sleep(3)
      serArduino.write('<90,90,90,90>')
      sleep(3)
      serArduino.write('<180,90,90,90>')
      sleep(3)
  except KeyboardInterrupt:
    pass

  
if __name__ == "__main__":
  serArduino = serialArduino()
  serArduino.initialize(serArduino.available_ports[-1].device, 38400)
  
  def setValueB(value):
    servoAngles[0] = int(value)
    serArduino.write(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    print(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    sleep(0.05)
  def setValueL(value):
    servoAngles[1] = int(value)
    serArduino.write(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    print(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    sleep(0.05)
  def setValueR(value):
    servoAngles[2] = int(value)
    serArduino.write(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    print(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    sleep(0.05)
  def ToggleClaw():
    if servoAngles[3] == 90:
      servoAngles[3] = 0
    else:
      servoAngles[3] = 90
    serArduino.write(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    print(f"<{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]}>")
    sleep(0.05)
  
  
  window = tk.Tk()
  b = tk.Scale(window, from_=0, to=180, command=setValueB)
  b.set(90)
  b.pack()
  l = tk.Scale(window, from_=45, to=135, command=setValueL)
  l.set(90)
  l.pack()
  r = tk.Scale(window, from_=45, to=135, command=setValueR)
  r.set(90)
  r.pack()
  c = tk.Button(window, text ="Claw", command = ToggleClaw)
  c.pack()
  
  window.mainloop()
  
  serArduino.close()