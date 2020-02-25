"""
这个程序用于分数与评级换算
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出能不能好好学习。
"""

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)