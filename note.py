

@cmt1
def compare_CrmMemberTier(a, b):
  with open(r'CrmMemberTier.csv', 'r', newline='',encoding="utf-8-sig") as cmt1,\
       open(r'CrmMemberTier1.csv', 'r', newline='',encoding="utf-8-sig") as cmt11: #對照組

    cmt_reader1 = csv.reader(cmt1)
    cmt_reader11 = csv.reader(cmt11)

    for line1, line11 in zip(cmt_reader1, cmt_reader11):
      print(line1)
      print(line11)
      cmt_equal = all(x == y for n, (x, y) in enumerate(zip(line1, line11)))
      cmt_d = difflib.Differ()
      cmt_result = list(cmt_d.compare(line1,line11))
      print ("情境1-CMT",'\n')
      pprint(cmt_result)
      print("比較結果:",cmt_equal,'\n')