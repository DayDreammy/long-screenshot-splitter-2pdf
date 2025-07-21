#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自动化发布脚本
用于创建新版本和发布
"""

import os
import sys
import subprocess
import re
from datetime import datetime
from version import __version__, get_version_info

def run_command(cmd):
    """运行命令并返回结果"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ 命令执行失败: {cmd}")
        print(f"错误: {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def check_git_status():
    """检查git状态"""
    status = run_command("git status --porcelain")
    if status:
        print("❌ 工作目录不干净，请先提交所有更改")
        print(status)
        sys.exit(1)
    print("✅ Git工作目录干净")

def update_changelog(version, changes):
    """更新CHANGELOG.md"""
    changelog_path = "CHANGELOG.md"
    if not os.path.exists(changelog_path):
        print("❌ CHANGELOG.md 不存在")
        sys.exit(1)
    
    # 读取现有内容
    with open(changelog_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到[Unreleased]部分并更新
    new_section = f"""## [{version}] - {datetime.now().strftime('%Y-%m-%d')}

### 新增
{chr(10).join(f'- {change}' for change in changes)}

## [Unreleased]"""
    
    # 替换[Unreleased]部分
    content = re.sub(r'## \[Unreleased\].*?(?=## \[|\Z)', new_section, content, flags=re.DOTALL)
    
    # 写回文件
    with open(changelog_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已更新 {changelog_path}")

def create_tag(version):
    """创建Git标签"""
    tag_name = f"v{version}"
    run_command(f"git add .")
    run_command(f'git commit -m "chore: release {version}"')
    run_command(f'git tag -a {tag_name} -m "Release {version}"')
    print(f"✅ 已创建标签 {tag_name}")

def push_release(version):
    """推送发布"""
    tag_name = f"v{version}"
    run_command("git push origin main")
    run_command(f"git push origin {tag_name}")
    print(f"✅ 已推送发布 {version}")

def build_executable():
    """构建可执行文件"""
    print("🔨 开始构建可执行文件...")
    run_command("python -m pip install pyinstaller")
    run_command('pyinstaller --onefile --console --name="长截图切分工具" --icon=NONE split_screenshot.py')
    print("✅ 可执行文件构建完成")

def main():
    """主函数"""
    print("🚀 开始发布流程...")
    
    # 获取版本信息
    version_info = get_version_info()
    current_version = version_info["version"]
    
    print(f"📦 当前版本: {current_version}")
    
    # 检查git状态
    check_git_status()
    
    # 询问是否继续
    confirm = input(f"确认发布版本 {current_version}? (y/N): ")
    if confirm.lower() != 'y':
        print("❌ 发布已取消")
        sys.exit(0)
    
    try:
        # 构建可执行文件
        build_executable()
        
        # 创建标签
        create_tag(current_version)
        
        # 推送发布
        push_release(current_version)
        
        print(f"🎉 版本 {current_version} 发布成功！")
        print(f"📁 可执行文件位置: dist/长截图切分工具.exe")
        print(f"🌐 GitHub Actions 将自动创建发布页面")
        
    except Exception as e:
        print(f"❌ 发布过程中出现错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 