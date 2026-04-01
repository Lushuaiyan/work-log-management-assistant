import os

# 邮箱配置
QQEMAIL_PASSWORD = os.getenv("QQEMAIL_PASSWORD")
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your_email@qq.com")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "your_email@qq.com")

# 模型配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-chat")
TEMPERATURE = 0

# 工作日志路径
WORK_LOGS = "./work_logs.csv"