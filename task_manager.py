from datetime import date
from datetime import datetime as dt

# Helper functions
def read_txt_file(filename):
    with open(filename, 'r') as file:
        read_lines = file.readlines()
        file.close()

    return read_lines

def write_txt_file_with_line_number(line_no, values):
    lines = read_txt_file('tasks.txt')

    lines[line_no] = values
    with open('tasks.txt', 'w') as file:
        file.writelines(lines)
        file.close()


def set_user_dict(user_file):
    users_dict = {}
    for user in user_file:
        info = user.split(', ')
        # if the line is not last then it has '\n' at the end so removing it and adding to dictionary
        users_dict[info[0]] = info[1].replace("\n", "")
    return users_dict


def set_task_list(task_file):
    tasks_list = []

    count = 0
    for task in task_file:
        info = task.split(', ')
        temp = []
        for i in range(len(info) - 1):
            temp.append(info[i])

        # if the line is not last then it has '\n' at the end so removing it and adding to list
        temp.append(info[-1].replace("\n", ""))
        temp.append(count)
        tasks_list.append(temp)

        count += 1

    return tasks_list


# it will check which user is logging in
def authenticate(users_dict):
    while True:
        username = input("Enter your username: ")
        if username in users_dict.keys():
            while True:
                password = input("Enter your password: ")
                if password == users_dict[username]:
                    print("************Welcome to Task Management Application*************")
                    current_user = username
                    break
                else:
                    print("***Your Password is not right!***")
            break
        else:
            print("***Your username is not right!***")
    return current_user


# Append given text as a new line at the end of file
def append_new_line(file_name, text_to_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


# this helper method is using for editing lines in txt files
def editing_text(mode, values, tasks_list, task, lookup, option):
    # below if to check if the line to change is last or not
    if task[-1] == tasks_list[-1][-1]:
        if mode[0] == 'm':  # this m is for if the editing is to mark if the the task is completed or not
            text_to_write = "" + task[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + task[
                4] + ", " + values[0] + ""
        elif mode[0] == 'u':  # u is for if the task assigned to user has to change
            text_to_write = "" + values[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + task[
                4] + ", " + task[5] + ""
        elif mode[0] == 'd':  # d is for if the due date  of task has to change
            text_to_write = "" + task[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + values[
                0] + ", " + task[5] + ""
        elif mode[0] == 'b':  # b is for if both the assigned username and due date  of task has to change
            text_to_write = "" + values[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + values[
                1] + ", " + task[5] + ""
        write_txt_file_with_line_number(lookup[option], text_to_write)

    else: # if line
        # print("temp=", temp, "task_list=", tasks_list[dict_lookup[option_first]])
        if mode[0] == 'm':
            text_to_write = "" + task[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + task[
                4] + ", " + values[0] + "\n"

        elif mode[0] == 'u':
            text_to_write = "" + values[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + task[
                4] + ", " + task[5] + "\n"

        elif mode[0] == 'd':
            text_to_write = "" + task[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + values[
                0] + ", " + task[5] + "\n"

        elif mode[0] == 'b':
            text_to_write = "" + values[0] + ", " + task[1] + ", " + task[2] + ", " + task[3] + ", " + values[
                1] + ", " + task[5] + "\n"

        if task[-1] == tasks_list[0][-1]:
            # print("first")
            write_txt_file_with_line_number(0, text_to_write)
        else:
            # print("mid")
            write_txt_file_with_line_number(lookup[option], text_to_write)
    return


# this method is to update the lists whenever the menu is opened
def update_data():
    # reading user.txt file
    file_users = read_txt_file('user.txt')
    file_tasks = read_txt_file('tasks.txt')

    # storing user info in dictionary
    users_data = set_user_dict(file_users)
    tasks_data = set_task_list(file_tasks)

    return users_data, tasks_data


# below are functions which are required
def reg_user(user_dict):
    username = input("Enter new username: ")
    while username in user_dict:  # checking if entered username already exists
        print("User name already exits! Try again")
        username = input("Enter new username: ")

    password = input("Enter new password: ")
    confirm_password = input("Enter the password again to confirm: ")

    if password == confirm_password:

        # making a list of info so used for entering value
        whole_info_to_append = [username, password]

        # adding ', ' after every info and calling the function to enter new user in user.txt
        append_new_line('user.txt', ', '.join(whole_info_to_append))

        return "***User registered!!***"

    else:
        return "***User failed to register because passwords were not confirmed***"


def add_task():
    username_for_task = input("Enter the username to whom you want to assign task: ")
    title_of_task = input("Enter the title of task: ")
    desc_of_task = input("Enter the description of task: ")
    due_date = input("Enter the due date(format is dd-mm-yyyy): ")
    today = date.today().strftime("%d-%m-%Y")
    completed_task = input("Enter 'yes' if task is completed otherwise 'no': ")

    # making a list of info so used for entering value
    whole_info_to_append = [username_for_task, title_of_task, desc_of_task, due_date, today, completed_task]

    # adding ', ' after every info and calling the function to enter new task in tasks.txt
    append_new_line('tasks.txt', ', '.join(whole_info_to_append))

    return "***Task added successfully!***"


def view_all(tasks_list):
    for task in tasks_list:
        print("Assigned to: ", task[0], ", Title: ", task[1], ", Description: ", task[2],
              ", Due date: ", task[3], ", Assigned Date: ", task[4], ", Completed: ", task[5])


def view_mine(tasks_list, current_user):
    count = 1
    # to help to get the task number according to main list value, key will be main value from list and value will be
    # the number of task showed to user
    dict_lookup = {}
    for task in tasks_list:
        if task[0] == current_user:
            dict_lookup[count] = task[-1]
            print("Task number: ", count, ", Assigned to: ", task[0], ", Title: ", task[1], ", Description: ", task[2],
                  ", Due date: ", task[3], ", Assigned Date: ", task[4], ", Completed: ", task[5])
            # print("dictionary=", dict_lookup)
            count += 1

    option_first = int(input("Please select the task number or enter -1 to return to menu: "))
    if option_first == -1:
        return
    elif count >= option_first > 0:
        option_second = input("Enter 'm' for marking the task or 'e' for editing the task: ")

        if option_second == 'm':
            mark = input("Please enter 'yes' if task is completed or 'no': ")
            temp = tasks_list[dict_lookup[option_first]]
            editing_text(mode='m', values=[mark], tasks_list=tasks_list, task=temp, lookup=dict_lookup,
                         option=option_first)

        elif option_second == 'e':
            option_third = input("Whether you want to change the username 'u' or due date 'd' or both 'b': ")
            if option_third == 'u':
                username = input("Please enter the username to shift task: ")
                temp = tasks_list[dict_lookup[option_first]]
                editing_text(mode='u', values=[username], tasks_list=tasks_list, task=temp, lookup=dict_lookup,
                             option=option_first)
            elif option_third == 'd':
                due_date = input("Please enter the due date(dd-mm-yyyy): ")
                temp = tasks_list[dict_lookup[option_first]]
                editing_text(mode='d', values=[due_date], tasks_list=tasks_list, task=temp, lookup=dict_lookup,
                             option=option_first)
            elif option_third == 'b':
                username = input("Please enter the username to shift task: ")
                due_date = input("Please enter the due date(dd-mm-yyyy): ")
                temp = tasks_list[dict_lookup[option_first]]
                editing_text(mode='b', values=[username, due_date], tasks_list=tasks_list, task=temp,
                             lookup=dict_lookup, option=option_first)


def show_stats():
    try:
        print("***Task overview***")
        with open('task_overview.txt', 'r') as task_overview:
            for line in task_overview.readlines():
                print(line.replace("\n", ""))
    except FileNotFoundError:
        print("task_overview.txt is not accessible/available")
    finally:
        task_overview.close()

    try:
        print("***User overview***")
        with open('user_overview.txt', 'r') as user_overview:
            for line in user_overview.readlines():
                print(line.replace("\n", ""))
    except FileNotFoundError:
        print("user_overview.txt is not accessible/available")
    finally:
        user_overview.close()

    return


def generate_reports(users_list, tasks_list):
    today = dt.strptime(date.today().strftime("%d-%m-%Y"), "%d-%m-%Y")
    with open('task_overview.txt', 'w+') as task_overview:
        tasks_generated = str(len(tasks_list))
        completed_tasks = 0
        uncompleted_tasks = 0
        uncompleted_and_overdue = 0

        for task in tasks_list:
            if task[5] == 'yes':
                completed_tasks += 1
            else:
                uncompleted_tasks += 1

            if task[5] == 'no' and dt.strptime(task[3], "%d-%m-%Y") < today:
                uncompleted_and_overdue += 1

        percentage_uncompleted = round((uncompleted_tasks / len(tasks_list)) * 100, 2)
        percentage_overdue = round((uncompleted_and_overdue / len(tasks_list)) * 100, 2)
        tasks_text_lines = [f"The total number of tasks that have been generated: {tasks_generated} \n",
                            f"The total number of completed task: {completed_tasks} \n",
                            f"The total number of uncompleted tasks: {uncompleted_tasks} \n",
                            f"The total number of uncompleted tasks and overdue: {uncompleted_and_overdue} \n",
                            f"The percentage of tasks that are incomplete: {percentage_uncompleted} \n",
                            f"The percentage of tasks that are overdue: {percentage_overdue}"]

        task_overview.writelines(tasks_text_lines)
        task_overview.close()
    with open('user_overview.txt', 'w+') as user_overview:
        registered_users = len(users_list)

        users_text_lines = [f"The total number of registered users: {registered_users} \n",
                            f"The total number of tasks that have been generated: {tasks_generated} \n"]
        for key in users_list.keys():
            tasks_assigned = 0
            tasks_assigned_completed = 0
            tasks_assigned_uncompleted = 0
            tasks_assigned_uncompleted_overdue = 0
            for task in tasks_list:
                if task[0] == key:
                    tasks_assigned += 1
                if task[0] == key and task[5] == 'yes':
                    tasks_assigned_completed += 1
                if task[0] == key and task[5] == 'no':
                    tasks_assigned_uncompleted += 1
                if task[0] == key and task[5] == 'no' and dt.strptime(task[3], "%d-%m-%Y") < today:
                    tasks_assigned_uncompleted_overdue += 1

            if tasks_assigned > 0:
                percentage_tasks_assigned = round((tasks_assigned / len(tasks_list) * 100), 2)
                percentage_tasks_assigned_completed = round((tasks_assigned_completed / tasks_assigned * 100), 2)
                percentage_tasks_assigned_uncompleted = round((tasks_assigned_uncompleted / tasks_assigned * 100), 2)
                tasks_assigned_uncompleted_overdue = round(
                    (tasks_assigned_uncompleted_overdue / tasks_assigned * 100), 2)
            else:
                percentage_tasks_assigned = 0
                percentage_tasks_assigned_completed = 0
                percentage_tasks_assigned_uncompleted = 0
                tasks_assigned_uncompleted_overdue = 0

            string_user = f"The user: {key} \n"
            string_assigned = f"The percentage of total number of tasks assigned: {percentage_tasks_assigned} \n"
            string_completed = f"The percentage of total number of tasks completed: " \
                               f"{percentage_tasks_assigned_completed} \n"
            string_uncompleted = f"The percentage of total number of tasks uncompleted: " \
                                 f"{percentage_tasks_assigned_uncompleted} \n"
            string_uncompleted_overdue = f"The percentage of total number of tasks uncompleted and overdue: " \
                                         f"{tasks_assigned_uncompleted_overdue} \n"
            string_line = "----" * 5 + "\n"

            users_text_lines.append(string_user)
            users_text_lines.append(string_assigned)
            users_text_lines.append(string_completed)
            users_text_lines.append(string_uncompleted)
            users_text_lines.append(string_uncompleted_overdue)
            users_text_lines.append(string_line)

        user_overview.writelines(users_text_lines)
        user_overview.close()
    return


if __name__ == "__main__":
    users, tasks = update_data()

    current_logged_in = authenticate(users)

    admin_choice = ""

    while True:
        users, tasks = update_data()
        print("""
You are logged in as '""" + current_logged_in + """'
Please select one of the following options:

r - register user
a - add task
va - view all tasks
vm - view my tasks""")

        if current_logged_in == 'admin':
            print("ds - show statistics")
            print("gn - generate reports")
        admin_choice = input("""
e - exit

Enter your choice: """)

        if admin_choice == 'r':
            if current_logged_in == 'admin':
                print(reg_user(users))
            else:
                print("***You cannot register user because you are not admin!!!***")
        elif admin_choice == 'a':
            print(add_task())

        elif admin_choice == 'va':
            if len(tasks) > 0:
                print("Here are all the tasks: ")
                view_all(tasks)
            else:
                print("***There is no task available!***")

        elif admin_choice == 'vm':
            print("Here are all your tasks: ")
            view_mine(tasks, current_logged_in)

        elif admin_choice == 'ds':
            if current_logged_in == 'admin':
                show_stats()
            else:
                print("***You cannot perform this command because you are not admin!!!***")

        elif admin_choice == 'gn':
            if current_logged_in == 'admin':
                generate_reports(users, tasks)
            else:
                print("***You cannot perform this command because you are not admin!!!***")

        elif admin_choice == 'e':
            break
        else:
            print("***You have not entered a right command. Please choose from the above commands***")

    print("***Ending program GoodBye!!!***")