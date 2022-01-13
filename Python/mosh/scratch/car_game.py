# python 3.7.1
def car_game():
    started = False
    while True:
        command = input("> ")
        if command == "start":
            if started:
                print("car has already started")
            else:
                print("car has started")
                started = True
        elif command == "stop":
            if not started:
                print("car has already stopped")
            else:
                print("car has stopped")
                started = False
        elif command == "help":
            print('''start - to start the car
    stop - to stop the car
    quit - to quit''')
        elif command == "quit":
            break
        else:
            print("sorry can't understand your command")
