# 🌟 个人智能助手小智

一个跨平台的Python个人助手，帮助你管理天气、待办事项、学习笔记和励志名言。支持Windows和Linux系统，是你学习和生活中的得力助手！

---

## ✨ 功能特色

| 功能模块 | 描述 | 表情 |
|----------|------|------|
| 🌤️ **天气查询** | 实时查询城市天气，支持全国主要城市 | 🌤️📱 |
| 📝 **待办事项** | 管理个人任务，支持优先级和状态跟踪 | ✅📅 |
| 📒 **学习笔记** | 记录学习心得，支持分类和全文搜索 | 📚🔍 |
| 💪 **励志名言** | 随机推荐励志名言，支持收藏功能 | 💖🎯 |

---

## 🚀 快速开始

### 第1步：克隆项目
```bash
git clone https://github.com/rikka914/personal_assistant.git
cd personal_assistant
```

### 第2步：安装依赖
```bash
pip install -r requirements.txt
```

### 第3步：配置天气API（可选）
1. 访问[和风天气开发者平台](https://dev.qweather.com/)
2. 注册并获取API Key
3. 编辑`config/`目录下的配置文件：
   - Windows: `windows_weather_config.json`
   - Linux: `linux_weather_config.json`
4. 将`"your_api_key_here"`替换为你的真实API Key

### 第4步：运行程序
```bash
cd src
python main.py
```

---

## 🎮 使用方法

运行程序后，你会看到以下主菜单：

```
==============================
       个人智能助手小智 - 跨平台版
==============================
运行平台: [你的系统]

所有模块加载成功！

------------------------------
1. 🌤️  查看天气
2. 📝  待办事项
3. 📒  学习笔记
4. 💪  随机鼓励
5. ⚙️  系统信息
6. ❌  退出
------------------------------
请选择功能 (1-6):
```

### 功能示例

#### 1. 查询天气
```
选择：1
输入：北京

🌤️  北京天气
🌡️  温度：18°C
☁️  天气：晴
💧  湿度：45%
💨  风力：东北风 2级
```

#### 2. 管理待办事项
- 添加任务：记录学习计划、购物清单等
- 标记完成：成就感满满！
- 按优先级排序：重要的事情先做

#### 3. 记录学习笔记
- 分类管理：学习、工作、生活
- 全文搜索：快速找到需要的笔记
- 时间戳记录：追踪学习进度

#### 4. 获取励志名言
- 随机推荐：每天一句正能量
- 收藏功能：保存你喜欢的名言
- 自定义添加：创建个人名言库

---

## 📁 项目结构

```
personal_assistant/
├── src/                    # 源代码
│   ├── main.py            # 主程序入口
│   ├── utils/             # 工具函数
│   └── modules/           # 功能模块
├── config/                # 配置文件
│   ├── windows_weather_config.json
│   ├── linux_weather_config.json
│   └── default_weather_config.json
├── modules/               # 模块代码
│   ├── weather.py        # 天气查询
│   ├── todo.py           # 待办事项
│   ├── notes.py          # 学习笔记
│   └── quotes.py         # 励志名言
├── requirements.txt       # 依赖列表
└── README.md             # 项目说明
```

---

## ⚙️ 技术特点

- **跨平台支持**：自动适配Windows/Linux系统
- **数据持久化**：JSON格式存储，安全可靠
- **错误处理**：友好的错误提示和异常捕获
- **用户友好**：中文界面，简单直观的操作
- **模块化设计**：易于扩展和维护

---

## 🔧 高级功能

### 打包为可执行文件
```bash
# 安装打包工具
pip install pyinstaller

# 打包为单个exe文件
pyinstaller --onefile --name="PersonalAssistant" --add-data="config;config" src/main.py
```

### 自定义配置
- 修改`config/`目录下的配置文件，适配你的需求
- 在`modules/quotes.py`中添加你自己的励志名言
- 扩展新的功能模块，只需在`modules/`目录下添加新文件

---

## 🤝 贡献指南

欢迎为项目贡献力量！你可以：

1. **报告问题**：在GitHub Issues中反馈bug或建议
2. **改进代码**：提交Pull Request优化代码
3. **添加功能**：扩展新的功能模块
4. **完善文档**：帮助改进README和注释

### 开发规范
- 使用清晰的函数和变量命名
- 添加必要的代码注释
- 保持代码风格统一
- 测试你的修改

---

## 📚 学习价值

这个项目非常适合Python初学者学习：

- ✅ **文件操作**：JSON读写、路径管理
- ✅ **网络请求**：API调用、错误处理
- ✅ **面向对象**：类设计、模块化编程
- ✅ **用户交互**：命令行界面设计
- ✅ **跨平台开发**：适配不同操作系统

---

## 🐛 常见问题

### Q: 天气查询失败怎么办？
A: 检查网络连接，确认API Key配置正确。

### Q: 数据文件存储在哪里？
- Windows: `%APPDATA%\PersonalAssistant\`
- Linux: `~/.personal_assistant/`

### Q: 如何添加新的功能模块？
1. 在`modules/`目录下创建新的Python文件
2. 实现相应的类和方法
3. 在`src/main.py`中导入并集成到菜单

### Q: 程序在Linux上显示乱码？
A: 确保终端支持UTF-8编码，可以尝试设置：
```bash
export LANG=en_US.UTF-8
```

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

## 👩‍💻 关于作者

**Rika** - Python爱好者和学习者

- GitHub: [@rikka914](https://github.com/rikka914)
- 项目初衷：在学习Python过程中，开发一个实用的个人工具

---

## 💖 致谢

感谢所有为项目提供建议和帮助的朋友们！特别感谢：
- 和风天气提供的免费API服务
- Python开源社区的各种优秀库
- 所有测试和使用这个项目的用户

---

## 🎯 下一步计划

- [ ] 添加GUI图形界面
- [ ] 支持数据云同步
- [ ] 增加语音交互功能
- [ ] 开发移动端应用
- [ ] 集成更多实用工具

---

## 🌈 开始使用吧！

无论你是想管理日常生活，还是学习Python编程，这个项目都能帮到你。现在就克隆项目，开始你的智能助手之旅吧！

```bash
git clone https://github.com/rikka914/personal_assistant.git
cd personal_assistant
pip install -r requirements.txt
cd src
python main.py
```

**祝你使用愉快！** 🎉

---

*如果觉得这个项目对你有帮助，请给它一个⭐星标支持！*