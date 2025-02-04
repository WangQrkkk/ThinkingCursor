# ThinkingCursor

A powerful tool for optimizing programming prompts through DeepSeek API integration.

通过 DeepSeek API 集成的强大编程提示优化工具。

Of course, you can use any thinking model. (DeepSeek-R1,o1,etc.) | 当然，您可以使用任何思维模型。（ DeepSeek-R1,o1等）

This example uses DeepSeek-R1. | 本示例使用 DeepSeek-R1。

<font color="red">Free trial deepseek series models | 免费试用deepseek系列模型

Register address: https://cloud.siliconflow.cn/i/oIk9pMI6 | 注册地址：https://cloud.siliconflow.cn/i/oIk9pMI6

14 yuan free quota | 14元免费额度 </font>



## 🌟 Features | 特性

- Automatic prompt optimization for programming tasks
- Seamless integration with DeepSeek API
- Intelligent analysis of technical requirements
- Clean output format
- Automatic prompt saving

- 自动优化编程任务的提示
- 与 DeepSeek API 无缝集成
- 智能分析技术需求
- 清晰的输出格式
- 自动保存优化后的提示

## 🚀 Installation | 安装

1. Clone the repository | 克隆仓库:
```bash
git clone https://github.com/WangQrkkk/ThinkingCursor.git
cd ThinkingCursor
```

2. Install dependencies | 安装依赖:
```bash
pip install requests
```

## ⚙️ Configuration | 配置

Before using ThinkingCursor, configure your DeepSeek API key:
使用 ThinkingCursor 之前，请配置您的 DeepSeek API 密钥：

1. Open `deepseek_client.py`
2. Replace `"put your api key here"` with your actual API key:
```python
client = DeepSeekClient("your-actual-api-key")
```
for example:
```python
client = DeepSeekClient("sk-123456789")
```

## 📖 Usage | 使用方法

1. Cursor Composer Mode | Cursor Composer 模式:
- Open project in Cursor | 在 Cursor 中打开项目
- Press Cmd/Ctrl + I to open composer | 按 Cmd/Ctrl + I 打开 composer
- Type your requirements directly | 直接输入您的需求

The optimized prompt will be:
优化后的提示将会：
- Display in console | 显示在控制台
- Save to `1.cursorrules` | 保存到 `1.cursorrules` 文件
- automatically run the optimized prompt | 自动运行优化后的提示

Examples | 示例:
```bash
# Cursor composer example | Cursor composer 示例
"Create a snake game in HTML" // 直接在 composer 中输入
"Write a Python web scraper" // 直接在 composer 中输入
```
2. Command Line | 命令行方式:
```bash
python deepseek_client.py "your prompt here"
```

## 🔧 How It Works | 工作原理

ThinkingCursor analyzes prompts based on:
ThinkingCursor 基于以下方面分析提示：

1. Technical Requirements | 技术要求
   - Core functionality | 核心功能
   - Error scenarios | 错误场景
   - Best practices | 最佳实践

2. User Context | 用户上下文
   - Technical background | 技术背景
   - Requirements | 需求
   - Guidance level | 指导级别

3. Implementation Details | 实现细节
   - Component interactions | 组件交互
   - Configuration options | 配置选项
   - Testing needs | 测试需求

## 📁 Project Structure | 项目结构

```
ThinkingCursor/
├── deepseek_client.py   # Main client | 主客户端
├── .cursorrules         # Rules file | 规则文件
└── README.md           # Documentation | 文档
```

## 🤝 Contributing | 贡献

Contributions welcome! Please:
欢迎贡献！请：

1. Fork the repository | 复刻仓库
2. Create feature branch | 创建特性分支
3. Submit Pull Request | 提交拉取请求

## 📄 License | 许可证

MIT License

## 💡 Support | 支持

For issues or questions | 如有问题或疑问：
1. Check existing issues | 检查现有问题
2. Create new issue | 创建新问题
3. Provide context | 提供上下文

---

Made with ❤️ for better AI programming assistance
为更好的 AI 编程助手而制作 