#!/usr/bin/env python3
"""发送报告到Telegram"""

import asyncio
import os
import sys
import telegram

# 配置
TOKEN = "8693851497:AAH6WwKEN14pdbCKWykAELhhLEQBjl-BaDI"
USER_ID = 8648326215
BASE_PATH = "/Users/jqj_mini/Documents/OpenClaw报表"

async def send_report(company: str, report_type: str, report_name: str):
    """发送报告到Telegram"""
    
    # 查找文件
    file_path = os.path.join(BASE_PATH, company, report_type, f"{report_name}.html")
    
    if not os.path.exists(file_path):
        # 也尝试 .md
        file_path = os.path.join(BASE_PATH, company, report_type, f"{report_name}.md")
    
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        return False
    
    # 发送文件
    bot = telegram.Bot(token=TOKEN)
    
    with open(file_path, 'rb') as f:
        if file_path.endswith('.html'):
            await bot.send_document(
                chat_id=USER_ID,
                document=f,
                caption=f"🏪 {company} {report_type}\n{report_name}\n\n请确认后告诉我'OK'，我帮你上传GitHub"
            )
        else:
            await bot.send_document(
                chat_id=USER_ID,
                document=f,
                caption=f"📄 {company} {report_type} - {report_name}"
            )
    
    print(f"✅ 已发送: {company}/{report_type}/{report_name}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("用法: python send_report.py <公司> <报表类型> <报告名>")
        print("示例: python send_report.py 至汇贸易 销售报表 2026-03-10-3月第2周")
        sys.exit(1)
    
    company = sys.argv[1]
    report_type = sys.argv[2]
    report_name = sys.argv[3]
    
    asyncio.run(send_report(company, report_type, report_name))
