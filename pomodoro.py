import tkinter as tk
from pygame import mixer 

def update_time():
    global stop
    global pause
    global pause_button
    global pause_on
    global work
    global duration
    if duration >= 0:
        minutes = duration // 60
        seconds = duration % 60
        timer_label.config(text=f"Time remaining: {minutes:02d}:{seconds:02d}")
        if pause_on == False:
            pause_button = tk.Button(root, text = "Pause", font = 35, command = pause_pomo)
            pause_button.pack()
            pause_on = True
        if pause == False:
            duration -= 1
            root.after(1000, update_time)
    else:
        if stop == True:
            timer_label.config(text = "Pomodoro has been stopped")    
        else:
            if (work == True):
                duration = break_duration
                work = False
            else:
                duration = work_duration
                work = True
            popup()
            root.after(1000,update_time)
            sound()


def pause_pomo():
    global pause, resume_button, resume_on
    #timer_label.config(text= "Pomodoro has been paused")
    if resume_on == True:
        resume_button.destroy()
    resume_button = tk.Button(root, text = "Resume", font = 35, command = resume_pomo)
    resume_on = True

    resume_button.pack()
    pause = True

def resume_pomo():
    global pause, resume_button
    pause = False
    resume_button.destroy()
    update_time()

def start_pomo():
    global duration, pr_button, pause_button, stop
    #global resume_button
    duration = work_duration
    if (pr_button == True):
        pause_button.destroy()
        #resume_button.destroy()
    update_time()
    pr_button = True
    stop = False
    
def stop_pomo():
    global duration, stop, pause_button, resume_button
    stop = True
    duration = -10
    if (pr_button == True):
        pause_button.destroy()
        resume_button.destroy()
    update_time()

def popup():
    global work
    if work == False:
        tag1 = "Work"
        tag2 = "Break"
    else:
        tag1 = "Break"
        tag2 = "Work"

    pop = tk.Tk()
    pop.title("Notification")
    pop_label = tk.Label(pop, text = f"{tag1} has finsihed \n{tag2} has begun", font = ("Helvetica", 25))
    pop_label.pack()
    pop_button = tk.Button(pop, text = "OK", font = ("Helvetica", 25), command = pop.destroy)
    pop_button.pack()

def sound():
    global work
    mixer.init()

    if work == True:
        link = "/Users/macos/Projects/CE/it's-over-anakin!-i-have-the-high-ground!.wav"
    else:
        link = "/Users/macos/Projects/CE/My_time_has_come.wav"
    mixer.music.load(link)
    mixer.music.set_volume(1.0)
    mixer.music.play()


global pause, pr_button, resume_on, stop, pause_on, work_duration, break_duration
work_duration = int(25 * 60)
break_duration = int(5 * 60)
pause = False
pr_button = False
resume_on = False
stop = False
pause_on = False
work = True
duration = work_duration

root = tk.Tk()
root.title("POMODORO")

start_button = tk.Button(root, text="Start Pomodoro", font=("Helvetica", 14), command=start_pomo)
start_button.pack()
stop_button = tk.Button(root, text="Stop Pomodoro", font=("Helvetica", 14), command = stop_pomo)
stop_button.pack()
dspt_label = tk.Label(root, text="", font =("Helvetica", 15))
dspt_label.pack()

timer_label = tk.Label(root, text="", font=("Helvetica", 20))
timer_label.pack()
if pause == True:
    pause_label = tk.Label(root, text = "", font = ("Helvetica", 20))
    pause_label.pack()

root.mainloop()