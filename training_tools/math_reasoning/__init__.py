"""
人类训练工具 - 数学语言推理
目标：用形式逻辑替代中文的模糊思维
"""
import streamlit as st


def render_math_reasoning():
    """渲染数学语言推理训练页面"""

    st.title("∑ 数学语言推理")
    st.caption("目标：用形式逻辑替代中文的模糊思维")
    st.markdown("---")

    module = st.selectbox(
        "训练模块",
        options=[
            "🧐 中文思维的BUG",
            "🔤 形式逻辑入门",
            "🎯 逻辑谬误识别训练",
            "🧠 公理化思维培养"
        ]
    )

    st.markdown("---")

    if module == "🧐 中文思维的BUG":
        render_chinese_bugs()
    elif module == "🔤 形式逻辑入门":
        render_formal_logic()
    elif module == "🎯 逻辑谬误识别训练":
        render_fallacy_detection()
    elif module == "🧠 公理化思维培养":
        render_axiomatic_thinking()


def render_chinese_bugs():
    """展示中文思维的固有问题"""

    st.info("""
    💡 **核心问题**

    自然语言（包括中文）本质是**模糊的、联想式的、说服导向的**。

    它是为了社交、讲故事、说服别人进化的，不是为了精确推理。

    当你用中文思考数学和逻辑问题时，你在用螺丝刀敲钉子。
    """)

    st.markdown("### 🐛 BUG 1：歧义性")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 中文表达")
        st.code("""
        "我喜欢一个人。"

        可能的意思：
        1. 我喜欢某一个特定的人
        2. 我喜欢独自待着

        中文读者靠语境猜，
        但数学里不允许猜！
        """)

    with col2:
        st.markdown("#### 形式语言表达")
        st.code("""
        意思1:
        ∃x (Person(x) ∧ Like(我, x))

        意思2:
        Prefer(我, Alone)

        没有歧义！
        是什么就是什么。
        """)

    st.divider()

    st.markdown("### 🐛 BUG 2：偷换概念")

    st.code("""
    经典诡辩：
    "你没有丢掉的东西，就是你拥有的东西。
     你没有丢掉角，所以你有角。"

    问题在哪？
    "丢掉"的概念被偷换了：
    - 第一个"丢掉" = 原本有的东西失去了
    - 第二个"丢掉" = 字面上失去

    中文里靠同一个字就能偷换概念，
    形式语言里根本做不到！
    """)

    st.divider()

    st.markdown("### 🐛 BUG 3：联想代替演绎")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 中文思维模式")
        st.code("""
        道生一，
        一生二，
        二生三，
        三生万物。

        听起来很有道理，
        但你能用它算出
        123 × 456 等于几吗？

        不能。
        因为这是**类比联想**，
        不是**逻辑演绎**。
        """)

    with col2:
        st.markdown("#### 数学思维模式")
        st.code("""
        皮亚诺公理：
        1. 0 是自然数
        2. 每个自然数有后继
        3. 0 不是任何数的后继
        4. 不同的数有不同的后继
        5. 归纳原理

        听起来很枯燥，
        但你能用它证明
        任何算术定理！

        这就是**公理化演绎**。
        """)

    st.success("""
    🎯 **训练目标**

    不是让你放弃中文，而是：

    **当你需要精确推理时，切换到"形式语言模式"；
    当你需要交流和表达时，再切换回中文模式。**

    能自由在两种模式间切换，才是真正的聪明人。
    """)


def render_formal_logic():
    """形式逻辑入门"""

    st.info("""
    💡 **形式逻辑**是数学家和程序员的母语。

    它没有歧义、没有修辞、没有感情。
    只有：精确的定义 + 严格的推理规则。
    """)

    st.markdown("### 🔤 基本符号")

    symbols = {
        "∀": "全称量词（所有）",
        "∃": "存在量词（存在）",
        "∧": "与（并且）",
        "∨": "或（或者）",
        "¬": "非（不是）",
        "→": "蕴含（如果...那么）",
        "↔": "等价（当且仅当）",
        "∴": "所以"
    }

    col1, col2 = st.columns(2)

    with col1:
        for symbol, meaning in list(symbols.items())[:4]:
            st.markdown(f"`{symbol}` = **{meaning}**")

    with col2:
        for symbol, meaning in list(symbols.items())[4:]:
            st.markdown(f"`{symbol}` = **{meaning}**")

    st.divider()

    st.markdown("### ✏️ 翻译练习：中文 → 形式逻辑")

    exercises = {
        "所有人都会死": "∀x (人(x) → 会死(x))",
        "苏格拉底是人": "人(苏格拉底)",
        "所以苏格拉底会死": "∴ 会死(苏格拉底)",
        "不是所有鸟都会飞": "¬∀x (鸟(x) → 会飞(x))",
        "存在会飞的哺乳动物": "∃x (哺乳动物(x) ∧ 会飞(x))"
    }

    chinese = st.selectbox("选择中文句子", list(exercises.keys()))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 中文句子")
        st.success(f"**{chinese}**")

    with col2:
        st.markdown("#### 形式逻辑翻译")
        st.code(exercises[chinese], language="text")

    st.divider()

    st.markdown("### 🧠 三段论推理练习")

    syllogisms = [
        {
            "name": "经典三段论",
            "premise1": "∀x (人(x) → 会死(x))",
            "premise2": "人(苏格拉底)",
            "conclusion": "会死(苏格拉底)",
            "valid": True
        },
        {
            "name": "肯定后件谬误",
            "premise1": "∀x (鸟(x) → 会飞(x))",
            "premise2": "会飞(蝙蝠)",
            "conclusion": "鸟(蝙蝠)",
            "valid": False
        }
    ]

    selected = st.selectbox("选择推理", [s["name"] for s in syllogisms])
    syllogism = next(s for s in syllogisms if s["name"] == selected)

    st.markdown("#### 推理形式")
    st.code(f"""
    前提1：{syllogism['premise1']}
    前提2：{syllogism['premise2']}
    ──────────────────────────
    结论：  {syllogism['conclusion']}
    """)

    user_judgment = st.radio("这个推理有效吗？", ["有效", "无效"], horizontal=True)

    if st.button("检查答案"):
        if (user_judgment == "有效" and syllogism["valid"]) or \
           (user_judgment == "无效" and not syllogism["valid"]):
            st.success("✅ 正确！你开始用形式逻辑思考了！")
        else:
            st.error(f"❌ 不对。这个推理是{'有效' if syllogism['valid'] else '无效'}的。")

        if not syllogism["valid"]:
            st.warning("""
            💡 错误原因：肯定后件

            "所有鸟会飞" 不等于 "所有会飞的是鸟"。

            中文里经常有人用这种方式诡辩，
            但形式逻辑一眼就能看穿！
            """)


def render_fallacy_detection():
    """逻辑谬误识别训练"""

    st.info("""
    💡 **训练价值**

    互联网上90%的争论都源于逻辑谬误。

    学会识别这些谬误，你就能：
    - 不被别人忽悠
    - 自己不犯低级错误
    - 瞬间看穿键盘侠的诡辩
    """)

    fallacies = [
        {
            "name": "偷换概念",
            "description": "同一个词在论证中表达不同的意思",
            "example": "中国的大学遍布全国，清华大学是中国的大学，所以清华大学遍布全国。",
            "analysis": "第一个'中国的大学'是整体概念，第二个是个体概念"
        },
        {
            "name": "人身攻击",
            "description": "攻击对方的人，而不是对方的论证",
            "example": "你这么穷，你的经济观点肯定错。",
            "analysis": "经济观点正确与否和说话者的财富没有关系"
        },
        {
            "name": "稻草人谬误",
            "description": "歪曲对方的观点，然后攻击歪曲后的版本",
            "example": "你主张减少军费？那你就是不爱国！",
            "analysis": "减少军费不等于不爱国，攻击者树立了一个稻草人"
        },
        {
            "name": "诉诸权威",
            "description": "用权威人士的观点代替论证",
            "example": "爱因斯坦信上帝，所以上帝一定存在。",
            "analysis": "物理学权威不代表神学权威"
        },
        {
            "name": "虚假两难",
            "description": "只给两个选项，实际上还有更多可能",
            "example": "你要么支持我们，要么就是敌人。",
            "analysis": "还可以中立，还可以部分支持部分反对"
        }
    ]

    st.markdown("### 🎮 谬误识别游戏")

    if 'current_fallacy' not in st.session_state:
        st.session_state.current_fallacy = random.choice(fallacies)

    fallacy = st.session_state.current_fallacy

    st.markdown("#### 📝 这个论证犯了什么错误？")
    with st.container(border=True):
        st.markdown(f"**{fallacy['example']}**")

    user_answer = st.selectbox(
        "选择谬误类型",
        ["我先想想..."] + [f["name"] for f in fallacies]
    )

    if user_answer != "我先想想...":
        if user_answer == fallacy["name"]:
            st.success("✅ 正确！你看穿了这个诡辩！")
        else:
            st.error(f"❌ 不对。正确答案是：{fallacy['name']}")

        st.markdown("#### 🔍 分析")
        st.info(fallacy["analysis"])

    if st.button("🔄 下一题"):
        st.session_state.current_fallacy = random.choice(fallacies)
        st.rerun()


def render_axiomatic_thinking():
    """公理化思维培养"""

    st.info("""
    💡 **公理化思维**是人类最强大的思维工具。

    从几个不证自明的**公理**出发，
    通过严格的逻辑推理，
    推导出整个知识大厦。

    这就是数学、物理、计算机科学的思维方式。
    """)

    st.markdown("### 🏛 经典公理系统")

    systems = {
        "欧几里得几何": [
            "任意两个点可以用一条直线连接",
            "任意线段可以无限延长成一条直线",
            "给定任意线段，可以以其一个端点为圆心，该线段为半径作一个圆",
            "所有直角都相等",
            "平行公理"
        ],
        "皮亚诺算术": [
            "0 是自然数",
            "每个自然数有唯一的后继",
            "0 不是任何数的后继",
            "不同的数有不同的后继",
            "数学归纳法成立"
        ],
        "概率论": [
            "任何事件的概率在0到1之间",
            "必然事件的概率为1",
            "互斥事件的概率可以相加"
        ]
    }

    system_name = st.selectbox("选择公理系统", list(systems.keys()))

    st.markdown(f"#### {system_name}的公理")
    for i, axiom in enumerate(systems[system_name]):
        st.markdown(f"{i+1}. {axiom}")

    st.divider()

    st.markdown("### 🎯 训练：从公理到定理")

    st.markdown("""
    从皮亚诺公理出发，证明 **1 + 1 = 2**

    （这不是废话，这是数学史上最重要的证明之一）
    """)

    with st.expander("查看证明过程（震撼）"):
        st.code("""
        定义：
        1 = 0 的后继
        2 = 1 的后继
        a + 0 = a
        a + b的后继 = (a + b)的后继

        证明 1 + 1 = 2：

        1 + 1
        = 1 + (0的后继)          （根据1的定义）
        = (1 + 0)的后继          （根据加法的定义）
        = 1的后继                （因为 1 + 0 = 1）
        = 2                      （根据2的定义）

        Q.E.D. 证明完毕！

        怀特海和罗素用了362页《数学原理》
        才严格证明 1 + 1 = 2。
        这就是公理化思维的力量。
        """)

    st.success("""
    🎉 **公理化思维的本质**

    1. 把所有隐藏的假设挖出来，变成明确的公理
    2. 定义所有概念，不依赖直觉和常识
    3. 每一步推理都严格按照规则来
    4. 结论只要你接受公理，就必须接受结论

    这种思维方式，是人类所有精确知识的基础。
    """)


if __name__ == "__main__":
    pass
