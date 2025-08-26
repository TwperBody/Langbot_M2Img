# 🪟 Windows 用户安装指南

## 📋 前置要求

- Windows 10 或更高版本
- 管理员权限（用于安装软件）

## 🚀 安装步骤

### 方法一：手动下载安装（推荐）

1. **访问官方网站**
   - 打开浏览器访问：https://wkhtmltopdf.org/downloads.html

2. **下载安装包**
   - 找到 "Windows" 部分
   - 下载适合您系统的版本：
     - **64位系统**：`wkhtmltopdf-0.12.6-1.msvc2015-win64.exe`
     - **32位系统**：`wkhtmltopdf-0.12.6-1.msvc2015-win32.exe`

3. **安装软件**
   - 双击下载的 `.exe` 文件
   - 按照安装向导完成安装
   - **重要**：使用默认安装路径（通常是 `C:\Program Files\wkhtmltopdf\`）

4. **验证安装**
   - 打开新的命令提示符或 PowerShell
   - 运行：`wkhtmltopdf --version`
   - 如果显示版本信息，说明安装成功

### 方法二：使用 Chocolatey（如果已安装）

```powershell
# 以管理员身份运行 PowerShell
choco install wkhtmltopdf
```

### 方法三：使用 Scoop（如果已安装）

```powershell
# 在 PowerShell 中运行
scoop install wkhtmltopdf
```

## ✅ 安装后验证

安装完成后，请按以下步骤验证：

1. **重启命令提示符/PowerShell**
   - 关闭所有已打开的命令行窗口
   - 重新打开新的命令行窗口

2. **测试命令**
   ```powershell
   wkhtmltopdf --version
   ```

3. **重启插件**
   ```bash
   lbp run
   ```

## 🔧 故障排除

### 问题1：命令未找到
**症状**：`'wkhtmltopdf' 不是内部或外部命令`

**解决方案**：
1. 检查是否已正确安装
2. 检查环境变量 PATH 是否包含安装路径
3. 重启命令行窗口

### 问题2：权限不足
**症状**：安装过程中提示权限不足

**解决方案**：
1. 右键点击安装程序
2. 选择"以管理员身份运行"

### 问题3：插件仍无法使用
**症状**：安装 wkhtmltopdf 后插件仍报错

**解决方案**：
1. 确认 wkhtmltopdf 命令可用
2. 重启 LangBot 插件
3. 检查插件日志

## 📱 安装完成后的效果

安装成功后，您将看到：

```
✅ 使用 imgkit (系统wkhtmltopdf) 引擎
✅ imgkit (系统wkhtmltopdf) 依赖检查通过
```

## 🎯 下一步

安装完成后，您可以：

1. **测试插件功能**
   - 发送 Markdown 文本
   - 查看图片输出效果

2. **自定义配置**
   - 调整图片尺寸
   - 设置输出格式
   - 配置缓存选项

3. **享受完整功能**
   - 数学公式渲染
   - 代码语法高亮
   - 表格和列表支持

## 💡 技术说明

- **为什么需要安装**：Windows 系统无法使用 Linux 兼容的二进制文件
- **降级机制**：插件会自动检测并使用系统安装的 wkhtmltopdf
- **性能表现**：系统版本通常比内置版本性能更好
- **更新维护**：可以独立更新 wkhtmltopdf 版本

---

**需要帮助？** 请检查插件日志或联系技术支持。 