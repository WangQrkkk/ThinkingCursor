# ThinkingCursor

A powerful tool for optimizing programming prompts through DeepSeek API integration.

Of course, you can use any thinking model. (DeepSeek-R1,o1,etc.) 

This example uses DeepSeek-R1. 

Before the official website restores API access, you can temporarily use this website

Free trial deepseek series models 

Register address: https://cloud.siliconflow.cn/i/oIk9pMI6 

14 yuan free quota 



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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Interactive Page</title>
    <style>
        /* Modern color scheme */
        :root {
            --primary: #2563eb;
            --secondary: #7c3aed;
            --background: #f8fafc;
            --text: #1e293b;
        }

        /* Base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background: var(--background);
        }

        /* Responsive navigation */
        .navbar {
            background: white;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            justify-content: center;
            list-style: none;
        }

        .nav-links a {
            color: var(--text);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        /* Hero section */
        .hero {
            min-height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
        }

        .hero h1 {
            font-size: clamp(2rem, 5vw, 4rem);
            margin-bottom: 1rem;
        }

        /* Card grid */
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .card {
            background: white;
            padding: 2rem;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        /* Interactive features */
        .button {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 0.25rem;
            cursor: pointer;
            transition: background 0.3s;
        }

        .button:hover {
            background: var(--secondary);
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
        }

        .modal-content {
            background: white;
            padding: 2rem;
            border-radius: 0.5rem;
            max-width: 500px;
            margin: 10vh auto;
        }

        /* Form styles */
        .form-group {
            margin-bottom: 1rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 0.25rem;
        }

        /* Footer */
        footer {
            background: var(--text);
            color: white;
            padding: 2rem;
            text-align: center;
            margin-top: 4rem;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .nav-links {
                flex-direction: column;
                text-align: center;
            }

            .card-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#contact">Contact</a></li>
            <li><a href="#about">About</a></li>
        </ul>
    </nav>

    <!-- Hero section -->
    <section class="hero" id="home">
        <div>
            <h1>Welcome to Our Modern Site</h1>
            <p>Experience the future of web design</p>
            <button class="button" onclick="openModal()">Get Started</button>
        </div>
    </section>

    <!-- Features section -->
    <section id="features">
        <div class="card-grid">
            <div class="card">
                <h3>Responsive Design</h3>
                <p>Looks great on all devices</p>
            </div>
            <div class="card">
                <h3>Modern Interface</h3>
                <p>Clean and intuitive design</p>
            </div>
            <div class="card">
                <h3>Interactive Elements</h3>
                <p>Engaging user experience</p>
            </div>
        </div>
    </section>

    <!-- Contact form -->
    <section id="contact">
        <div class="card-grid">
            <div class="card">
                <h2>Contact Us</h2>
                <form id="contactForm" onsubmit="handleSubmit(event)">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" id="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" rows="4" required></textarea>
                    </div>
                    <button type="submit" class="button">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Modal -->
    <div id="modal" class="modal">
        <div class="modal-content">
            <h2>Welcome!</h2>
            <p>Thank you for your interest. Please sign up for updates.</p>
            <button class="button" onclick="closeModal()">Close</button>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 Modern Website. All rights reserved.</p>
    </footer>

    <script>
        // Modal functionality
        function openModal() {
            document.getElementById('modal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('modal').style.display = 'none';
        }

        // Close modal when clicking outside
        window.onclick = function(event) {
            if (event.target == document.getElementById('modal')) {
                closeModal();
            }
        }

        // Form handling
        function handleSubmit(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            // Here you would typically send this data to a server
            console.log('Form submitted:', { name, email, message });
            alert('Thank you for your message!');
            event.target.reset();
        }

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html> 