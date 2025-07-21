# 更新日志

所有项目的重要更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### 计划新增
- 支持批量处理多个图片文件
- 添加图形用户界面 (GUI)
- 支持更多输出格式 (DOCX, HTML)
- 自定义水印功能

## [1.0.0] - 2025-01-26

### 新增
- 🔪 智能切分长截图功能
- 📄 自动生成PDF文件
- 🖱️ 拖拽文件支持
- 📂 智能文件命名
- 🎯 支持多种图片格式 (JPG, PNG, BMP, GIF, TIFF)
- 💻 Windows可执行文件打包
- 🌐 中英文双语README
- 🔧 自动化构建和发布流程

### 技术特性
- 基于Python 3.12和Pillow库
- PyInstaller打包为独立可执行文件
- GitHub Actions自动化CI/CD
- MIT开源协议

### 文件结构
```
screenshot-splitter/
├── split_screenshot.py    # 主程序文件
├── requirements.txt       # Python依赖
├── build.bat             # Windows构建脚本
├── README.md             # 项目说明文档
├── LICENSE               # MIT许可证
├── CHANGELOG.md          # 版本更新记录
└── .github/
    └── workflows/
        └── build-and-release.yml  # GitHub Actions工作流
```

## [0.1.0] - 2025-01-26 (内部版本)

### 新增
- 基础的图片切分功能
- 简单的PDF生成功能
- 命令行界面
- 基本错误处理

---

## 版本说明

- **新增**: 新功能
- **修改**: 现有功能的更改
- **弃用**: 即将移除的功能
- **移除**: 已移除的功能
- **修复**: 错误修复
- **安全**: 安全相关的修复 