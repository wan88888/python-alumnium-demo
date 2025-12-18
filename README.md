# Python Alumnium Demo

基于 [Alumnium](https://github.com/alumnium-hq/alumnium) 的自动化测试示例项目，展示如何使用自然语言编写 UI 自动化测试。

## 项目简介

Alumnium 是一个 AI 驱动的自动化测试框架，允许你使用自然语言描述测试步骤，而不需要编写复杂的定位器代码。本项目包含三种不同框架的示例：

- **Playwright** - Web 端自动化测试
- **Selenium** - Web 端自动化测试
- **Appium** - iOS 移动端自动化测试

## 环境要求

- Python 3.10+
- Node.js 18+（Appium 需要）
- Xcode（iOS 测试需要）
- Google API Key 或 OpenAI API Key

## 安装步骤

### 1. 克隆项目

```bash
git clone <repository-url>
cd python-alumnium-demo
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 安装 Playwright 浏览器（Web 测试需要）

```bash
playwright install
```

### 5. 安装 Appium（iOS 测试需要）

```bash
npm install -g appium
appium driver install xcuitest
```

### 6. 配置环境变量

复制环境变量示例文件：

```bash
cp env.example .env
```

编辑 `.env` 文件，填写你的配置：

```bash
# LLM 配置（二选一）
ALUMNIUM_MODEL="google"
GOOGLE_API_KEY="your-google-api-key"

# 或者使用 OpenAI
# OPENAI_API_KEY="your-openai-api-key"

# SauceDemo 登录配置
SAUCEDEMO_USERNAME="standard_user"
SAUCEDEMO_PASSWORD="secret_sauce"

# Appium 设备配置
APPIUM_DEVICE_NAME="iPhone 16"
APPIUM_PLATFORM_VERSION="18.5"
```

## 运行测试

### 运行 Playwright 测试

```bash
pytest playwright-demo/test_login.py -v
```

### 运行 Selenium 测试

```bash
pytest selenium-demo/test_login.py -v
```

### 运行 Appium 测试

首先启动 Appium Server：

```bash
appium
```

然后在新终端运行测试：

```bash
pytest appium-demo/test_demo.py -v
```

### 生成 HTML 测试报告

```bash
pytest playwright-demo/test_login.py -v --html=report.html --self-contained-html
```

## 项目结构

```
python-alumnium-demo/
├── playwright-demo/          # Playwright 测试示例
│   ├── __init__.py
│   └── test_login.py         # SauceDemo 登录测试
├── selenium-demo/            # Selenium 测试示例
│   ├── __init__.py
│   └── test_login.py         # SauceDemo 登录测试
├── appium-demo/              # Appium 测试示例
│   ├── __init__.py
│   └── test_demo.py          # iOS 设置 App 测试
├── .env                      # 环境变量配置（需自行创建）
├── env.example               # 环境变量示例
├── requirements.txt          # Python 依赖
├── .gitignore               # Git 忽略文件
└── README.md                # 项目说明
```

## Alumnium 核心 API

### `al.do(instruction)`

执行自然语言描述的操作：

```python
al.do("点击登录按钮")
al.do("在用户名输入框输入 'admin'")
al.do("向下滚动页面")
```

### `al.check(statement)`

验证页面状态：

```python
al.check("页面显示登录成功")
al.check("页面包含 'Products' 文字")
```

### `al.get(query)`

从页面获取信息：

```python
title = al.get("页面标题")
price = al.get("商品价格")
```

## 测试网站

本项目使用以下测试网站：

- [SauceDemo](https://www.saucedemo.com) - Sauce Labs 提供的 Web 测试网站
  - 用户名：`standard_user`
  - 密码：`secret_sauce`

## 注意事项

1. **环境变量加载顺序**：`load_dotenv()` 必须在 `from alumnium import Alumni` 之前调用，否则 Alumnium 无法读取到 API Key。

2. **测试目录命名**：避免使用与第三方库同名的目录名（如 `appium`、`playwright`、`selenium`），否则会导致导入冲突。

3. **Appium Session**：Appium 的 `driver.quit()` 只结束 session，不会关闭 App。如需关闭 App，请使用 `driver.terminate_app(bundle_id)`。

## 许可证

MIT License

