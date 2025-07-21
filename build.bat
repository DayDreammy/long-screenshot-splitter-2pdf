@echo off
chcp 65001 >nul
echo ================================================================
echo 🔧 长截图切分工具 - 自动打包脚本
echo ================================================================

echo.
echo 📦 正在检查和安装依赖...
pip install -r requirements.txt
pip install pyinstaller

echo.
echo 🔨 开始打包程序（控制台版本）...
pyinstaller --onefile --console --name="长截图切分工具" --icon=NONE split_screenshot.py

echo.
echo 📁 创建输出目录...
if not exist "发布版本" mkdir "发布版本"
copy "dist\长截图切分工具.exe" "发布版本\"

echo.
echo ✅ 打包完成！
echo 📁 可执行文件位置: 发布版本\长截图切分工具.exe
echo.
echo 📖 使用方法：
echo   1. 双击运行程序（会显示命令行窗口）
echo   2. 或者将图片文件拖拽到程序图标上
echo   3. 程序会自动切分图片并生成PDF
echo   4. 处理完成后按回车键退出
echo.
echo 💡 提示：控制台版本支持完整的交互功能！
echo.
pause 