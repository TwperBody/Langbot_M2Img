# Markdown2IMG Plugin Configuration
# 插件配置文件

# 图片渲染配置
IMG_CONFIG = {
    'width': 400,                    # 图片宽度（像素）
    'format': 'png',                 # 输出格式：png 或 jpg
    'zoom': 2,                       # 缩放比例，提高图片质量
    'quiet': '',                     # 静默模式
    'no-stop-slow-scripts': None,    # 不停止慢脚本
    'enable-local-file-access': None, # 启用本地文件访问
    'quality': 95,                   # JPG质量（仅JPG格式有效）
    'encoding': 'UTF-8'              # 文本编码
}

# Markdown解析配置
MARKDOWN_CONFIG = {
    'enable_dollar_delimiter': True,  # 启用单美元符号数学公式
    'add_preview': True,              # 启用公式预览
    'extensions': [                   # 启用的Markdown扩展
        'mdx_math',                   # 数学公式支持
        'fenced_code',                # 代码块支持
        'tables',                     # 表格支持
        'codehilite',                 # 代码高亮
        'toc',                        # 目录生成
        'footnotes',                  # 脚注支持
        'def_list',                   # 定义列表
        'abbr',                       # 缩写支持
        'attr_list',                  # 属性列表
        'md_in_html',                 # HTML中的Markdown
    ],
    'extension_configs': {
        'codehilite': {
            'css_class': 'highlight',
            'use_pygments': True,
            'noclasses': False,
            'linenums': False,
        },
        'toc': {
            'permalink': True,
            'baselevel': 1,
        }
    }
}

# HTML模板配置 - 简化版本
HTML_TEMPLATE = {
    'front': '''
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown to Image</title>
    
    <!-- MathJax 数学公式支持 -->
    <script type="text/javascript" src="https://cdn.bootcdn.net/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-MML-AM_CHTML"></script>
    
    <!-- 代码高亮样式 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
    
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            padding: 20px;
            margin: 0;
            background-color: #ffffff;
            color: #333333;
            font-size: 14px;
        }
        
        h1, h2, h3, h4, h5, h6 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
            color: #24292e;
        }
        
        h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
        h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
        h3 { font-size: 1.25em; }
        
        p { margin-top: 0; margin-bottom: 16px; }
        
        code {
            background-color: #f6f8fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, monospace;
            font-size: 85%;
            color: #e36209;
        }
        
        pre {
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            border: 1px solid #e1e4e8;
            margin-bottom: 16px;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            border-radius: 0;
            color: inherit;
        }
        
        ul, ol { padding-left: 2em; margin-bottom: 16px; }
        li { margin-bottom: 0.25em; }
        
        blockquote {
            border-left: 4px solid #dfe2e5;
            padding-left: 16px;
            color: #6a737d;
            margin: 0 0 16px 0;
            font-style: italic;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
        }
        
        th, td {
            border: 1px solid #dfe2e5;
            padding: 6px 13px;
            text-align: left;
        }
        
        th { background-color: #f6f8fa; font-weight: 600; }
        tr:nth-child(even) { background-color: #f6f8fa; }
        
        a { color: #0366d6; text-decoration: none; }
        a:hover { text-decoration: underline; }
        
        img { max-width: 100%; height: auto; border-radius: 3px; }
        hr { height: 0.25em; padding: 0; margin: 24px 0; background-color: #e1e4e8; border: 0; }
        strong { font-weight: 600; }
        em { font-style: italic; }
        del { text-decoration: line-through; }
        
        .highlight { background-color: #f6f8fa; border-radius: 6px; }
        .MathJax { overflow-x: auto; overflow-y: hidden; }
    </style>
</head>
<body>
''',
    
    'end': '''
    <!-- 初始化代码高亮 -->
    <script>
        hljs.highlightAll();
    </script>
</body>
</html>
'''
}

# 插件行为配置
PLUGIN_CONFIG = {
    'auto_convert': True,            # 是否自动转换检测到的Markdown
    'min_text_length': 10,           # 最小文本长度（低于此长度不处理）
    'max_text_length': 10000,        # 最大文本长度（超过此长度不处理）
    'temp_file_cleanup': True,       # 是否自动清理临时文件
    'log_level': 'INFO',             # 日志级别：DEBUG, INFO, WARNING, ERROR
    'cache_enabled': True,           # 是否启用缓存
    'cache_ttl': 3600,               # 缓存生存时间（秒）
}

# 支持的输出格式
SUPPORTED_FORMATS = ['png', 'jpg', 'jpeg']

# 默认配置
DEFAULT_CONFIG = {
    'img': IMG_CONFIG,
    'markdown': MARKDOWN_CONFIG,
    'html_template': HTML_TEMPLATE,
    'plugin': PLUGIN_CONFIG,
    'supported_formats': SUPPORTED_FORMATS
} 