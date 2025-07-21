# 🖼️ Screenshot Splitter | 长截图切分工具

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/DayDreammy/long-screenshot-splitter-2pdf)](https://github.com/DayDreammy/long-screenshot-splitter-2pdf/releases)
[![GitHub downloads](https://img.shields.io/github/downloads/DayDreammy/long-screenshot-splitter-2pdf/total)](https://github.com/DayDreammy/long-screenshot-splitter-2pdf/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/DayDreammy/long-screenshot-splitter-2pdf/workflows/Build%20and%20Release/badge.svg)](https://github.com/DayDreammy/long-screenshot-splitter-2pdf/actions)

一个简单易用的工具，可以将长截图切分成多个较小的图片，并自动生成PDF文件。支持拖拽操作，无需安装Python环境。

[English](#english) | [中文](#中文)

## 中文

### 💡 项目背景

在现代工作和学习中，**长截图**已经成为信息记录和分享的重要方式。无论是保存网页内容、聊天记录、还是技术文档，长截图都能完整地保留信息的上下文。

同时，**多模态大模型**（如GPT-4V、Claude 3等）的普及让我们能够通过AI来分析和处理图像内容。然而，在实际使用中我们发现了一个关键问题：

> 🚨 **长截图直接输入给多模态大模型效果非常差！**

**主要原因包括：**
- 📏 **分辨率限制**: 大模型对输入图片尺寸有严格限制
- 🔍 **细节丢失**: 长图压缩后文字变得模糊不清
- 🧠 **注意力分散**: 模型难以聚焦于图片中的关键信息
- ⚡ **处理效率低**: 超大图片影响模型推理速度

**这个工具就是为了解决这个痛点而生！**

通过将长截图智能切分成多个小图片，每个小图都能被多模态大模型高质量地处理，同时生成PDF方便整体查看和存档。

### 🎯 使用场景

- **📱 AI分析长聊天记录**: 将微信/QQ长聊天截图切分后用AI总结要点
- **📄 AI解读长文档**: 将长网页/文章截图切分后让AI提取关键信息  
- **📊 AI分析长报告**: 将长图表/报告切分后用AI生成分析报告
- **📚 AI处理学习资料**: 将长教程/笔记截图切分后让AI制作学习卡片
- **💼 工作流程优化**: 结合AI助手处理各种长截图内容

### ✨ 功能特性

- 🔪 **智能切分**：将长截图切分成多个指定高度的图片
- 📄 **PDF生成**：自动将切分后的图片合并成PDF文件
- 🖱️ **拖拽支持**：支持直接拖拽图片文件到程序上
- 📂 **智能命名**：根据原图片名称自动生成输出文件夹和PDF文件名
- 🎯 **格式支持**：支持 JPG、PNG、BMP、GIF、TIFF 等常见图片格式
- 💻 **跨平台**：Windows可执行文件，无需安装Python环境
- 🤖 **AI友好**：切分后的图片尺寸最适合多模态大模型处理

### 🚀 快速开始

#### 下载使用（推荐）

1. 前往 [Releases页面](https://github.com/DayDreammy/long-screenshot-splitter-2pdf/releases) 下载最新版本的 `长截图切分工具.exe`
2. 使用方式：
   - **双击运行**：打开程序，按提示选择图片
   - **拖拽使用**：直接将图片文件拖拽到程序图标上
   - **命令行**：`长截图切分工具.exe "your_image.jpg"`

#### 从源码运行

```bash
# 克隆仓库
git clone https://github.com/DayDreammy/long-screenshot-splitter-2pdf.git
cd long-screenshot-splitter-2pdf

# 安装依赖
pip install -r requirements.txt

# 运行程序
python split_screenshot.py

# 或者指定图片文件
python split_screenshot.py "your_image.jpg"
```

### 📁 输出说明

程序运行后会生成：
- `split_原图片名称/` 文件夹：包含所有切分的PNG图片
- `原图片名称_merged.pdf`：合并后的PDF文件

### ⚙️ 自定义设置

可以在 `split_screenshot.py` 中修改以下参数：
- `max_height=1500`：每个切片的最大高度（像素）

### 🔧 本地构建

```bash
# 安装构建依赖
pip install pyinstaller

# Windows构建
python -m PyInstaller --onefile --console --name="长截图切分工具" split_screenshot.py

# 或者使用批处理脚本
.\build.bat
```

### 📋 系统要求

- **可执行文件**：Windows 10/11 (64-bit)
- **源码运行**：Python 3.6+ + Pillow库

### 🤝 贡献指南

我们欢迎任何形式的贡献！

1. Fork 这个仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### 📝 版本历史

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细的版本更新记录。

### 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详细信息。

### 🐛 问题反馈

如果你遇到任何问题，请在 [Issues](https://github.com/DayDreammy/long-screenshot-splitter-2pdf/issues) 页面提交bug报告或功能请求。

---

## English

A simple and easy-to-use tool that can split long screenshots into multiple smaller images and automatically generate PDF files. Supports drag-and-drop operations without requiring Python installation.

### 💡 Project Background

In modern work and study, **long screenshots** have become an essential way to record and share information. Whether it's saving web content, chat records, or technical documentation, long screenshots can completely preserve the context of information.

At the same time, the popularity of **multimodal large models** (such as GPT-4V, Claude 3, etc.) allows us to analyze and process image content through AI. However, in actual use, we discovered a critical problem:

> 🚨 **Long screenshots directly input to multimodal large models perform very poorly!**

**Main reasons include:**
- 📏 **Resolution limitations**: Large models have strict limits on input image dimensions
- 🔍 **Detail loss**: Text becomes blurry after long image compression
- 🧠 **Attention dispersion**: Models struggle to focus on key information in images
- ⚡ **Low processing efficiency**: Oversized images affect model inference speed

**This tool was created to solve this pain point!**

By intelligently splitting long screenshots into multiple small images, each small image can be processed with high quality by multimodal large models, while generating PDFs for convenient overall viewing and archiving.

### 🎯 Use Cases

- **📱 AI analysis of long chat records**: Split WeChat/QQ long chat screenshots for AI to summarize key points
- **📄 AI interpretation of long documents**: Split long webpage/article screenshots for AI to extract key information
- **📊 AI analysis of long reports**: Split long charts/reports for AI to generate analysis reports
- **📚 AI processing of learning materials**: Split long tutorial/note screenshots for AI to create study cards
- **💼 Workflow optimization**: Combine with AI assistants to process various long screenshot content

### ✨ Features

- 🔪 **Smart Splitting**: Split long screenshots into multiple images with specified height
- 📄 **PDF Generation**: Automatically merge split images into PDF files
- 🖱️ **Drag & Drop**: Support drag-and-drop image files directly onto the program
- 📂 **Smart Naming**: Automatically generate output folders and PDF file names based on original image names
- 🎯 **Format Support**: Support common image formats like JPG, PNG, BMP, GIF, TIFF
- 💻 **Cross-platform**: Windows executable without Python installation required
- 🤖 **AI-Friendly**: Split image sizes are optimally suited for multimodal large model processing

### 🚀 Quick Start

#### Download and Use (Recommended)

1. Go to [Releases page](https://github.com/DayDreammy/long-screenshot-splitter-2pdf/releases) and download the latest `长截图切分工具.exe`
2. Usage:
   - **Double-click**: Open the program and follow prompts to select images
   - **Drag & Drop**: Drag image files directly onto the program icon
   - **Command line**: `长截图切分工具.exe "your_image.jpg"`

#### Run from Source

```bash
# Clone repository
git clone https://github.com/DayDreammy/long-screenshot-splitter-2pdf.git
cd long-screenshot-splitter-2pdf

# Install dependencies
pip install -r requirements.txt

# Run program
python split_screenshot.py

# Or specify image file
python split_screenshot.py "your_image.jpg"
```

### 📁 Output

The program generates:
- `split_original_image_name/` folder: Contains all split PNG images
- `original_image_name_merged.pdf`: Merged PDF file

### ⚙️ Customization

You can modify the following parameters in `split_screenshot.py`:
- `max_height=1500`: Maximum height of each slice (pixels)

### 🔧 Local Build

```bash
# Install build dependencies
pip install pyinstaller

# Windows build
python -m PyInstaller --onefile --console --name="长截图切分工具" split_screenshot.py

# Or use batch script
.\build.bat
```

### 📋 System Requirements

- **Executable**: Windows 10/11 (64-bit)
- **Source**: Python 3.6+ + Pillow library

### 🤝 Contributing

We welcome contributions of all kinds!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 