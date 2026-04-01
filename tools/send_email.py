import yagmail
import os
from langchain.tools import tool

# 常量
QQEMAIL_PASSWORD = os.getenv("QQEMAIL_PASSWORD")
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your_email@qq.com")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "your_email@qq.com")

@tool
def send_QQemail(sender:str = EMAIL_SENDER, receiver:str = EMAIL_RECEIVER, password:str = QQEMAIL_PASSWORD, body:str = "", subject:str = "", file_path:str = None)-> str:
    """
    Description:
        Send an email to user.
    Args:        
        sender: The email address of the sender. 
        receiver: The email address of the receiver.
        password: The password of the sender's email account.
        body: The body of the email.
        subject: The subject of the email.
        file_path: The attachments of the email.
    """
    try:
        yag = yagmail.SMTP(sender, password, host='smtp.qq.com', port=465, smtp_ssl=True, timeout=30)
        content = [body, file_path] if file_path else body
        yag.send(to=receiver, subject=subject, contents=content)
        yag.close()
        return f"邮件发送成功：收件人 {receiver}，主题 {subject}"
    except Exception as e:
        return f"邮件发送失败：{e}"
