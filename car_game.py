instruct = ""
cur_state = "stop" 
prev_state = ""

while True:
    print("""
\nCAR GAME
--------\n
Start   : To Start the car
Stop    : To Stop the car
Right   : To turn the car to Right
Left    : To turn the car to Left
Drift   : Drift the car
Exit    : To Quit the Game
    """)
    prev_state = instruct

    instruct = input("What command needs to be sent to the car: ").lower()
    if instruct == "start":
        if cur_state == "stop":
            cur_state = "start"
            print("\nCar Started ...")
        elif cur_state == "start" or cur_state == "drift" or cur_state == "right" or cur_state == "left":
            print("\nCar is already running ...")
    elif instruct == "stop":
        if cur_state == "start" or cur_state == "drift" or cur_state == "right" or cur_state == "left":
            cur_state = "stop"
            print("\nCar Stopped ...")
        elif cur_state == "stop":
            print("\nCar is already stopped ...")
    elif instruct == "right":
        if cur_state == "stop":
            print("\nCar is Stopped, can't turn")
        else:
            print("\nCar turned Right ...")
    elif instruct == "left":
        if cur_state == "stop":
            print("\nCar is Stopped, can't turn")
        else:
            print("\nCar turned Left ...")
    elif instruct == "drift":
        if cur_state == "stop":
            print("\nCar is Stopped, can't Drift")
        else:
            print("\nCar Drifted ...")
    elif instruct == "exit":
        break
    else:
        print("\nIncorrect Instruction ...")
