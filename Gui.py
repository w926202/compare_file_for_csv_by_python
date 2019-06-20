import tkinter as tk

import CompareRun

root = tk.Tk()
canvas1 = tk.Canvas(root, width=450, height=250)
root.title("CompareRun")
canvas1.pack()

test_case_configs = CompareRun.get_test_case_configs()


def b1_command():
    CompareRun.test_all(test_case_configs)


def b2_command():
    CompareRun.compare_all(test_case_configs)


def b4_command():
    CompareRun.clear_log()


def launch_program():
    button1 = tk.Button(root, text='跑起來', command=b1_command)
    canvas1.create_window(170, 130, window=button1)

    button2 = tk.Button(root, text='比較CrmMemberTier', command=b2_command)
    canvas1.create_window(270, 130, window=button2)

    button4 = tk.Button(root, text='清理', command=b4_command)
    canvas1.create_window(270, 70, window=button4)


if __name__ == '__main__':
    launch_program()

root.mainloop()
