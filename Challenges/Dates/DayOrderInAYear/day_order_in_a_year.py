import datetime

def calc_day_order_in_a_year(date:str):
    monthArr = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    # date = input("请输入某年某月某日，格式是 yyyy-mm-dd: ")
    y = int(date[0:4])  # 获取年
    m = int(date[5:7])  # 获取月
    d = int(date[8:])  # 获取日

    targetdate = datetime.date(y,m,d)  # 将输入的日期转化为标准日期
    print(targetdate.strftime("%B"))
    print(monthArr[targetdate.month-1])
    thisyeardate = datetime.date(y,1,1)  # 获取当前年第一天的标准日期
    daycount = (targetdate - thisyeardate).days + 1
    return daycount

# def month_name(date:str):

def calc_day_order_in_a_year_fast(date:str):
# method1
    # return time.strptime(date, "%Y-%m-%d")[-2]

# method2
    Y, M, D = map(int, date.split("-"))
    return int(datetime.date(Y, M, D).strftime("%j"))

# method3
    year, month, day = map(int, date.split('-'))
    month_day_count_arr = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    if year % 400 == 0:
        month_day_count_arr[2] += 1
    elif year % 100 != 0 and year % 4 == 0:
        month_day_count_arr[2] += 1
    
    return sum(month_day_count_arr[:month]) + day

# method4
    year, month, day = map(int, date.split('-'))
    month_day_count_arr = [0,31,59,90,120,151,181,212,243,273,304,334,365]

    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        if month > 2:
            return month_day_count_arr[month - 1] + day + 1
        else:
            return month_day_count_arr[month - 1] + day
    else:
        return month_day_count_arr[month - 1] + day

print("1984-11-12是第",calc_day_order_in_a_year("1984-11-12"),"天")
print("1984-11-12是第",calc_day_order_in_a_year("2020-03-22"),"天")
