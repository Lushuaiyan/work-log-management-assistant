from tools.save_logs import save_log_to_csv
from tools.query_logs import query_logs_csv
from tools.work_summary import save_work_summary
from tools.send_email import send_QQemail

send_QQemail(file_path=save_work_summary("这是一个测试"))