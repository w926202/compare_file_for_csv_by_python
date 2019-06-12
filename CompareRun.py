import csv, difflib, os, subprocess, sys
import tkinter as tk

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 450, height = 250) 
root.title("CompareRun")
canvas1.pack()


def launch_program(): 
       button1 = tk.Button (root, text='跑起來',command=echo_bat_file)
       canvas1.create_window(170, 130, window=button1)
    
       button2 = tk.Button (root, text='比較CrmMemberTier',command=CMT)
       canvas1.create_window(270, 130, window=button2)

       button3 = tk.Button (root, text='比較CrmMemberTierSummary',command=CMTS)
       canvas1.create_window(270, 170, window=button3)

       button4 = tk.Button (root, text='清理', command=clear_log)
       canvas1.create_window(270, 70, window=button4)


def echo_bat_file():
      subprocess.call([r'C:\Users\Jack Li\Desktop\Excel_compare_python\test.bat'])


def clear_log():
      subprocess.call('reset')

def CMT():
       compare_CrmMemberTier()
       compare_CrmMemberTier2()
       compare_CrmMemberTier3()
       compare_CrmMemberTier4()
       compare_CrmMemberTier5()

def CMTS():
       compare_CrmMemberTierSummary1()
       compare_CrmMemberTierSummary2()
       compare_CrmMemberTierSummary3()
       compare_CrmMemberTierSummary4()
       compare_CrmMemberTierSummary5()



def compare_CrmMemberTier():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final1\CrmMemberTier.csv', 'r', newline='',encoding="utf-8-sig") as cmt1,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final1\CrmMemberTier1.csv', 'r', newline='',encoding="utf-8-sig") as cmt11: #對照組

       cmt_reader1 = csv.reader(cmt1)
       cmt_reader11 = csv.reader(cmt11)

       for line1, line11 in zip(cmt_reader1, cmt_reader11):
        cmt_equal = all(x == y for n, (x, y) in enumerate(zip(line1, line11))
        )
        cmt_d = difflib.Differ()
        cmt_result = list(cmt_d.compare(line1,line11))
        print ("情境1-CMT",'\n',cmt_result,'\n', "比較結果:",cmt_equal,'\n')

def compare_CrmMemberTier2():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final2\CrmMemberTier.csv', 'r', newline='',encoding="utf-8-sig") as cmt2,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final2\CrmMemberTier1.csv', 'r', newline='',encoding="utf-8-sig") as cmt22: #對照組

       cmt_reader2 = csv.reader(cmt2)
       cmt_reader22 = csv.reader(cmt22)

       for line2, line22 in zip(cmt_reader2, cmt_reader22):
        cmt_equal2 = all(x == y for n, (x, y) in enumerate(zip(line2, line22))
        )
        cmt_d2 = difflib.Differ()
        cmt_result2 = list(cmt_d2.compare(line2,line22))
        print ("情境2-CMT",'\n',cmt_result2,'\n', "比較結果:",cmt_equal2,'\n')

def compare_CrmMemberTier3():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTier.csv', 'r', newline='',encoding="utf-8-sig") as cmt3,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTier1.csv', 'r', newline='',encoding="utf-8-sig") as cmt33: #對照組

       cmt_reader3 = csv.reader(cmt3)
       cmt_reader33 = csv.reader(cmt33)

       for line3, line33 in zip(cmt_reader3, cmt_reader33):
        cmt_equal3 = all(x == y for n, (x, y) in enumerate(zip(line3, line33))
        )
        cmt_d3 = difflib.Differ()
        cmt_result3 = list(cmt_d3.compare(line3,line33))
        print ("情境3-CMT",'\n',cmt_result3,'\n', "比較結果:",cmt_equal3,'\n')

def compare_CrmMemberTier4():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTier.csv', 'r', newline='',encoding="utf-8-sig") as cmt4,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTier1.csv', 'r', newline='',encoding="utf-8-sig") as cmt44: #對照組

       cmt_reader4 = csv.reader(cmt4)
       cmt_reader44 = csv.reader(cmt44)

       for line4, line44 in zip(cmt_reader4, cmt_reader44):
        cmt_equal4 = all(x == y for n, (x, y) in enumerate(zip(line4, line44))
        )
        cmt_d4 = difflib.Differ()
        cmt_result4 = list(cmt_d4.compare(line4,line44))
        print ("情境4-CMT",'\n',cmt_result4,'\n', "比較結果:",cmt_equal4,'\n')

def compare_CrmMemberTier5():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTier.csv', 'r', newline='',encoding="utf-8-sig") as cmt5,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTier1.csv', 'r', newline='',encoding="utf-8-sig") as cmt55: #對照組

       cmt_reader5 = csv.reader(cmt5)
       cmt_reader55 = csv.reader(cmt55)

       for line5, line55 in zip(cmt_reader5, cmt_reader55):
        cmt_equal5 = all(x == y for n, (x, y) in enumerate(zip(line5, line55))
        )
        cmt_d5 = difflib.Differ()
        cmt_result5 = list(cmt_d5.compare(line5,line55))
        print ("情境5-CMT",'\n',cmt_result5,'\n', "比較結果:",cmt_equal5,'\n')




def compare_CrmMemberTierSummary1():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final1\CrmMemberTierSummary.csv', 'r', newline='',encoding="utf-8-sig") as cmts1,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final1\CrmMemberTierSummary1.csv', 'r', newline='',encoding="utf-8-sig") as cmts11: #對照組

       cmts_reader1 = csv.reader(cmts1)
       cmts_reader11 = csv.reader(cmts11)

       for line1, line11 in zip(cmts_reader1, cmts_reader11):
        cmts_equal = all(x == y for n, (x, y) in enumerate(zip(line1, line11))
        )       
        cmts_e = difflib.Differ()
        cmts_result = list(cmts_e.compare(line1,line11))
        print ("情境CMTS-1",'\n',cmts_result,'\n', "比較結果:",cmts_equal,'\n')

def compare_CrmMemberTierSummary2():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final2\CrmMemberTierSummary.csv', 'r', newline='',encoding="utf-8-sig") as cmts2,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final2\CrmMemberTierSummary1.csv', 'r', newline='',encoding="utf-8-sig") as cmts22: #對照組

       cmts_reader2 = csv.reader(cmts2)
       cmts_reader22 = csv.reader(cmts22)

       for line2, line22 in zip(cmts_reader2, cmts_reader22):
        cmts_equal2 = all(x == y for n, (x, y) in enumerate(zip(line2, line22))
        )       
        cmts_e2 = difflib.Differ()
        cmts_result2 = list(cmts_e2.compare(line2,line22))
        print ("情境CMTS-2",'\n',cmts_result2,'\n', "比較結果:",cmts_equal2,'\n')

def compare_CrmMemberTierSummary3():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTierSummary.csv', 'r', newline='',encoding="utf-8-sig") as cmts3,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final3\CrmMemberTierSummary1.csv', 'r', newline='',encoding="utf-8-sig") as cmts33: #對照組

       cmts_reader3 = csv.reader(cmts3)
       cmts_reader33 = csv.reader(cmts33)

       for line3, line33 in zip(cmts_reader3, cmts_reader33):
        cmts_equal3 = all(x == y for n, (x, y) in enumerate(zip(line3, line33))
        )       
        cmts_e3 = difflib.Differ()
        cmts_result3 = list(cmts_e3.compare(line3,line33))
        print ("情境CMTS-3",'\n',cmts_result3,'\n', "比較結果:",cmts_equal3,'\n')

def compare_CrmMemberTierSummary4():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final4\CrmMemberTierSummary.csv', 'r', newline='',encoding="utf-8-sig") as cmts4,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final4\CrmMemberTierSummary1.csv', 'r', newline='',encoding="utf-8-sig") as cmts44: #對照組

       cmts_reader4 = csv.reader(cmts4)
       cmts_reader44 = csv.reader(cmts44)

       for line4, line44 in zip(cmts_reader4, cmts_reader44):
        cmts_equal4 = all(x == y for n, (x, y) in enumerate(zip(line4, line44))
        )       
        cmts_e4 = difflib.Differ()
        cmts_result4 = list(cmts_e4.compare(line4,line44))
        print ("情境CMTS-4",'\n',cmts_result4,'\n', "比較結果:",cmts_equal4,'\n')

def compare_CrmMemberTierSummary5():
  with open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final5\CrmMemberTierSummary.csv', 'r', newline='',encoding="utf-8-sig") as cmts5,\
       open(r'C:\Users\Jack Li\Desktop\Excel_compare_python\final5\CrmMemberTierSummary1.csv', 'r', newline='',encoding="utf-8-sig") as cmts55: #對照組

       cmts_reader5 = csv.reader(cmts5)
       cmts_reader55 = csv.reader(cmts55)

       for line5, line55 in zip(cmts_reader5, cmts_reader55):
        cmts_equal5 = all(x == y for n, (x, y) in enumerate(zip(line5, line55))
        )       
        cmts_e5 = difflib.Differ()
        cmts_result5 = list(cmts_e5.compare(line5,line55))
        print ("情境CMTS-5",'\n',cmts_result5,'\n', "比較結果:",cmts_equal5,'\n')
       

if __name__ == '__main__':
       launch_program()

root.mainloop()
