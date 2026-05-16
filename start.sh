#!/bin/bash

echo "🧠 元语言计划 - MetaLanguage Project"
echo "====================================="
echo ""

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装，请先安装 Python3"
    exit 1
fi

echo "✅ Python3 已安装"

# 检查并安装依赖
echo "📦 检查依赖..."
pip3 show streamlit > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "🔧 安装依赖中..."
    pip3 install -r requirements.txt
fi

echo "✅ 依赖已安装"
echo ""
echo "🚀 启动 Web 应用..."
echo ""
echo "📱 应用将在浏览器中打开"
echo "🔗 访问地址: http://localhost:8501"
echo ""
echo "按 Ctrl+C 停止应用"
echo ""

# 启动应用
streamlit run app.py --server.port=8501
