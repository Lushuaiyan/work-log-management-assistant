import pandas as pd
import os
from langchain.tools import tool

# 常量
WORK_LOGS = "./work_logs.csv"

@tool
def change_log_csv(query:dict, alteration:dict)->str:
    """
    Description:
        Modify specified rows in the work logs CSV file based on query conditions.
        Update target column values using the alteration dictionary.
        Save changes back to the original CSV file if data is found and modified.
    Args:
        query: Dictionary containing filter conditions to locate target rows.Required.           
        alteration: Dictionary with columns to update and their new values.Required.
            Keys: Column names in the CSV to modify.
            Values: New data to assign to the corresponding columns.   
    """
    try:
        if not os.path.isfile(WORK_LOGS):
            return "日志文件不存在"
        df = pd.read_csv(WORK_LOGS, encoding="utf-8-sig")
        mask = pd.Series([True] * len(df))
        if "公司" in query:
            mask &= (df["公司"] == query["公司"])
        if "日期" in query:
            mask &= (df["日期"] == query["日期"])
        if "项目名称" in query:
            mask &= (df["项目名称"] == query["项目名称"])
        if not mask.any():
            return "未找到符合条件的日志，请检查条件"
        df.loc[mask, list(alteration.keys())] = list(alteration.values())
        df.to_csv(WORK_LOGS, index=False, encoding="utf-8-sig")
        return "修改成功!"
    except Exception as e:
        return f"修改日志失败：{e}"