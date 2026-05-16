"""
个人仪表盘界面
展示用户的学习进度和统计数据
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from 核心模块.数据模型.data_store import DataStore
from 核心模块.任务设计.task_loader import TaskLoader


def render_personal_dashboard(user_id: str = "default_user"):
    """渲染个人仪表盘"""

    st.header("📊 个人仪表盘")
    st.markdown("追踪你的语言思维探索之旅。")

    if 'data_store' not in st.session_state:
        st.session_state.data_store = DataStore()
    if 'task_loader' not in st.session_state:
        st.session_state.task_loader = TaskLoader()

    data_store = st.session_state.data_store
    task_loader = st.session_state.task_loader

    # 获取用户统计
    stats = data_store.get_user_statistics(user_id)
    sessions = data_store.get_user_sessions(user_id)
    reflections = data_store.get_user_reflections(user_id)

    st.divider()

    # 核心指标卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🧩 完成任务", stats['tasks_completed'])
    with col2:
        st.metric("📝 思考会话", stats['total_sessions'])
    with col3:
        st.metric("🌍 使用语言", stats['languages_used'])
    with col4:
        st.metric("💭 反思记录", stats['reflections_count'])

    st.divider()

    # 语言使用分布
    st.subheader("🌍 语言使用分布")
    if stats['by_language']:
        lang_names = {"zh": "中文", "en": "英文", "ja": "日文", "de": "德文", "fr": "法文"}
        lang_data = pd.DataFrame({
            '语言': [lang_names.get(k, k) for k in stats['by_language'].keys()],
            '会话数': list(stats['by_language'].values())
        })

        # 饼图
        fig = px.pie(lang_data, values='会话数', names='语言', title='各语言使用比例')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("暂无数据，开始完成一些任务吧！")

    st.divider()

    # 自信度和难度趋势
    st.subheader("📈 学习趋势")

    if sessions:
        # 准备数据
        session_data = []
        for s in sessions:
            if s.confidence is not None or s.difficulty_rating is not None:
                session_data.append({
                    '日期': s.start_time.date(),
                    '自信度': s.confidence or 0,
                    '难度': s.difficulty_rating or 0,
                    '语言': s.language
                })

        if session_data:
            df = pd.DataFrame(session_data)

            # 按日期聚合
            daily_avg = df.groupby('日期').agg({
                '自信度': 'mean',
                '难度': 'mean'
            }).reset_index()

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 自信度趋势")
                st.line_chart(daily_avg, x='日期', y='自信度')
            with col2:
                st.markdown("### 感知难度趋势")
                st.line_chart(daily_avg, x='日期', y='难度')

    st.divider()

    # 任务类型分布
    st.subheader("🧩 任务类型分布")
    if stats['by_task']:
        task_names = {
            "logical_reasoning": "逻辑推理",
            "problem_solving": "问题解决",
            "moral_judgment": "道德判断",
            "creative_thinking": "创造性思维",
            "time_perception": "时间认知",
            "spatial_cognition": "空间认知",
            "decision_making": "决策判断"
        }

        # 解析任务类型
        type_counts = {}
        for task_id in stats['by_task'].keys():
            task_type = task_id.split('_')[0]
            type_name = task_names.get(task_type, task_type)
            type_counts[type_name] = type_counts.get(type_name, 0) + stats['by_task'][task_id]

        type_df = pd.DataFrame({
            '任务类型': list(type_counts.keys()),
            '完成次数': list(type_counts.values())
        })

        st.bar_chart(type_df, x='任务类型', y='完成次数')

    st.divider()

    # 最近活动
    st.subheader("📋 最近活动")

    if sessions:
        recent_sessions = sessions[:5]

        task_names_cache = {}
        tasks = task_loader.load_all_tasks()

        for s in recent_sessions:
            if s.task_id not in task_names_cache:
                task = tasks.get(s.task_id)
                if task and s.language in task.versions:
                    task_names_cache[s.task_id] = task.versions[s.language].title
                else:
                    task_names_cache[s.task_id] = s.task_id

            task_title = task_names_cache[s.task_id]
            lang_name = {"zh": "中文", "en": "英文", "ja": "日文", "de": "德文", "fr": "法文"}.get(s.language, s.language)

            with st.container(border=True):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.markdown(f"**{task_title}**")
                    st.caption(f"🌍 {lang_name} · {s.start_time.strftime('%Y-%m-%d %H:%M')}")
                with col2:
                    if s.confidence:
                        st.metric("自信度", f"{s.confidence:.0f}%")
                with col3:
                    if s.difficulty_rating:
                        st.metric("难度", f"{s.difficulty_rating:.0f}%")

    else:
        st.info("暂无活动记录")

    st.divider()

    # 成就系统
    st.subheader("🏆 成就")

    achievements = [
        {
            "id": "first_task",
            "name": "初探者",
            "description": "完成第一个思考任务",
            "icon": "🌱",
            "achieved": stats['total_sessions'] >= 1
        },
        {
            "id": "multilingual",
            "name": "多语言思考者",
            "description": "使用2种以上语言完成任务",
            "icon": "🌍",
            "achieved": stats['languages_used'] >= 2
        },
        {
            "id": "explorer",
            "name": "探索者",
            "description": "完成5个不同的任务",
            "icon": "🔍",
            "achieved": stats['tasks_completed'] >= 5
        },
        {
            "id": "reflective",
            "name": "反思者",
            "description": "写下3条反思记录",
            "icon": "💭",
            "achieved": stats['reflections_count'] >= 3
        },
        {
            "id": "master",
            "name": "思维大师",
            "description": "完成10个任务并记录5条反思",
            "icon": "🏆",
            "achieved": stats['tasks_completed'] >= 10 and stats['reflections_count'] >= 5
        }
    ]

    cols = st.columns(5)
    for i, ach in enumerate(achievements):
        with cols[i]:
            if ach['achieved']:
                st.success(f"{ach['icon']} **{ach['name']}**")
            else:
                st.info(f"{ach['icon']} {ach['name']}")
            st.caption(ach['description'])

    st.divider()

    # 导出数据
    st.subheader("📦 数据导出")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("导出所有数据为 JSON"):
            export_data = {
                "user_id": user_id,
                "export_date": datetime.now().isoformat(),
                "statistics": stats,
                "sessions": [s.__dict__ for s in sessions],
                "reflections": [r.__dict__ for r in reflections]
            }

            # 转换日期
            for s in export_data['sessions']:
                s['start_time'] = s['start_time'].isoformat() if s['start_time'] else None
                s['end_time'] = s['end_time'].isoformat() if s['end_time'] else None

            for r in export_data['reflections']:
                r['created_at'] = r['created_at'].isoformat()

            import json
            json_str = json.dumps(export_data, ensure_ascii=False, indent=2)
            st.download_button(
                "下载 JSON 文件",
                data=json_str,
                file_name=f"共语论数据_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )

    with col2:
        st.info("""
        💡 **隐私提示**：
        - 你的所有数据默认保存在本地
        - 你可以随时导出或删除自己的数据
        - 只有在你明确同意后，数据才会被匿名化用于研究
        """)
