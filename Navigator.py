"""
Daily Coding Challenge: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-28
"""
def navigate(commands):
    history = ["Home"]
    i = 0
    back = 0
    forward = 0
    for command in commands:
        if "Visit" in command:
            history.append(command[6:])
            i += 1
            forward += 1
        elif command == "Back":
            if forward:
                i -= 1
                forward -= 1
                back += 1
        elif command == "Forward":
            if back:
                i += 1
                forward += 1
                back -= 1
    return history[i]
