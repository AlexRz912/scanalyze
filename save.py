import os

user_answer = input("Do you want to save 2xx, 3xx and 4xx status codes into different files? (y/n): ")

def save_in_diff_files(status):
    if (status == "2[0-9][0-9]") :
        file_status = "2xx"
    elif (status == "3[0-9][0-9]") :
        file_status = "3xx"
    else :
        file_status = "4xx"
    
    command = f"cat live_domains | grep '{status}' | anew status_{file_status}"
    os.system(command)

if user_answer.lower() == "y":
    save_in_diff_files("2[0-9][0-9]")  
    save_in_diff_files("3[0-9][0-9]")  
    save_in_diff_files("4[0-9][0-9]")
