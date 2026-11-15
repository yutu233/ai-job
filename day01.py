from datetime import date

NAME = "YUTU"
START = date(2026, 11, 15) # 开始
SPRING = date(2027, 2, 15) # 春招
GRAD = date(2027, 4, 30) # 毕业

def days_between(day1: date, day2: date):
    """返回两个日期之间相差的天数"""
    return (day2 - day1).days

def bar(done, total, width=20):
    """将完成比例以进度条形式呈现"""
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)

def main():
    today = date.today()
    day_no = days_between(START, today) + 1
    left = days_between(today, SPRING)
    total = days_between(START, SPRING)
    done = total - left

    print("=" * 44)
    print(f"{NAME}的求职冲刺面板")
    print(f"今天是第{day_no}天 / 共{total}天")
    print(f"{bar(done, total)} {done}/{total}")
    print(f"距离春招还有{left}天")
    print(f"距离毕业还有{days_between(today, GRAD)}天")
    print("=" * 44)

    if left > 60:
        print("状态: 基础阶段")
    elif left >30:
        print("状态: 项目收尾, 简历定稿")
    else:
        print("状态: 投递期, 边投边补")

main()