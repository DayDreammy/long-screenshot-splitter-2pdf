#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
长截图切分脚本
将长截图切分成多个较小的图片文件，并可以将切分后的图片合成PDF
支持拖拽文件到程序上使用
"""

import os
import sys
from PIL import Image
import math
import glob

try:
    from version import __version__, get_version_info
except ImportError:
    __version__ = "1.0.0"
    def get_version_info():
        return {"version": __version__, "author": "Screenshot Splitter Team"}

def safe_input(prompt="", default=""):
    """
    安全的输入函数，在没有控制台时返回默认值
    """
    try:
        return input(prompt)
    except (EOFError, OSError, RuntimeError):
        # 在没有控制台的情况下返回默认值
        return default

def safe_pause():
    """
    安全的暂停函数，在没有控制台时直接返回
    """
    try:
        input("\n按回车键退出...")
    except (EOFError, OSError, RuntimeError):
        # 在没有控制台时，程序自动退出
        pass

def split_image(image_path, output_dir="split_images", max_height=1000):
    """
    将长截图切分成多个图片
    
    Args:
        image_path: 输入图片路径
        output_dir: 输出目录
        max_height: 每个切片的最大高度（像素）
    """
    try:
        # 打开图片
        with Image.open(image_path) as img:
            width, height = img.size
            print(f"原图尺寸: {width} x {height}")
            
            # 创建输出目录
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            # 计算需要切分的片数
            num_slices = math.ceil(height / max_height)
            print(f"将切分成 {num_slices} 个片段")
            
            # 获取原文件名（不含扩展名）
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            
            # 切分图片
            for i in range(num_slices):
                # 计算切片的上下边界
                top = i * max_height
                bottom = min((i + 1) * max_height, height)
                
                # 切片区域 (left, top, right, bottom)
                box = (0, top, width, bottom)
                
                # 裁剪图片
                slice_img = img.crop(box)
                
                # 保存切片
                output_filename = f"{base_name}_part_{i+1:02d}.png"
                output_path = os.path.join(output_dir, output_filename)
                slice_img.save(output_path, "PNG")
                
                print(f"已保存: {output_filename} (尺寸: {slice_img.size[0]} x {slice_img.size[1]})")
                
            print(f"\n✅ 切分完成！共生成 {num_slices} 个文件")
            print(f"输出目录: {output_dir}")
            
    except Exception as e:
        print(f"❌ 错误: {str(e)}")

def images_to_pdf(images_dir, output_pdf_name=None, base_name=None):
    """
    将目录中的图片合成为PDF文件
    
    Args:
        images_dir: 包含图片的目录
        output_pdf_name: 输出PDF文件名，如果为None则自动生成
        base_name: 原图片的基础名称，用于生成PDF文件名
    """
    try:
        # 获取目录中所有PNG图片文件，按名称排序
        image_files = glob.glob(os.path.join(images_dir, "*.png"))
        image_files.sort()  # 确保按正确顺序排列
        
        if not image_files:
            print("❌ 在输出目录中没有找到PNG图片文件")
            return
            
        print(f"📄 找到 {len(image_files)} 个图片文件，准备合成PDF...")
        
        # 打开所有图片
        images = []
        for img_path in image_files:
            img = Image.open(img_path)
            # 如果图片是RGBA模式，转换为RGB（PDF不支持透明度）
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            images.append(img)
            print(f"✓ 加载: {os.path.basename(img_path)}")
        
        # 生成PDF文件名
        if output_pdf_name is None:
            if base_name:
                output_pdf_name = f"{base_name}_merged.pdf"
            else:
                output_pdf_name = "merged_screenshot.pdf"
        
        # 保存为PDF
        if images:
            # 第一张图片作为主图片，其余作为附加页面
            images[0].save(
                output_pdf_name, 
                "PDF", 
                resolution=100.0, 
                save_all=True, 
                append_images=images[1:] if len(images) > 1 else []
            )
            
            print(f"✅ PDF文件已生成: {output_pdf_name}")
            print(f"包含 {len(images)} 页")
            
            # 清理内存
            for img in images:
                img.close()
        
    except Exception as e:
        print(f"❌ 生成PDF时发生错误: {str(e)}")

def show_header():
    """显示程序头部信息"""
    version_info = get_version_info()
    print("=" * 60)
    print("🖼️  Screenshot Splitter | 长截图切分工具")
    print(f"📦 版本: {version_info['version']}")
    print(f"👥 作者: {version_info.get('author', 'Unknown')}")
    print("📄 许可证: MIT")
    print("🌐 GitHub: https://github.com/DayDreammy/long-screenshot-splitter-2pdf")
    print("=" * 60)

def main():
    show_header()
    
    # 检查命令行参数（支持拖拽）
    if len(sys.argv) > 1:
        # 通过拖拽或命令行参数传入文件路径
        image_path = sys.argv[1]
        print(f"📁 检测到输入文件: {os.path.basename(image_path)}")
    else:
        # 交互式输入
        print("请选择输入方式：")
        print("1. 输入文件路径")
        print("2. 使用默认图片文件")
        
        choice = safe_input("请选择 (1-2): ", "2").strip()
        
        if choice == "1":
            image_path = safe_input("请输入图片文件路径: ", "").strip().strip('"')
            if not image_path:
                print("❌ 未输入文件路径")
                safe_pause()
                return
        else:
            # 查找当前目录中的图片文件
            image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.tiff']
            found_images = []
            for ext in image_extensions:
                found_images.extend(glob.glob(ext))
                found_images.extend(glob.glob(ext.upper()))
            
            if found_images:
                print("\n📂 发现以下图片文件:")
                for i, img in enumerate(found_images, 1):
                    print(f"  {i}. {img}")
                
                try:
                    user_choice = safe_input(f"请选择图片 (1-{len(found_images)}): ", "1")
                    idx = int(user_choice) - 1
                    image_path = found_images[idx]
                except (ValueError, IndexError):
                    print("❌ 选择无效，使用第一个图片文件")
                    image_path = found_images[0]
            else:
                print("❌ 当前目录没有找到图片文件")
                safe_pause()
                return
    
    # 检查文件是否存在
    if not os.path.exists(image_path):
        print(f"❌ 文件不存在: {image_path}")
        safe_pause()
        return
    
    # 检查是否为支持的图片格式
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    if not image_path.lower().endswith(supported_formats):
        print(f"❌ 不支持的文件格式。支持的格式: {', '.join(supported_formats)}")
        safe_pause()
        return
    
    print(f"\n🔄 开始处理图片...")
    print(f"📁 输入文件: {image_path}")
    
    # 创建基于图片名称的输出目录
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_dir = f"split_{base_name}"
    
    try:
        # 切分图片
        print(f"\n📂 输出目录: {output_dir}")
        split_image(image_path, output_dir=output_dir, max_height=1500)
        
        # 将切分后的图片合成PDF
        print(f"\n📑 开始生成PDF...")
        images_to_pdf(output_dir, base_name=base_name)
        
        print(f"\n🎉 处理完成！")
        print(f"📁 切分图片保存在: {output_dir}/")
        print(f"📄 PDF文件: {base_name}_merged.pdf")
        
    except Exception as e:
        print(f"❌ 处理过程中发生错误: {str(e)}")
    
    safe_pause()

if __name__ == "__main__":
    main() 