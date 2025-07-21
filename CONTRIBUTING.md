# 贡献指南

感谢你对Screenshot Splitter项目的兴趣！我们欢迎并感谢任何形式的贡献。

## 🤝 如何贡献

### 报告Bug

如果你发现了bug，请在GitHub Issues中报告：

1. 使用清晰、描述性的标题
2. 详细描述重现bug的步骤
3. 提供预期行为和实际行为的描述
4. 如果可能，提供屏幕截图
5. 包含你的操作系统和Python版本信息

### 建议新功能

我们很乐意听到你的想法！请在Issues中提交功能请求：

1. 使用清晰、描述性的标题
2. 详细描述建议的功能
3. 解释为什么这个功能有用
4. 如果可能，提供mockup或示例

### 提交代码

#### 开发环境设置

1. Fork这个仓库
2. 克隆你的fork：
   ```bash
   git clone https://github.com/your-username/screenshot-splitter.git
   cd screenshot-splitter
   ```
3. 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
4. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

#### 开发流程

1. 创建新分支：
   ```bash
   git checkout -b feature/amazing-feature
   ```
2. 进行更改
3. 测试你的更改：
   ```bash
   python split_screenshot.py
   ```
4. 提交更改：
   ```bash
   git add .
   git commit -m "Add amazing feature"
   ```
5. 推送到你的fork：
   ```bash
   git push origin feature/amazing-feature
   ```
6. 创建Pull Request

#### 代码规范

- 使用4个空格缩进
- 遵循PEP 8代码风格
- 为函数和类添加文档字符串
- 保持代码简洁易读
- 添加必要的注释

#### 提交信息规范

使用清晰的提交信息：

- `feat: 添加新功能`
- `fix: 修复bug`
- `docs: 更新文档`
- `style: 代码格式化`
- `refactor: 重构代码`
- `test: 添加测试`
- `chore: 构建过程或辅助工具的变动`

### Pull Request指南

1. 确保PR描述清晰地说明了更改内容
2. 引用相关的Issue（如果有）
3. 包含任何必要的文档更新
4. 确保代码通过所有检查
5. 保持PR尽可能小和专注

## 📋 开发计划

### 近期目标
- [ ] 添加单元测试
- [ ] 支持批量处理
- [ ] 改进错误处理
- [ ] 添加进度条显示

### 长期目标
- [ ] 图形用户界面 (GUI)
- [ ] 支持更多输出格式
- [ ] 跨平台支持 (macOS, Linux)
- [ ] 插件系统

## 🛠️ 技术栈

- **语言**: Python 3.6+
- **主要依赖**: Pillow (PIL)
- **打包工具**: PyInstaller
- **CI/CD**: GitHub Actions
- **文档**: Markdown

## 📞 联系方式

如果你有任何问题或需要帮助：

- 创建GitHub Issue
- 在Pull Request中留言
- 通过email联系维护者

## 📄 许可证

通过贡献代码，你同意你的贡献将在MIT许可证下授权。

---

再次感谢你的贡献！ 🎉 