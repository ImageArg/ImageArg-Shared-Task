"""
=========================================================
Title: ImageArg Shared Task Code - Dataset Downloader
---------------------------------------------------------
Warning: The dataset to download should only be used for
scientific or research purposes. Any other use is
explicitly prohibited. Any participants are not allowed
to redistribute the dataset per Twitter Developer Policy:
https://developer.twitter.com/en/developer-terms/policy.
---------------------------------------------------------
Notice: This code is managed by ImageArg Shared Task
(https://imagearg.github.io/).
---------------------------------------------------------
Data: 2023-10-05
=========================================================
"""
import platform

if __name__ == '__main__':
    if platform.processor() == "arm":
        from plugins.macos_silicon import get_train_dev_data
    elif platform.system() == "Darwin" and platform.machine() == "x86_64":
        from plugins.macos_intel import get_train_dev_data
    elif platform.system() == "Linux" and platform.machine() == "x86_64":
        from plugins.ubuntu import get_train_dev_data
    else:
        raise "not supported system!"
    get_train_dev_data()


