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
for amerFilename in os.listdir():
    mo = datePattern.search(amerFilename)

    # TODO: Skip files without a date
    if mo == None:
        continue

    # TODO: Get the different parts of the filename
    beforeFile = mo.group(1)
    monthFile = mo.group(2)
    dayFile = mo.group(4)
    yearFile = mo.group(5)
    afterFile = mo.group(7)

    # TODO: From the Chinese-style filename
    chineseFilename = beforeFile + yearFile + '-' + monthFile + '-' + dayFile + afterFile

    # TODO: Get the full, absolute files paths
    absWorkDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkDir, amerFilename)
    chineseFilename = os.path.join(absWorkDir, chineseFilename)

    # TODO: Rename the files
    print('Renaming %s to %s...' % (amerFilename, chineseFilename))
    shutil.move(amerFilename, chineseFilename)
