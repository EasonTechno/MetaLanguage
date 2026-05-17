"""
语言切换练习界面
引导用户进行沉浸式语言切换练习
"""
import streamlit as st
import time
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from 核心模块.语言认知.language_switcher import LanguageSwitcher
from 核心模块.语言认知.language_features import LANGUAGE_FEATURES, get_supported_languages


def render_language_switch_practice():
    """渲染语言切换练习界面"""

    st.header("🌍 语言切换练习")
    st.markdown("""
    通过沉浸式引导，帮助你在不同语言间平滑切换思考模式。
    研究表明，语言不仅仅是交流工具，它还塑造着我们感知世界的方式。
    """)

    if 'switcher' not in st.session_state:
        st.session_state.switcher = LanguageSwitcher()

    switcher = st.session_state.switcher

    st.divider()

    # 选择目标语言
    lang_names = {
        "zh": "中文",
        "en": "英文",
        "ja": "日文",
        "de": "德文",
        "fr": "法文"
    }

    col1, col2 = st.columns(2)
    with col1:
        from_lang = st.selectbox(
            "从哪种语言切换",
            options=get_supported_languages(),
            format_func=lambda x: lang_names.get(x, x),
            index=0
        )

    with col2:
        to_lang = st.selectbox(
            "切换到哪种语言",
            options=[l for l in get_supported_languages() if l != from_lang],
            format_func=lambda x: lang_names.get(x, x),
            index=0
        )

    # 显示语言对比
    with st.expander("📊 查看两种语言的认知特征对比", expanded=True):
        comparison = switcher.compare_languages(from_lang, to_lang)
        st.markdown(f"### {comparison['languages'][0]} vs {comparison['languages'][1]}")

        if comparison['key_differences']:
            for diff in comparison['key_differences']:
                st.markdown(f"**{diff['feature']}**")
                col_a, col_b = st.columns(2)
                col_a.info(diff[from_lang])
                col_b.info(diff[to_lang])
                st.caption(f"💡 {diff['implication']}")
                st.markdown("---")
        else:
            st.info("两种语言在关键认知特征上较为相似")

    st.divider()

    if st.button("🚀 开始语言切换练习", type="primary", use_container_width=True):
        st.session_state.practice_mode = True
        st.session_state.switch_step = 0
        st.rerun()

    # 练习流程
    if st.session_state.get('practice_mode', False):
        _render_practice_flow(to_lang)


def _render_practice_flow(target_language: str):
    """渲染语言切换练习流程"""
    switcher = st.session_state.switcher
    steps = switcher.get_switch_steps(target_language)

    current_step = st.session_state.get('switch_step', 0)

    if current_step < len(steps):
        step = steps[current_step]
        progress = (current_step + 1) / len(steps)

        st.markdown("---")
        st.progress(progress)

        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            with st.container(border=True):
                st.markdown(f"## 步骤 {step['step']}/{len(steps)}")
                st.markdown(f"### 🎯 {step['title']}")
                st.markdown("---")
                st.markdown(step['instruction'])

                if step.get('content'):
                    st.markdown("---")
                    st.markdown("### 📖 沉浸文本")
                    st.markdown(f"> {step['content']}")

                st.markdown("---")
                st.caption(f"⏱ 建议用时：{step.get('duration', 30)} 秒")

                # 计时器
                if st.button("✅ 完成这一步", use_container_width=True):
                    st.session_state.switch_step = current_step + 1
                    st.rerun()

    else:
        st.success("""
        ## 🎉 语言切换完成！

        现在你已经准备好了用目标语言思考。记住：

        - ❌ **不要在心里翻译** — 这会降低你的思考速度和流畅度
        - ✅ **直接用目标语言思考** — 让概念直接和目标语言关联
        - ✅ **如果卡住了，用最简单的词汇表达** — 沟通比完美更重要

        现在你可以去「推理任务库」用新的语言完成一些任务体验！
        """)

        st.balloons()

        if st.button("重新练习"):
            st.session_state.practice_mode = False
            st.session_state.switch_step = 0
            st.rerun()
