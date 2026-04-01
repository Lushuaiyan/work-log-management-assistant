from langchain.tools import tool

@tool
def save_work_summary(summary: str)-> str:
    """
    Description:
        Save the work summary content to a local MD file.        
    Args:
        summary (any): Work summary content to be saved (will be converted to string automatically).
    """
    try:
        file_path = "./工作摘要.md"
        with open(file_path, "w", encoding="utf-8-sig") as f:
            f.write(str(summary))
        return f"工作总结已保存至：{file_path}"
    except Exception as e:
        return f"保存工作总结失败：{e}"