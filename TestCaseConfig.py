import os


class TestCaseConfig:
    def __init__(self, postfix_generator, base_path, exe_file_path, enabled=True):
        self.base_path = base_path

        # 實驗組path
        self.experiment_paths = [os.path.sep.join([self.base_path, f'情境{c}', r"final"])
                                 for c in postfix_generator]

        # 對照組path
        self.controlled_paths = [os.path.sep.join([self.base_path, f'情境{c}', r"controlled"])
                                 for c in postfix_generator]

        # 執行bat位置
        self.bat_file_paths = [os.path.sep.join([self.base_path, f'情境{c}', r"test.bat"])
                               for c in postfix_generator]

        # 執行檔位置
        self.exe_file_path = exe_file_path

        self.enabled = enabled
