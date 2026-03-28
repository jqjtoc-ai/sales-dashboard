#!/usr/bin/env python3
"""监听 Telegram 上传文件，自动移动到对应公司文件夹"""

import os
import shutil
import time
from pathlib import Path

# 配置
UPLOAD_BASE = "/Users/jqj_mini/Documents/OpenClaw报表"

# 公司映射（模糊匹配关键词 -> 公司文件夹）
COMPANY_KEYWORDS = {
    "至汇": "至汇贸易",
    "金诚": "金诚铭语",
    "深红果": "深红果",
}

# 默认公司（未知/其他）
DEFAULT_COMPANY = "好转俱乐部"

def detect_company(filename: str) -> str:
    """根据文件名检测公司"""
    for keyword, company in COMPANY_KEYWORDS.items():
        if keyword in filename:
            return company
    return DEFAULT_COMPANY

def move_file(filepath: Path):
    """移动文件到对应公司"""
    filename = filepath.name
    company = detect_company(filename)
    
    # 目标文件夹
    target_dir = Path(UPLOAD_BASE) / company / "上传资料"
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # 移动文件
    target_path = target_dir / filename
    shutil.move(str(filepath), str(target_path))
    
    print(f"📂 已移动: {filename} -> {company}/上传资料/")
    return company

def main():
    """主循环"""
    print("🔄 开始监听文件上传...")
    
    # 创建监听目录（如果不存在）
    upload_base = Path(UPLOAD_BASE)
    for company in list(COMPANY_KEYWORDS.values()) + [DEFAULT_COMPANY]:
        (upload_base / company / "上传资料").mkdir(parents=True, exist_ok=True)
    
    # 记录已处理的文件
    processed = set()
    
    while True:
        try:
            # 检查所有公司的上传资料文件夹
            for company in list(COMPANY_KEYWORDS.values()) + [DEFAULT_COMPANY]:
                upload_dir = upload_base / company / "上传资料"
                if not upload_dir.exists():
                    continue
                    
                for filepath in upload_dir.iterdir():
                    if filepath.is_file() and filepath.name not in processed:
                        # 新文件，处理它
                        processed.add(filepath.name)
                        move_file(filepath)
            
            time.sleep(2)
        except KeyboardInterrupt:
            print("\n🛑 停止监听")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()