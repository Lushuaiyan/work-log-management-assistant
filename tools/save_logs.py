import pandas as pd
import os
from langchain.tools import tool

# 常量
WORK_LOGS = "./work_logs.csv"

@tool
def save_log_to_csv(datetime:str, company:str, project:str, work_content:str)->str:
    """
    Description: 
        Appends a single work log entry to the CSV file.
    Args:
        datetime (str): Date and time of the work record
        company (str): Name of the company
        project (str): Name of the project
        work_content (str): Detailed description of the work content
    """
    try:
        file_exists = os.path.isfile(WORK_LOGS)
        now_row = {
            "日期": datetime,
            "公司": company,
            "项目名": project,
            "工作内容": work_content
        }
        df_new = pd.DataFrame([now_row])
        df_new.to_csv(WORK_LOGS, mode="a", index=False, header=not file_exists, encoding="utf-8-sig")
        return f"工作日志保存成功：{datetime},{company},{project},{work_content}"
    except Exception as e:
        return f"保存日志失败：{e}"