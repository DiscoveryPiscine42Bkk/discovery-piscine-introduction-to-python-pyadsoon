while True:
    user_input = input("Say something (type 'stop' to exit): ")
  
    if user_input.upper() == "STOP":
        print("Stopping the program.")
        break

  print(F"I got that: {user_input}")
