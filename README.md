# Real-Time Proctoring System

A computer vision based proctoring system to monitor the student's face during an online examination by performing face tracking and recognition. Written in Python.

The Python packages necessary to deploy this project include: cv2, tkinter, PIL, dlib and numpy.

To deploy this project run 'final.py' from the 'Final' directory:
```bash
python final.py
```
Upon startup, a window pops up asking the user to click an image to register their face. The image gets saved in a 'Candidate.jpg' file. The proctored window appears subsequently that reports any cases of mismatch.
