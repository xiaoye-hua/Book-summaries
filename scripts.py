# -*- coding: utf-8 -*-
# @File    : scripts.py
# @Author  : Hua Guo
# @Time    : 2019/12/15 下午10:24
# @Disc    :
import os
from glob import glob
import subprocess as sp

# target_dir = "convert_pdf"
base_dir = "./pdf_files"
files = glob(os.path.join(base_dir, "*"))
for old_dir in files:
    old_file = old_dir.split("/")[-1]
    new_file = old_file.replace(" ", "_")
    new_dir = os.path.join(base_dir, new_file)
    # if old_file != new_file:
    #     cmd1 = f"cp '{old_dir}' '{new_dir}'"
    #     cmd2 = f"rm -rf '{old_dir}'"
    #     for cmd in [cmd1, cmd2]:
    #         exit_code = sp.call(cmd, shell=True)
    #         assert exit_code == 0 , cmd
    lst = [
        "[",
        new_file.replace(".pdf", ""),
        "]",
        '(',
        new_dir,
        ")"
    ]
    print("".join(lst))
print()