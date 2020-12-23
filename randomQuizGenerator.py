#! /usr/bin/env python3
# randomQuizGenerator.py - 创建若干题目相同但是顺序不同的试卷，选出中国省份对应的行政中心
import random

capitals ={'Shandong': 'Jinan', 'Heilongjiang': 'Harbin', 'Jilin': 'Changchun', 'Liaoning': 'Shenyang',
'Hebei': 'Shijiazhuang', 'Shånxi': 'Taiyuan', 'Shanxi': 'Xian' , 'Neimengu': 'Hohhot', 'Jiangsu': 'Nanjing',
'Zhejiang': 'Hangzhou', 'Anhui': 'Hefei', 'Fujian': 'Fuzhou', 'Jiangxi': 'Nanchang', 'Henan': 'zhengzhou',
'Hubei': 'Wuhan', 'Hunan': 'Changsha', 'Guangdong': 'Guangzhou', 'Guangxi': 'Nanning', 'Hainan': 'Haikou',
'Sichuan': 'Chengdu', 'Guizhou': 'Guiyang', 'Yunnan': 'Kunming', 'Xizang': 'Lasa', 'Gansu': 'Lanzhou',
'Qinghai': 'Xining', 'Ningxia': 'Yinchuan', 'Xinjiang': 'Wulumuqi', 'Taiwan': 'Taibei'
}

# 创建5个不同的试卷文件
for quizNum in range(5):
    # 创建试卷文件
    quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')
    # 创建答案文件
    answerKeyFile = open('capitalsqui_anser%s.txt' % (quizNum+1), 'w')

    # 添加试卷头，各种信息及试卷名
    quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'Province Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    # 对省份的顺序随机排序
    provinces = list(capitals.keys())
    random.shuffle(provinces)           # shuffle()使得参数顺序随机并赋给参数

    # 创建答案选项
    for question in range(len(capitals)):
        correctAnswer = capitals[provinces[question]]       # 获取正确答案
        wrongAnswers = list(capitals.values())               # 将全部答案加入wrongAnswer
        del wrongAnswers[wrongAnswers.index(correctAnswer)]   # 删除其中的correctAnswer
        wrongAnswers = random.sample(wrongAnswers, 3)       # 随机任取3个错误选项
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)                       # 打乱选项顺序

        # 输出选项
        quizFile.write('%s. What is the capital of %s\n' % (question + 1, provinces[question]))
        for i in range(4):
            quizFile.write('%s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # 创建答案文件
        answerKeyFile.write('%s. %s\n' % (question+1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

