#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
版本信息
"""

__version__ = "1.0.0"
__author__ = "Screenshot Splitter Team"
__email__ = "your-email@example.com"
__description__ = "A tool to split long screenshots into smaller images and generate PDF"
__url__ = "https://github.com/your-username/screenshot-splitter"
__license__ = "MIT"

# 版本历史
VERSION_HISTORY = {
    "1.0.0": {
        "date": "2025-01-26",
        "changes": [
            "智能切分长截图功能",
            "自动生成PDF文件",
            "拖拽文件支持",
            "智能文件命名",
            "支持多种图片格式",
            "Windows可执行文件打包"
        ]
    }
}

def get_version():
    """获取当前版本号"""
    return __version__

def get_version_info():
    """获取详细版本信息"""
    return {
        "version": __version__,
        "author": __author__,
        "description": __description__,
        "url": __url__,
        "license": __license__
    } 