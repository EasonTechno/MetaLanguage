"""
反思记录界面
记录和对比不同语言下的思考体验
"""
import streamlit as st
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from 核心模块.数据模型.data_store import DataStore
from 核心模块.任务设计.task_loader import TaskLoader


def render_reflection_notes(user_id: str = "default_user"):
    """渲染反思记录界面"""

    st.header("💭 反思记录")
    st.markdown("""
    记录你在不同语言下思考同一问题的体验和感受。
    通过对比和反思，你会发现语言如何微妙地塑造着你的思维。
    """)

    if 'data_store' not in st.session_state:
        st.session_state.data_store = DataStore()
    if 'task_loader' not in st.session_state:
        st.session_state.task_loader = TaskLoader()

    data_store = st.session_state.data_store
    task_loader = st.session_state.task_loader

    st.divider()

    tab1, tab2 = st.tabs(["📝 新建反思", "📋 历史记录"])

    with tab1:
        _render_new_reflection(user_id, data_store, task_loader)

    with tab2:
        _render_reflection_history(user_id, data_store)


def _render_new_reflection(user_id: str, data_store: DataStore, task_loader: TaskLoader):
    """渲染新建反思表单"""

    st.subheader("创建新的反思记录")

    # 选择对比的任务
    tasks = task_loader.load_all_tasks()
    task_options = []
    for task_id, task in tasks.items():
        # 找到有多语言版本的任务
        if len(task.versions) >= 2:
            # 获取第一个版本的标题
            first_lang = list(task.versions.keys())[0]
            title = task.versions[first_lang].title
            langs = ", ".join(task.versions.keys())
            task_options.append((task_id, f"{title} ({langs})"))

    if not task_options:
        st.info("暂无可用于对比的多语言任务")
        return

    selected_task_id = st.selectbox(
        "选择要反思的任务",
        options=[t[0] for t in task_options],
        format_func=lambda x: dict(task_options).get(x, x)
    )

    # 选择对比的语言
    task = tasks[selected_task_id]
    available_langs = list(task.versions.keys())

    if len(available_langs) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            lang1 = st.selectbox("语言 A", options=available_langs, index=0)
        with col2:
            lang2 = st.selectbox("语言 B", options=[l for l in available_langs if l != lang1], index=0)

        # 显示两个语言版本的问题
        st.markdown("---")
        st.subheader("📖 任务内容对比")

        col_a, col_b = st.columns(2)
        lang_names = {"zh": "中文", "en": "英文", "ja": "日文", "de": "德文", "fr": "法文"}

        with col_a:
            st.markdown(f"### {lang_names.get(lang1, lang1)}")
            content1 = task.versions[lang1]
            st.markdown(f"**{content1.title}**")
            st.markdown(content1.description)
            st.markdown("---")
            st.markdown(content1.question)

        with col_b:
            st.markdown(f"### {lang_names.get(lang2, lang2)}")
            content2 = task.versions[lang2]
            st.markdown(f"**{content2.title}**")
            st.markdown(content2.description)
            st.markdown("---")
            st.markdown(content2.question)

        # 反思问题
        st.markdown("---")
        st.subheader("💭 你的反思")

        question_text = st.text_area(
            "你思考的问题：",
            value=content1.title,
            disabled=True
        )

        observations = st.text_area(
            "🔍 你观察到什么差异？",
            placeholder="例如：用中文思考时我更关注...，用英文思考时更关注...",
            height=120
        )

        surprising = st.text_area(
            "😮 有什么让你感到意外的？",
            placeholder="例如：我没想到同一个问题用不同语言读起来感觉这么不同...",
            height=100
        )

        insights = st.text_area(
            "💡 你获得了什么新的洞见？",
            placeholder="例如：原来语言真的会影响我思考问题的方式...",
            height=100
        )

        if st.button("保存反思记录", type="primary", use_container_width=True):
            if observations:
                data_store.save_reflection(
                    user_id=user_id,
                    session_ids=[],  # 可以关联实际会话ID
                    languages_compared=[lang1, lang2],
                    question=question_text,
                    observations=observations,
                    surprising_aspects=surprising,
                    insights=insights
                )
                st.success("✅ 反思记录已保存！")
                st.balloons()
            else:
                st.warning("请至少填写观察到的差异")


def _render_reflection_history(user_id: str, data_store: DataStore):
    """渲染历史反思记录"""

    reflections = data_store.get_user_reflections(user_id)

    if not reflections:
        st.info("暂无反思记录")
        return

    st.subheader(f"共 {len(reflections)} 条反思记录")

    for i, note in enumerate(reflections):
        with st.expander(f"📝 {note.question} — {note.created_at.strftime('%Y-%m-%d %H:%M')}"):
            langs = ", ".join(note.languages_compared)
            st.caption(f"🌍 对比语言：{langs}")

            st.markdown("### 🔍 观察到的差异")
            st.markdown(note.observations)

            if note.surprising_aspects:
                st.markdown("### 😮 意外发现")
                st.markdown(note.surprising_aspects)

            if note.insights:
                st.markdown("### 💡 新的洞见")
                st.markdown(note.insights)

    # 统计可视化
    st.divider()
    st.subheader("📊 反思统计")

    # 语言使用统计
    all_langs = []
    for note in reflections:
        all_langs.extend(note.languages_compared)

    if all_langs:
        from collections import Counter
        lang_counts = Counter(all_langs)
        df = pd.DataFrame({
            '语言': [lang_names.get(k, k) for k in lang_counts.keys()],
            '次数': list(lang_counts.values())
        })
        lang_names = {"zh": "中文", "en": "英文", "ja": "日文", "de": "德文", "fr": "法文"}
        st.bar_chart(df, x='语言', y='次数')

        col1, col2, col3 = st.columns(3)
        col1.metric("总反思数", len(reflections))
        col2.metric("涉及语言数", len(lang_counts))
        col3.metric("总对比次数", sum(lang_counts.values()) // 2)
