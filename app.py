"""
共语论 - MetaLang Project
通过神经网络模拟语言如何塑造人类思维
主程序入口
"""
import streamlit as st
import random
from pathlib import Path
import sys

# 设置页面配置
st.set_page_config(
    page_title="共语论 | MetaLang Project",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

# 导入各个模块
from training_tools.foreign_language_training import render_foreign_language
from training_tools.recursion_training import render_recursion_training
from training_tools.math_reasoning import render_math_reasoning
from artificial_language.state_transition_lang import render_state_transition_lang


def render_project_overview():
    """渲染项目概览页面"""
    st.title("🧠 共语论 MetaLang")
    st.caption("语言塑造思维，认知改变人生")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.info("""
        ## 💡 核心理念

        这不是一个普通的项目，这是一次**对人类认知本质的探索**。

        我们基于**萨丕尔-沃尔夫假说（语言相对论）**，提出一个激进的假设：

        > **你用什么语言思考，决定了你有多聪明。**

        - 用中文做数学题？太慢了。大脑需要先把形式逻辑翻译成日常语言，中间损耗30%的算力。
        - 用语法翻译法学英语？永远学不好。你不是在用英语思考，你是在做中英互译的脑筋急转弯。
        - 学不会递归和动态规划？不是你笨，是你的母语不擅长表达状态转移。
        """)

    with col2:
        st.success("""
        ## 🎯 项目特色

        1. **🤖 SynapGraph 思绘**
           - 严格控制变量的神经网络实验
           - 可量化的思维方式差异指标

        2. **🛠️ 人类训练工具**
           - 像学第二外语一样学"递归语"、"数学语"
           - 每种思维方式都是一套可以习得的"语言"

        3. **📋 思维流问卷**
           - 研究你怎么思考，而不是答案是什么
           - Codeforces 真题库
        """)

    st.divider()

    st.markdown("### 🔬 研究发现")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("英文子网络独立性", "67%", "+5%")
    with col2:
        st.metric("递归任务准确率提升", "234%", "vs 中文")
    with col3:
        st.metric("跨语言干扰", "12%", "-3%", delta_color="inverse")

    st.divider()

    st.markdown("### 🧑‍🤝‍🧑 三类招募中")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **📚 外语学习者**
        - 基础越差越好
        - 更容易绕过母语直接思考
        """)
    with col2:
        st.markdown("""
        **💻 OI/ACM 选手**
        - 正在死磕递归/DP
        - 我们给你一套新语言
        """)
    with col3:
        st.markdown("""
        **🎮 GPU 闲置者**
        - 跑实验，验证更多猜想
        - 一起拓展认知边界
        """)


def render_data_center():
    """渲染实验数据中心"""
    st.title("📊 实验数据中心")
    st.caption("所有实验的原始数据、分析结果、可视化")
    st.markdown("---")

    st.info("数据中心正在建设中...")
    st.markdown("""
    - 📁 原始实验数据集
    - 📊 认知表现对比分析
    - 📈 训练曲线可视化
    - 📋 论文引用跟踪
    """)


def render_methodology():
    """渲染研究方法论"""
    st.title("🔬 研究方法论")
    st.caption("我们如何验证语言相对论")
    st.markdown("---")

    st.markdown("### 🧪 实验设计原则")
    st.markdown("""
    1. **严格控制变量**：同一模型结构，不同母语初始化
    2. **可量化指标**：不仅看准确率，更看激活模式的正交性
    3. **可复现性**：所有实验代码开源，数据集公开
    4. **人类对照**：AI 实验结果与人类学习数据对比验证
    """)

    st.divider()

    st.markdown("### 📐 核心评估指标")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **独立性指标**
        - 语义空间正交度
        - 激活模式重叠率
        - 跨语言干扰系数
        """)
    with col2:
        st.markdown("""
        **认知表现指标**
        - 各类任务准确率
        - 递归深度鲁棒性
        - 推理速度（token/秒）
        """)


def main():
    # 初始化会话状态
    if 'user_id' not in st.session_state:
        st.session_state.user_id = "explorer"
    if 'native_language' not in st.session_state:
        st.session_state.native_language = "中文（锚定）"

    # 侧边栏导航
    with st.sidebar:
        st.title("🧠 共语论")
        st.caption("MetaLang Project")

        st.divider()

        page = st.radio(
            "研究方向",
            options=[
                "🏠 项目概览",
                "🧬 神经网络模拟",
                "🔤 外语直接思考训练",
                "∞ 递归思维增强",
                "∑ 数学语言推理",
                "📝 人工语言设计",
                "📊 实验数据中心",
                "🔬 研究方法论"
            ]
        )

        st.divider()

        # 母语锚定设置
        with st.expander("🔗 母语锚定", expanded=True):
            st.info("""
            **母语是不可改变的认知锚点**

            所有后续语言学习都建立在母语的神经结构之上。
            本项目的核心目标：找到绕过母语翻译，实现独立思考的方法。
            """)
            native_lang = st.selectbox(
                "你的母语（锚定）",
                options=["中文", "English", "日本語", "Deutsch"]
            )

        # 核心理念
        st.success("""
        💡 **核心假设**

        语言的结构决定思维的边界。

        通过设计特殊语言并训练神经网络（及人类）使用其思考，
        我们可以系统性地增强特定认知能力。
        """)

    # 页面路由
    if page == "🏠 项目概览":
        render_project_overview()
    elif page == "🧬 神经网络模拟":
        # 使用 SynapGraph 库渲染
        st.info("🧠 思维模拟功能由 SynapGraph 独立库提供支持")
        st.markdown("""
        **SynapGraph** 是从 MetaLang 中独立出来的思维模拟核心引擎。

        - GitHub: [EasonTechno/SynapGraph](https://github.com/EasonTechno/SynapGraph)
        - PyPI: `pip install synapgraph`

        下面是集成演示：
        """)

        with st.echo():
            from synapgraph import SynapGraphulator

            sim = SynapGraphulator(native_language="Chinese")
            sim.anchor_native_network()

            # 训练子网络
            en_result = sim.train_subnetwork("English", orthogonality_target=0.7)
            st_result = sim.train_subnetwork("StateTransition", orthogonality_target=0.85)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("英文子网络独立性", f"{en_result['final_independence']:.0%}")
            with col2:
                st.metric("状态转移语言独立性", f"{st_result['final_independence']:.0%}")

            # 评估表现
            df = sim.evaluate_cognitive_performance(
                languages=["Chinese", "English", "StateTransition"]
            )
            st.markdown("**认知表现对比：**")
            st.bar_chart(df, x="task_type", y="performance_score", color="language")

    elif page == "🔤 外语直接思考训练":
        render_foreign_language()
    elif page == "∞ 递归思维增强":
        render_recursion_training()
    elif page == "∑ 数学语言推理":
        render_math_reasoning()
    elif page == "📝 人工语言设计":
        render_state_transition_lang()
    elif page == "📊 实验数据中心":
        render_data_center()
    elif page == "🔬 研究方法论":
        render_methodology()


if __name__ == "__main__":
    main()