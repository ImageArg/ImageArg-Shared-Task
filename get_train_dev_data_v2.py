"""
=========================================================
Title: ImageArg Shared Task Code - Dataset Downloader
---------------------------------------------------------
Warning: The downloaded dataset should only be used for
participating in ImageArg Shared Task. Any other use is
explicitly prohibited. Any participants are not allowed
to redistribute the dataset per Twitter Developer Policy:
https://developer.twitter.com/en/developer-terms/policy.
---------------------------------------------------------
Notice: This code is managed by ImageArg Shared Task
(https://imagearg.github.io/). Please keep dataset.so
in the root folder in order to run the code.
---------------------------------------------------------
Data: 2023-07-03
=========================================================
"""
import platform

if __name__ == '__main__':
    if platform.processor() == "arm":
        from src.dataset_macos_silicon import get_train_dev_data
    elif platform.system() == "Darwin" and platform.machine() == "x86_64":
        from src.dataset_macos_intel import get_train_dev_data
    elif platform.system() == "Linux" and platform.machine() == "x86_64":
        from src.dataset_ubuntu import get_train_dev_data
    else:
        raise "not supported system!"
    get_train_dev_data()


