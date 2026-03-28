#!/usr/bin/env python3
"""根据文件名自动移动文件到对应公司"""

import os
import sys
import shutil
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
    # 转为小写忽略大小写
    filename_lower = filename.lower()
    for keyword, company in COMPANY_KEYWORDS.items():
        if keyword in filename_lower:
            return company
    return DEFAULT_COMPANY

def move_file(filepath: str) -> bool:
    """移动文件到对应公司"""
    filepath = Path(filepath)
    if not filepath.exists():
        print(f"❌ 文件不存在: {filepath}")
        return False
    
    filename = filepath.name
    company = detect_company(filename)
    
    # 目标文件夹
    target_dir = Path(UPLOAD_BASE) / company / "上传资料"
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # 目标路径
    target_path = target_dir / filename
    
    # 如果目标文件已存在，加序号
    if target_path.exists():
        stem = target_path.stem
        suffix = target_path.suffix
        counter = 1
        while target_path.exists():
            target_path = target_dir / f"{stem}_{counter}{suffix}"
            counter += 1
    
    # 移动文件
    shutil.move(str(filepath), str(target_path))
    
    print(f"✅ 已移动: {filename}")
    print(f"   -> {company}/上传资料/{target_path.name}")
    return True

def main():
    if len(sys.argv) < 2:
        print("用法: python move_file.py <文件路径>")
        print("示例: python move_file.py /path/to/销售数据.xlsx")
        sys.exit(1)
    
    filepath = sys.argv[1]
    success = move_file(filepath)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()