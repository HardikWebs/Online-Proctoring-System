# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2
import dlib


def save(frame, button):
   cv2.imwrite('Candidate.jpg', frame)
   button.config(text='Saved')

# Create an instance of TKinter Window or frame
win = Tk()
detector = dlib.get_frontal_face_detector()

# Set the size of the window
win.geometry('640x585')
win.title('Setup')
# Create a Label to capture the Video frames
image_label = Label(win)
image_label.grid(row=0, column=0)

text_label = Label(win, text='Face the camera!')
text_label.grid(row=1, column=0)

save_button = Button(win, text='Capture', state=DISABLED)
save_button.grid(row=2, column=0)

e = Entry(win, width=50)
e.grid(row=3, column=0)
e.insert(0, 'Enter your name here')

def exit():
    global name
    if e.get() == 'Enter your name here' or e.get() == 'Please enter a valid name':
        e.delete(0, END)
        e.insert(0, 'Please enter a valid name')
        return

    name = e.get()
    win.destroy()

exit_button = Button(win, text='Exit', command=exit)
exit_button.grid(row=4, column=0)

cap = cv2.VideoCapture(0)

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image   
   frame = cap.read()[1]
   gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   saved_frame = frame.copy()
   faces = detector(gray_frame, 1)
   for face in faces:
      x1 = face.left()
      y1 = face.top()
      x2 = face.right()
      y2 = face.bottom()
      cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
   
   if len(faces) == 0:
      text_label.config(text='Face the camera!')
      save_button.config(state=DISABLED)
   
   elif len(faces) == 1:
      text_label.config(text='Great! Now hit "Capture" to save your photo.')
      save_button.config(state=NORMAL, command=lambda: save(saved_frame, save_button))
         
   else:
      text_label.config(text='Only one person allowed!')
      save_button.config(state=DISABLED)
   
   cv2image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   image_label.imgtk = imgtk
   image_label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   image_label.after(20, show_frames)

show_frames()
win.mainloop()

print(name)