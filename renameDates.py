#! /usr/bin/env python3
# renameDates - 将文件名中的美国日期(MM-DD-YYYY)改为中国日期(YYYY-MM-DD)
import re, os, shutil

# 建立匹配日期的正则表达式
datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)
    ([0-3]?\d)
    ((19|20)\d{2})
    (.*?)$
''', re.VERBOSE)

# TODO: Loop over the files in the working directory

# TODO: Skip files without a date

# TODO: Get the different parts of the filename

# TODO: From the Chinese-style filename

# TODO: Get the full, absolute files paths

# TODO: Rename the files
