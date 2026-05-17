"""
推理任务库界面
展示和执行各类认知任务
"""
import streamlit as st
import time
from datetime import timedelta
from pathlib import Path
import sys

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from 核心模块.任务设计.task_loader import TaskLoader
from 核心模块.语言认知.language_switcher import LanguageSwitcher
from 核心模块.数据模型.schemas import TaskType, Difficulty
from 核心模块.数据模型.data_store import DataStore


def render_task_library(user_id: str = "default_user"):
    """渲染任务库界面"""

    st.header("🧩 推理任务库")
    st.markdown("选择不同类型的认知任务，用不同语言思考，探索语言如何塑造你的思维。")

    # 初始化
    if 'task_loader' not in st.session_state:
        st.session_state.task_loader = TaskLoader()
    if 'data_store' not in st.session_state:
        st.session_state.data_store = DataStore()
    if 'switcher' not in st.session_state:
        st.session_state.switcher = LanguageSwitcher()

    loader = st.session_state.task_loader
    data_store = st.session_state.data_store
    switcher = st.session_state.switcher

    # 任务统计
    stats = loader.get_task_statistics()
    col1, col2, col3 = st.columns(3)
    col1.metric("总任务数", stats['total'])
    col2.metric("支持语言", len(stats['languages']))
    col3.metric("任务类型", len(stats['by_type']))

    st.divider()

    # 任务过滤
    col1, col2, col3 = st.columns(3)

    task_types = {t.value: t.name for t in TaskType}
    task_type_names = {
        "logical_reasoning": "逻辑推理",
        "problem_solving": "问题解决",
        "moral_judgment": "道德判断",
        "creative_thinking": "创造性思维",
        "time_perception": "时间认知",
        "spatial_cognition": "空间认知",
        "decision_making": "决策判断"
    }

    with col1:
        selected_type = st.selectbox(
            "任务类型",
            options=["全部"] + list(task_types.keys()),
            format_func=lambda x: "全部类型" if x == "全部" else task_type_names.get(x, x)
        )

    with col2:
        difficulty_names = {d.value: d.name for d in Difficulty}
        difficulty_display = {
            "beginner": "入门级",
            "intermediate": "进阶级",
            "advanced": "挑战级"
        }
        selected_difficulty = st.selectbox(
            "难度",
            options=["全部"] + list(difficulty_names.keys()),
            format_func=lambda x: "全部难度" if x == "全部" else difficulty_display.get(x, x)
        )

    with col3:
        selected_language = st.selectbox(
            "思考语言",
            options=["zh", "en"],
            format_func=lambda x: "中文" if x == "zh" else "English"
        )

    # 加载任务
    tasks = loader.load_all_tasks()
    filtered_tasks = list(tasks.values())

    if selected_type != "全部":
        filtered_tasks = [t for t in filtered_tasks if t.task_type.value == selected_type]
    if selected_difficulty != "全部":
        filtered_tasks = [t for t in filtered_tasks if t.difficulty.value == selected_difficulty]
    filtered_tasks = [t for t in filtered_tasks if selected_language in t.versions]

    if not filtered_tasks:
        st.info("没有找到符合条件的任务")
        return

    st.divider()
    st.subheader(f"找到 {len(filtered_tasks)} 个任务")

    # 任务列表
    for i, task in enumerate(filtered_tasks):
        task_content = task.versions[selected_language]
        type_display = task_type_names.get(task.task_type.value, task.task_type.value)
        diff_display = difficulty_display.get(task.difficulty.value, task.difficulty.value)

        with st.expander(f"📋 {task_content.title} — {type_display} · {diff_display}"):
            st.markdown(f"**描述：** {task_content.description}")

            if task.reference:
                st.caption(f"📚 来源：{task.reference}")

            if task.tags:
                st.markdown(" ".join([f"`{tag}`" for tag in task.tags]))

            col_start, col_compare = st.columns(2)
            with col_start:
                if st.button(f"开始任务", key=f"start_{task.task_id}"):
                    st.session_state.current_task = task
                    st.session_state.current_language = selected_language
                    st.session_state.show_task = True
                    st.rerun()

            with col_compare:
                other_lang = "en" if selected_language == "zh" else "zh"
                if other_lang in task.versions:
                    if st.button(f"双语对比", key=f"compare_{task.task_id}"):
                        st.session_state.current_task = task
                        st.session_state.compare_mode = True
                        st.rerun()

    # 显示任务执行界面
    if st.session_state.get('show_task', False):
        _render_task_execution(user_id)

    # 显示双语对比界面
    if st.session_state.get('compare_mode', False):
        _render_comparison_mode()


def _render_task_execution(user_id: str):
    """渲染任务执行界面"""
    task = st.session_state.current_task
    lang = st.session_state.current_language
    loader = st.session_state.task_loader
    data_store = st.session_state.data_store

    task_content = task.versions[lang]

    with st.container(border=True):
        st.subheader(f"📝 {task_content.title}")
        st.markdown(f"**{task_content.description}**")

        # 语言切换引导
        if not st.session_state.get('switch_complete', False):
            st.info("🌍 在开始任务前，让我们先切换到目标语言模式...")

            switcher = LanguageSwitcher()
            steps = switcher.get_switch_steps(lang)

            current_step = st.session_state.get('current_switch_step', 0)

            if current_step < len(steps):
                step = steps[current_step]
                progress = (current_step + 1) / len(steps)

                st.progress(progress)
                st.markdown(f"### 步骤 {step['step']}/{len(steps)}：{step['title']}")
                st.info(step['instruction'])

                if step.get('content'):
                    st.markdown(f"> {step['content']}")

                if st.button("下一步 →", key=f"switch_next_{current_step}"):
                    st.session_state.current_switch_step = current_step + 1
                    st.rerun()
            else:
                st.session_state.switch_complete = True
                st.success("✅ 语言切换完成！现在开始用目标语言思考。")
                st.rerun()
        else:
            # 开始任务计时
            if 'start_time' not in st.session_state:
                st.session_state.start_time = time.time()
                # 在数据库中开始会话
                session = data_store.start_session(
                    user_id=user_id,
                    task_id=task.task_id,
                    language=lang
                )
                st.session_state.current_session_id = session.session_id

            elapsed = time.time() - st.session_state.start_time
            st.caption(f"⏱ 已用时：{timedelta(seconds=int(elapsed))}")

            # 显示问题
            st.markdown("---")
            st.markdown(f"**问题：**")
            st.markdown(task_content.question)

            # 提示
            if task_content.hint and st.toggle("显示提示"):
                st.info(f"💡 {task_content.hint}")

            # 答案输入
            st.markdown("---")
            user_answer = None

            if task_content.options:
                user_answer = st.radio("你的答案：", options=task_content.options)
            else:
                user_answer = st.text_area("你的答案：", height=150)

            # 思考过程记录
            thinking_process = st.text_area(
                "💭 思考过程记录（可选）：",
                placeholder="描述一下你是如何得出这个答案的...",
                height=100
            )

            col1, col2 = st.columns(2)
            with col1:
                confidence = st.slider("自信度 (%)", 0, 100, 50)
            with col2:
                difficulty_rating = st.slider("感知难度", 0, 100, 50)

            # 提交答案
            if st.button("提交答案", type="primary", use_container_width=True):
                # 检查是否正确
                is_correct = None
                if task_content.correct_answer:
                    is_correct = (user_answer == task_content.correct_answer)

                # 保存到数据库
                data_store.complete_session(
                    session_id=st.session_state.current_session_id,
                    answer=user_answer,
                    thinking_process=thinking_process,
                    confidence=confidence,
                    difficulty_rating=difficulty_rating,
                    is_correct=is_correct
                )

                # 显示结果
                st.markdown("---")
                if is_correct is not None:
                    if is_correct:
                        st.success("✅ 回答正确！")
                    else:
                        st.error(f"❌ 回答不正确。正确答案是：{task_content.correct_answer}")
                else:
                    st.success("✅ 答案已记录！")

                st.balloons()

                if st.button("完成，返回任务库"):
                    st.session_state.show_task = False
                    st.session_state.switch_complete = False
                    if 'current_switch_step' in st.session_state:
                        del st.session_state.current_switch_step
                    if 'start_time' in st.session_state:
                        del st.session_state.start_time
                    st.rerun()


def _render_comparison_mode():
    """渲染双语对比模式"""
    task = st.session_state.current_task

    st.subheader("🌍 双语对比模式")
    st.info("用两种语言阅读相同的问题，注意你对问题的理解和感受有什么不同。")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🇨🇳 中文版本")
        zh_content = task.versions.get('zh')
        if zh_content:
            st.markdown(f"**{zh_content.title}**")
            st.markdown(zh_content.description)
            st.markdown("---")
            st.markdown(zh_content.question)
            if zh_content.options:
                for opt in zh_content.options:
                    st.markdown(f"- {opt}")

    with col2:
        st.markdown("### 🇺🇸 English Version")
        en_content = task.versions.get('en')
        if en_content:
            st.markdown(f"**{en_content.title}**")
            st.markdown(en_content.description)
            st.markdown("---")
            st.markdown(en_content.question)
            if en_content.options:
                for opt in en_content.options:
                    st.markdown(f"- {opt}")

    st.divider()
    st.subheader("💭 你的观察")

    observations = st.text_area(
        "阅读两个版本后，你注意到什么差异？",
        placeholder="例如：中文版本让我更关注...，英文版本让我更关注...",
        height=100
    )

    surprising = st.text_area(
        "有什么让你感到意外的？",
        placeholder="例如：我没想到同一个问题用不同语言读起来感觉这么不同...",
        height=80
    )

    insights = st.text_area(
        "你获得了什么新的洞见？",
        placeholder="例如：原来语言真的会影响我思考问题的方式...",
        height=80
    )

    if st.button("保存反思"):
        # 这里可以保存到数据库
        st.success("✅ 反思已保存！")
