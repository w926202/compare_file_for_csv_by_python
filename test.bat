mkdir offline_final1-1
.\exe\NineYi.MemberTier.Console.exe "/CalculateDateStart=2019-03-01" "/CalculateDateEnd=2019-03-01" "/CsvSourcePath=.\offline_stage1-1\\" "/CsvOutputPath=.\offline_final1-1\\"
mkdir online_final2
.\exe\NineYi.MemberTier.Console.exe "/CalculateDateStart=2019-03-01" "/CalculateDateEnd=2019-03-05" "/CsvSourcePath=.\online_stage2\\" "/CsvOutputPath=.\online_final2\\"
mkdir general_final1
.\exe\NineYi.MemberTier.Console.exe "/CalculateDateStart=2019-02-26" "/CalculateDateEnd=2019-02-26" "/CsvSourcePath=.\general_stage1\\" "/CsvOutputPath=.\general_final1\\"