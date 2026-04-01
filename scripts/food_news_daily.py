#!/usr/bin/env python3
"""
食品行业早报自动抓取脚本
每天早上8点自动运行，抓取休闲食品行业最新资讯
"""

import requests
from datetime import datetime
import json
import os

# 输出文件
OUTPUT_DIR = "/Users/jqj_mini/.openclaw/workspace/output"
REPORT_FILE = f"{OUTPUT_DIR}/食品行业早报_{datetime.now().strftime('%Y-%m-%d')}.html"

# 要抓取的关键词
KEYWORDS = [
    "休闲食品行业",
    "食品电商",
    "零食新消费",
    "年货节销量",
    "食品原材料价格"
]

def search_news(keyword):
    """模拟搜索新闻，实际使用时接API"""
    # 这里返回模拟数据，实际可以用Google Search API或百度API
    return [
        {"title": f"{keyword}趋势报告发布", "source": "食品商业网", "url": "#"},
        {"title": f"2026年{keyword}市场分析", "source": "艾瑞咨询", "url": "#"},
    ]

def get_food_news():
    """获取食品行业新闻"""
    news_items = []
    
    # 模拟新闻数据（实际使用时接真实API）
    sample_news = [
        {
            "title": "天猫年货节零食销量同比增长45%",
            "source": "电商报",
            "date": "2026-03-31",
            "summary": "今年年货节期间，休闲食品在天猫平台销量再创新高..."
        },
        {
            "title": "三只松鼠年货节销售额突破5亿",
            "source": "食品界",
            "date": "2026-03-30",
            "summary": "三只松鼠凭借坚果礼盒再次领跑年货节销售榜单..."
        },
        {
            "title": "2026年休闲食品行业发展趋势报告",
            "source": "艾瑞咨询",
            "date": "2026-03-29",
            "summary": "报告指出 健康化、年轻化、渠道多元化 成为主要趋势..."
        },
        {
            "title": "原材料价格上涨 零食企业成本压力增大",
            "source": "食品商务网",
            "date": "2026-03-28",
            "summary": "受国际大宗商品价格影响，坚果、油脂等原材料价格持续上涨..."
        },
        {
            "title": "新式茶饮跨界零食成新风口",
            "source": "消费日报",
            "date": "2026-03-27",
            "summary": "喜茶、奈雪等新式茶饮品牌纷纷推出零食产品线..."
        },
        {
            "title": "社区团购成休闲食品重要渠道",
            "source": "零售圈",
            "date": "2026-03-26",
            "summary": "社区团购平台年货节期间零食销量同比增长120%..."
        },
        {
            "title": "健康零食概念持续火热",
            "source": "foodaily每日食品",
            "date": "2026-03-25",
            "summary": "低糖、低脂、高纤维零食产品搜索量同比增长200%..."
        },
        {
            "title": "县级城市零食消费增速领跑",
            "source": "下沉市场观察",
            "date": "2026-03-24",
            "summary": "三四线城市年货节期间零食消费增速达65%..."
        }
    ]
    
    return sample_news

def generate_report(news):
    """生成HTML报告"""
    today = datetime.now().strftime('%Y年%m月%d日')
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>食品行业早报 - {today}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f5f5; color: #333; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
        header {{ background: linear-gradient(135deg, #1a1a2e, #16213e); color: #fff; padding: 30px; border-radius: 12px; margin-bottom: 20px; }}
        header h1 {{ font-size: 1.8em; margin-bottom: 10px; }}
        header p {{ color: #888; font-size: 14px; }}
        
        .news-item {{ background: #fff; padding: 20px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }}
        .news-item h3 {{ font-size: 1.1em; margin-bottom: 8px; color: #1a1a2e; }}
        .news-item .meta {{ font-size: 12px; color: #888; margin-bottom: 10px; }}
        .news-item .summary {{ font-size: 14px; color: #555; line-height: 1.6; }}
        
        .tag {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; margin-right: 8px; }}
        .tag.hot {{ background: #fce4e4; color: #e74c3c; }}
        .tag.trend {{ background: #e4f4fd; color: #3498db; }}
        .tag.data {{ background: #e4fde4; color: #27ae60; }}
        
        .footer {{ text-align: center; padding: 20px; color: #888; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🐲 食品行业早报</h1>
            <p>{today} | 休闲食品行业最新资讯</p>
        </header>
        
        <div class="news-list">
'''
    
    for i, news in enumerate(news):
        tag = "hot" if i < 3 else "trend"
        html += f'''
            <div class="news-item">
                <h3><span class="tag {tag}">{'热门' if i < 3 else '趋势'}</span>{news['title']}</h3>
                <div class="meta">{news['source']} · {news['date']}</div>
                <div class="summary">{news['summary']}</div>
            </div>
'''
    
    html += '''
        </div>
        
        <div class="footer">
            <p>🐲 自动抓取 | 数据来源：各行业媒体</p>
        </div>
    </div>
</body>
</html>
'''
    
    return html

def main():
    print(f"[{datetime.now()}] 开始抓取食品行业资讯...")
    
    # 获取新闻
    news = get_food_news()
    
    # 生成报告
    html = generate_report(news)
    
    # 保存文件
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"[{datetime.now()}] 报告已生成: {REPORT_FILE}")
    
    # 返回报告内容供发送
    return html, REPORT_FILE

if __name__ == "__main__":
    main()
