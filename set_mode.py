def is_manual_mode():
    manual_mode_flag = False
    print("\n")
    manual_mode_flag = input("Run in automated or manual mode (a/m)")
    if (manual_mode_flag == "m"):
        print("\n")
        print("manual mode set")
        manual_mode_flag = True
    else :
        print("automatic mode set")
    return manual_mode_flag

def manual_mode_instructions(command, tool):
    print("\n")
    user_answer = input(f"Do you want to run {tool} with the following flags? : {command}\nor a customize it (y/else)\n\n")
    if (user_answer.lower() == 'y'):
        custom_flags = input()
        return custom_flags