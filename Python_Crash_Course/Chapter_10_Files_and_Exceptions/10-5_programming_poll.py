filename = 'programming_poll.txt'

print("Enter 'quit' at any time to exit")

while True:
    reason = input("What do you like about programming?:")
    if reason.lower() == 'quit':
        break
    else:
        with open(f'Python_Crash_Course_MAIN/Python_Crash_Course_Exercises/Python_Crash_Course/txt_files/{filename}', 'a') as file_object:
            file_object.write(f"\n{reason}")

