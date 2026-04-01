from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from config import MODEL_NAME, TEMPERATURE, DEEPSEEK_API_KEY, QQEMAIL_PASSWORD
from tools.get_datetime import get_current_time, get_date_range
from tools.save_logs import save_log_to_csv
from tools.query_logs import query_logs_csv, get_all_companies, get_all_projects, get_all_work_contents
from tools.change_log import change_log_csv
from tools.work_summary import save_work_summary
from tools.send_email import send_QQemail

#from db import search      # 可选，用于检索增强

def load_system_prompt():
    """从文件加载系统提示词"""
    with open("prompts/工作日志管理助手.txt", "r", encoding="utf-8") as f:
        return f.read()

def build_agent():

    # 定义模型
    model = ChatDeepSeek(
        api_key=DEEPSEEK_API_KEY,
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )
        
    # 定义工具列表
    tools = [get_current_time,
             get_date_range,             
             save_log_to_csv,
             query_logs_csv,
             get_all_companies,
             get_all_projects,
             get_all_work_contents,
             change_log_csv,
             save_work_summary,
             send_QQemail]

    # 系统提示词（可包含工具说明、角色等）
    system_prompt = load_system_prompt()
    print(system_prompt)
    # 创建 ReAct Agent（使用 LangGraph 预置组件）
    agent = create_agent(
        model,
        tools=tools,
        system_prompt=system_prompt,   # 系统提示词注入
        checkpointer=MemorySaver()      # 支持对话记忆（可选）
    )
    return agent    
