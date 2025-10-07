# Markdown2IMG 插件

##非图形化系统需要安装无头浏览器
##非图形化系统需要安装无头浏览器
##非图形化系统需要安装无头浏览器
##重要的事情说三遍

![开发群聊](https://img.shields.io/badge/开发群聊-472263434+-blue)
![LangBot版本](https://img.shields.io/badge/LangBot-4.3+-blue)
![Python版本](https://img.shields.io/badge/Python-3.10+-blue)

## 🌟 平台兼容性

| 平台 | 支持状态 | 安装方式 | 说明 |
|------|----------|----------|------|
| 🐧 **Linux** | ✅ 开箱即用 | 自动安装 | 内置 wkhtmltopdf，无需额外配置 |
| 🐳 **Docker** | ✅ 开箱即用 | 自动安装 | 完全支持内置二进制 |
| ☁️ **云平台** | ✅ 开箱即用 | 自动安装 | Heroku、AWS 等云平台验证可用 |
| 🪟 **Windows** | ⚙️ 需配置 | 手动安装 | 需要安装系统 wkhtmltopdf |
| 🍎 **macOS** | ⚙️ 需配置 | 手动安装 | 需要安装系统 wkhtmltopdf |

## 📖 插件简介

Markdown2IMG 是一个为 LangBot 设计的插件，可以将 Markdown 文本实时渲染为精美的图片。支持完整的 Markdown 语法、LaTeX 数学公式、代码语法高亮等功能。

### ✨ 核心特性

- **🚀 智能引擎**: 自动选择最佳的 HTML 转图片引擎
- **🐧 Linux 开箱即用**: 内置 wkhtmltopdf，无需系统安装
- **🔄 跨平台降级**: Windows/macOS 自动降级到系统依赖
- **📐 完整 Markdown 支持**: 标准语法 + 扩展功能
- **🔬 LaTeX 数学公式**: 支持行内和块级数学公式渲染  
- **🎨 代码语法高亮**: 多种编程语言的彩色高亮
- **📊 表格和列表**: 完美支持各种表格和列表格式
- **⚙️ 高度可配置**: 丰富的配置选项满足个性化需求
- **🚀 性能优化**: 智能缓存和异步处理

## 🔧 安装指南

### 🐧 Linux 用户（推荐）

```bash
# 1. 安装插件
lbp install HelloPlugin

# 2. 自动完成！插件会使用内置的 wkhtmltopdf
# ✅ 所有依赖自动安装
# ✅ 无需系统级别的软件安装
# ✅ 立即可用

#非图形化系统需要安装无头浏览器
```


### 🪟 Windows 用户

**需要手动安装 wkhtmltopdf：**

```bash
# 1. 先安装插件
lbp install HelloPlugin

# 2. 安装 wkhtmltopdf（必需）
# 访问 https://wkhtmltopdf.org/downloads.html
# 下载 Windows 版本并安装到默认路径
# 安装完成后插件即可正常使用
```

### 🍎 macOS 用户

**需要通过 Homebrew 安装 wkhtmltopdf：**

```bash
# 1. 先安装插件
lbp install HelloPlugin

# 2. 安装 wkhtmltopdf（必需）
brew install --cask wkhtmltopdf

# 3. 重启插件即可使用
```

### 🐳 Docker 部署

**完全支持容器化部署：**

```dockerfile
FROM python:3.10-slim

# 安装 LangBot 和插件
RUN pip install langbot
COPY HelloPlugin /app/plugins/HelloPlugin

# 插件会自动使用内置的 wkhtmltopdf
# 无需额外的系统依赖
```

## 🚀 快速开始

### 基本使用

```
!md # Hello World
这是**粗体**文本，这是*斜体*文本。

## 代码示例
\```python
def hello():
    print("Hello, World!")
\```

## 数学公式
行内公式：$E = mc^2$

块级公式：
$$
\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}
$$
```

### 配置查看

```
!md-config
```

## ⚙️ 配置选项

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|

## 🎯 使用技巧

### 1. 数学公式渲染
```
!md 
# 数学公式示例

行内公式：$f(x) = ax^2 + bx + c$

块级公式：
$$
\\begin{align}
\\nabla \\times \\vec{E} &= -\\frac{\\partial \\vec{B}}{\\partial t} \\\\
\\nabla \\times \\vec{B} &= \\mu_0\\vec{J} + \\mu_0\\epsilon_0\\frac{\\partial \\vec{E}}{\\partial t}
\\end{align}
$$
```

### 2. 代码高亮
```
!md
\```python
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# 绘图
plt.plot(x, y)
plt.title('正弦函数')
plt.show()
\```
```

### 3. 表格制作
```
!md
| 项目 | 数量 | 价格 |
|------|------|------|
| 苹果 | 5个  | ¥10  |
| 香蕉 | 3根  | ¥6   |
| 橙子 | 2个  | ¥8   |
```

## 🔍 故障排除

### 常见问题

**Q: 插件提示"无可用的HTML转图片引擎"**
A: 请检查依赖安装

**Q: 插件提示"无可用的HTML转图片引擎"**
A: 请检查依赖安装：`pip install python-pdf pdf2image`

**Q: 生成的图片模糊**
A: 调整 `side` 参数，推荐值 800-1000

**Q: 内置wkhtmltopdf不兼容我的系统**
A: 插件会自动降级到系统wkhtmltopdf，请按安装指南安装系统版本

### 技术架构

```
用户输入
    ↓
Markdown解析器
    ↓
HTML模板渲染
    ↓
引擎选择
    ↓
图片生成
    ↓
Base64编码输出
```

## 📝 更新日志

### 1.0.0 (当前版本)
- 🎉 首个正式版本
- ✨ **新增**: 内置 wkhtmltopdf 二进制
- ✨ **新增**: 多引擎支持
- 🔧 **改进**: 重构项目

### v0.2.0
- ✨ **新增**: 内置 wkhtmltopdf 二进制，开箱即用
- ✨ **新增**: 多引擎支持（pydf + imgkit）
- ✨ **新增**: 智能引擎降级机制
- 🔧 **改进**: 更友好的错误提示和安装指南
- 🔧 **改进**: 优化依赖检查逻辑

### v0.1.0
- ✨ 完整的 Markdown 语法支持
- ✨ LaTeX 数学公式渲染
- ✨ 代码语法高亮
- ✨ 表格和脚注支持
- ⚙️ 丰富的配置选项

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证


MIT License
