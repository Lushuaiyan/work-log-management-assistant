import pandas as pd
import os
from langchain.tools import tool

# 常量
WORK_LOGS = "./work_logs.csv"

@tool
def get_all_companies()-> list:
    """
    Description:
        Get all unique company names from the work log
    Returns:
        list: All unique company names
    """
    if not os.path.isfile(WORK_LOGS):
        return []
    df = pd.read_csv(WORK_LOGS, encoding="utf-8-sig")
    return df["公司"].drop_duplicates().tolist()

@tool
def get_all_projects()-> list:
    """
    Description:
        Get all unique project names from the work log
    Returns:
        list: All unique project names
    """
    if not os.path.isfile(WORK_LOGS):
        return []
    df = pd.read_csv(WORK_LOGS, encoding="utf-8-sig")
    return df["项目名"].drop_duplicates().tolist()

@tool
def get_all_work_contents()-> list:
    """
    Description:
        Get all unique work contents from the work log
    Returns:
        list: All unique work content entries
    """
    if not os.path.isfile(WORK_LOGS):
        return []
    df = pd.read_csv(WORK_LOGS, encoding="utf-8-sig")
    return df["工作内容"].drop_duplicates().tolist()

@tool
def query_logs_csv(query)-> str:
    """
    Description:
        Query work logs from CSV file with multiple conditions.
        Supports exact matching and date range filtering.
    Args:
        query (dict): Query conditions as key-value pairs.
    Valid Keys:
        日期: Exact date for matching (yy-mm-dd)
        公司: Exact company name for matching
        项目名: Exact project name for matching
        工作内容: Exact work content for matching
        日期_start: Start date for date range query (Required with 日期_end)
        日期_end: End date for date range query (Required with 日期_start)
    Returns:
        pandas.DataFrame: Filtered log data if query succeeds.
        str: Error message if file not found or query fails.
    """
    # 判断文件是否存在
    if not os.path.isfile(WORK_LOGS): return "日志文件不存在"
    df = pd.read_csv(WORK_LOGS, encoding="utf-8-sig")

    conditions = []
    # 普通精确匹配
    for k, v in query.items():
        if k not in ["日期_start", "日期_end"]:
            conditions.append(f"{k}=='{v}'")
    
    # 日期范围查询（范围查询核心）
    date_start = query.get("日期_start")
    date_end = query.get("日期_end")
    if date_start and date_end:
        conditions.append(f"日期 >= '{date_start}'")
        conditions.append(f"日期 <= '{date_end}'")

    # 空查询 = 返回全部日志
    if not conditions:
        return "查询条件为空"
    
    # 拼接查询
    expr = " and ".join(conditions)
    try:
        df_filtered = df.query(expr)
        # 返回字符串方便模型理解
        return df_filtered.to_string(index=False)
    except Exception as e:
        return f"查询失败：{str(e)}"