# template for "Stopwatch: The Game"
import simplegui

# define global variables

game_time = 0
attempt = 0
wins = 0
running = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t / 600
    b = (t % 600) / 100
    c = (t % 100) / 10
    d = (t % 10)
    disp_time = str(a) + ':' + str(b) + str(c) + '.' + str(d)
    return disp_time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def timer_handler():
    global game_time 
    game_time += 1
    print format(game_time)
    
def start():
    global running
    timer.start()
    running = True
    
def stop():
    global running
    global attempt
    global wins
    if running == True:
        timer.stop()
        running = False
        if game_time % 10 == 0:
            wins += 1
        attempt += 1

def reset():
    global game_time
    global attempt
    global wins
    global running
    timer.stop()
    game_time = 0
    attempt = 0
    wins = 0
    running = False

# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(game_time), (20, 90), 30, "Gray", "sans-serif")
    canvas.draw_text(str(wins) + "/" + str(attempt), (100, 35), 20, "Red", "serif")
    
# create frame
gui = simplegui.create_frame('Stopwatch: The Game', 150, 150)

btn_start = gui.add_button('Start', start, 70)
btn_stop = gui.add_button('Stop', stop, 70)
btn_reset = gui.add_button('Reset', reset, 70)
gui.set_draw_handler(draw_handler)

# register event handlers

    


# start frame
timer.start()
gui.start()

# Please remember to review the grading rubric

#test
#print format(5123)
