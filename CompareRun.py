import csv
import difflib
import subprocess
import os
from pprint import pprint
from typing import List

from TestCaseConfig import TestCaseConfig


def echo_bat_file(bat_file_path, exe_file_path=None):
    """
    執行bat進行測試
    :param bat_file_path:
    :param exe_file_path:
    :return:
    """
    # 切換執行目錄
    parent_dir_of_bat_file = os.path.dirname(os.path.abspath(bat_file_path))
    os.chdir(parent_dir_of_bat_file)

    # 有指定exe_file路徑就丟到batch中
    if exe_file_path is not None:
        subprocess.run([bat_file_path, exe_file_path], check=True, shell=True)
    else:
        subprocess.run([bat_file_path], check=True, shell=True)


def clear_log():
    subprocess.call('reset')


def test_all(test_case_configs: List[TestCaseConfig]):
    """
    執行所有測試
    :param test_case_configs:
    :return:
    """
    for test_case_config in test_case_configs:
        if not test_case_config.enabled:
            continue

        for bat_file_path in test_case_config.bat_file_paths:
            try:
                echo_bat_file(bat_file_path, test_case_config.exe_file_path)
            except subprocess.CalledProcessError as ex:
                # Console有丟出Exception會拋出這個Exception
                # 目前先印出StackTrace讓程式繼續
                print(ex)


def compare_all(test_case_configs: List[TestCaseConfig]):
    """
    比較所有實驗組，對照組
    :return:
    """
    for test_case_config in test_case_configs:
        if not test_case_config.enabled:
            continue

        experiment_paths = test_case_config.experiment_paths
        controlled_paths = test_case_config.controlled_paths

        for experiment_path, controlled_path in zip(experiment_paths, controlled_paths):
            compare_csv(f"{experiment_path}/CrmMemberTier.csv", f"{controlled_path}/CrmMemberTier.csv",
                        ignore_index_list=[13,  # CrmMemberTier_CalculateGroupId
                                           20   # CrmMemberTier_CreatedDateTime
                                           ])
            compare_csv(f"{experiment_path}/CrmMemberTierSummary.csv", f"{controlled_path}/CrmMemberTierSummary.csv",
                        ignore_index_list=[15,  # CrmMemberTierSummary_UpdatedDateTime
                                           ])


def filter_out(line, ignore_index_list):
    """
    將ignore_index_list中的元素排除掉
    :param line:
    :param ignore_index_list:
    :return:
    """
    return [x for index, x in enumerate(line)
            if index not in ignore_index_list]


def compare_csv(experiment_path, controlled_path, ignore_index_list=[]):
    """
    比對csv
    :param experiment_path: 實驗組
    :param controlled_path: 對照組
    :param ignore_index_list: 忽略index清單
    :return:
    """
    print(f"experiment: {experiment_path}")
    print(f"controlled: {controlled_path}")

    total_equality = True

    with open(experiment_path, 'r', newline='', encoding="utf-8-sig") as experiment_file, \
            open(controlled_path, 'r', newline='', encoding="utf-8-sig") as controlled_file:  # 對照組

        experiment_reader = csv.reader(experiment_file)
        controlled_reader = csv.reader(controlled_file)

        # 移掉CSV Header
        zipped = list(zip(experiment_reader, controlled_reader))
        zipped.pop(0)

        for line_experiment, line_controlled in zipped:
            # 忽略不比較的元素
            line_experiment = filter_out(line_experiment, ignore_index_list)
            line_controlled = filter_out(line_controlled, ignore_index_list)

            line_equality = all(x == y for n, (x, y) in enumerate(zip(line_experiment, line_controlled)))

            # 只有不相等的才Show結果
            if not line_equality:
                print("比較結果:", line_equality, '\n')
                differ = difflib.Differ()
                differ_compare_list = list(differ.compare(line_experiment, line_controlled))
                pprint(differ_compare_list)
                total_equality = False

    if total_equality:
        print("全等")


def get_test_case_configs() -> List[TestCaseConfig]:
    exe_file_path = r"C:\91APP\NineYi.MemberTier\NineYi.MemberTier.Console\bin\Release\netcoreapp2.2\win-x64\publish" \
                    r"\NineYi.MemberTier.Console.exe"

    test_case_base_path = r"C:\Users\Alex Tann\Google 雲端硬碟\會員重構資料"

    test_case_configs = [
        TestCaseConfig(list(range(1, 7, 1)) + ['Demo'], fr"{test_case_base_path}\KPL\線上可勾稽退貨升降等", exe_file_path, True),
        TestCaseConfig(range(1, 7, 1), fr"{test_case_base_path}\KPL\線下可勾稽退貨升降等", exe_file_path),
        TestCaseConfig(range(1, 6, 1), fr"{test_case_base_path}\KPL\一般升降等", exe_file_path, False),
        TestCaseConfig([1], fr"{test_case_base_path}\KPL\手動升降等", exe_file_path, False),
        TestCaseConfig(range(1, 4, 1), fr"{test_case_base_path}\KPL\HistoryRepo扣到0不降等", exe_file_path, False),
    ]

    return test_case_configs


def main():
    test_case_configs = get_test_case_configs()

    # 執行.bat
    test_all(test_case_configs)

    # 比對資料
    compare_all(test_case_configs)


if __name__ == '__main__':
    main()
