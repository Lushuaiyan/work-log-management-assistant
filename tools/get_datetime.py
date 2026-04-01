from datetime import datetime, timedelta
from langchain.tools import tool

@tool
def get_current_time()-> str:
    """
    Description:
        Get the current time.: yy-mm-dd
    """
    current_time = datetime.now().strftime("%y-%m-%d")
    return current_time

@tool
def get_date_range(range_type: str, year: int = None, month: int = None) -> tuple[str, str]:
    """
    Description:
        Get the start and end date of a specified time range.
        Return dates in format 'yy-mm-dd'.
    Args:
        range_type: The type of time range.Required.
                   Valid values: week, month, year, spec_year, spec_month.
        year: The year for custom range.Required only for spec_year and spec_month.
        month: The month for custom range.Required only for spec_month.
    Returns:
        tuple: A tuple containing (start_date, end_date), both in 'yy-mm-dd' format.
    """
    now = datetime.now()
    current_year = now.year
    current_month = now.month


    # ====================== 本周（周一 ~ 周日）
    if range_type == "week":
        start = now - timedelta(days=now.weekday())
        end = now

    # ====================== 本月
    elif range_type == "month":
        start = now.replace(day=1)
        end = now

    # ====================== 本年
    elif range_type == "year":
        start = now.replace(month=1, day=1)
        end = now

    # ====================== 指定年份
    elif range_type == "spec_year":
        if not year:
            raise ValueError("指定年份时必须传入 year 参数")
        # 如果是 0~99 的两位数年份 → 自动转为 2000+
        if 0 <= year <= 99:
            year += 2000
        # 如果小于1900 → 强制使用当前年份
        if year < 1900:
            year = current_year
        start = datetime(year=year, month=1, day=1)
        end = datetime(year=year, month=12, day=31)

    # ====================== 指定年月
    elif range_type == "spec_month":
        if not year or not month:
            raise ValueError("指定年月时必须传入 year 和 month 参数")
        # 如果是 0~99 的两位数年份 → 自动转为 2000+
        if 0 <= year <= 99:
            year += 2000
        # 如果小于1900 → 强制使用当前年份
        if year < 1900:
            year = current_year
        start = datetime(year=year, month=month, day=1)
        if month == 12:
            next_month = datetime(year=year + 1, month=1, day=1)
        else:
            next_month = datetime(year=year, month=month + 1, day=1)
        end = next_month - timedelta(days=1)

    else:
        raise ValueError(f"不支持的范围类型：{range_type}")

    # 统一格式化为 yy-mm-dd
    return start.strftime("%y-%m-%d"), end.strftime("%y-%m-%d")