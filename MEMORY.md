# 长期记忆

## 关于周老帥
- **身份**：企业顾问，辅导国内休闲食品经销商
- **目标**：为客户谋获利，为企业谋增长
- **特点**：细心稳妥、稳重靠谱
- **公司**：至汇贸易（茂名地区休闲食品经销商）

## 工作模式
- 每天自动记录重点事项到 `memory/YYYY-MM-DD.md`
- 分析销售数据、库存数据
- 客户管理、销售分析

---

## 🌐 数据报告网站

### 网址
**https://jqjtoc-ai.github.io/sales-dashboard/**

### 仓库
**https://github.com/jqjtoc-ai/sales-dashboard**

---

## 📁 文件夹结构（重要！）

### 本地工作区
```
/Users/jqj_mini/Documents/OpenClaw报表/
├── 至汇贸易/
│   ├── 销售报表/
│   ├── 库存报表/
│   └── 上传资料/          # 原始数据上传位置
├── 金诚铭语/
│   ├── 销售报表/
│   ├── 库存报表/
│   └── 上传资料/
├── 深红果/
│   ├── 销售报表/
│   ├── 库存报表/
│   └── 上传资料/
├── 好转俱乐部/
│   ├── 销售报表/
│   ├── 库存报表/
│   └── 上传资料/
```

### 文件命名规则
- 报告名格式：`YYYY-MM-DD-报告名.后缀`
- 例如：`2026-03-21-销售数据分析看板.html`

### GitHub发布结构
```
sales-dashboard/
├── index.html              # 首页（公司列表）
├── 公司名/
│   ├── index.html         # 公司首页
│   ├── 销售报告/
│   │   ├── index.html
│   │   └── YYYY-MM-DD-报告名.html
│   └── 库存报告/
│       ├── index.html
│       └── YYYY-MM-DD-报告名.html
```

### 当前公司
- 至汇贸易
- 金诚铭语
- 深红果
- 好转俱乐部（其他公司或未知公司默认为好转俱乐部）

---

## 📋 工作流程（Telegram指令）

### 1. 发数据给我
- 直接上传Excel/CSV文件

### 2. 我分析并生成
- 网页看板（HTML）
- 详细报告（Markdown）
- PPT汇报版（PPTX）

### 3. 确认OK后
- 我自动推送到GitHub
- 自动发布到网址

### 4. 网址格式
```
首页：https://jqjtoc-ai.github.io/sales-dashboard/
公司：https://jqjtoc-ai.github.io/sales-dashboard/至汇贸易/
报告：https://jqjtoc-ai.github.io/sales-dashboard/至汇贸易/销售报告/2026-03-21-xxx.html
```

---

## 📋 工作流程

### 分析报告流程
1. **上传数据** → Telegram上传文件 → 我帮你移动到 `OpenClaw报表/公司名/上传资料/`
2. **分析数据** → 按照分析指令模板的4个维度分析
3. **发送确认** → 先发Telegram网页版给我确认
4. **确认OK** → 再上传GitHub

### Telegram发送报告
```bash
python3 /Users/jqj_mini/.openclaw/workspace/scripts/send_report.py <公司> <报表类型> <报告名>
```

---

## 关键数据（2026-03-18）
- 销售明细：3月1-17号，44,084条记录
- 库存明细：3-18号，23,297条记录
- 部门：13个

## 注意事项
- 需要定期补货的畅销品（库存天数接近0）
- 关注库存天数过高的滞销品
