import sys
from agent import build_agent

def main():
    agent = build_agent()
    
    print("Agent 已启动！输入 'exit' 退出。")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # 调用 agent，传入对话历史（这里简化为单轮）
        # 实际场景可使用会话ID管理多轮
        config = {"configurable": {"thread_id": "session_1"}}
        try:
            response = agent.invoke(
                {"messages": [("user", user_input)]},
                config=config
            )
            # 输出最后一条AI消息
            last_msg = response["messages"][-1].content
            print(f"AI: {last_msg}")
        except Exception as e:
            print(f"AI: 抱歉，处理时出现了错误：{e}\n请稍后再试或检查您的输入。")
if __name__ == "__main__":
    main()