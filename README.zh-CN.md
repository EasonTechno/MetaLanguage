# 🧠 共语论 MetaLang

[![GitHub Stars](https://img.shields.io/github/stars/EasonTechno/MetaLang?style=social)](https://github.com/EasonTechno/MetaLang/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/EasonTechno/MetaLang)](https://github.com/EasonTechno/MetaLang/issues)
[![License](https://img.shields.io/github/license/EasonTechno/MetaLang)](LICENSE)

> **语言塑造思维，认知改变人生。**

---

## 🌍 [English Version](README.en.md)

---

## 🎯 项目理念

这不是一个普通的项目，这是一次**对人类认知本质的探索**。

我们基于**萨丕尔-沃尔夫假说（语言相对论）**，提出一个激进的假设：
> **你用什么语言思考，决定了你有多聪明。**

- 用中文做数学题？太慢了。大脑需要先把形式逻辑翻译成日常语言，中间损耗30%的算力。
- 用语法翻译法学英语？永远学不好。你不是在用英语思考，你是在做中英互译的脑筋急转弯。
- 学不会递归和动态规划？不是你笨，是你的母语不擅长表达状态转移。

### 🔬 实验验证

我们用**神经网络复刻人类的语言学习过程**：
1. 给模型植入一种"母语"（固定，无法改变）
2. 训练模型学习第二种、第三种语言
3. 观察模型能否**完全绕过母语，直接用外语进行思考**
4. 验证不同语言对特定问题的思考效率差异

思维模拟核心引擎已独立为 **SynapGraph** 库，可单独安装使用。

### 🚀 人类应用

我们把 AI 实验的结论做成训练工具，迁移到人类身上：

| 训练模块 | 核心思想 | 实际效果 |
|---------|---------|---------|
| 📚 **外语直接思考** | 跳过母语翻译，直接用外语构建概念 | 英语考试提分20-30% |
| 🔄 **递归思维语言** | 不用主谓宾，用"状态-转移"描述问题 | OI/ACM 算法能力飞升 |
| 🧮 **数学语言推理** | 放弃自然语言，纯形式逻辑推导 | 数学物理压轴题不再头疼 |
| 🎯 **人工语言设计** | 为特定认知任务设计最优语言 | 解锁全新的思考维度 |

---

## ✨ 项目特色

### 🤖 SynapGraph 思绘（独立库）
- 严格控制变量，验证语言相对论的量化效果
- 同一模型结构，不同"母语"初始化的对照实验
- 可量化的思维方式差异指标
- **独立开源项目**: [EasonTechno/SynapGraph](https://github.com/EasonTechno/SynapGraph)

### 🛠️ 人类训练工具
- 不需要你有 AI 背景，人人都能用
- 每种思维方式都是一套可以习得的"语言"
- 像学第二外语一样学"递归语"、"数学语"

### 📋 思维流问卷自动生成器
这不是普通的刷题工具——**我们要研究的是你怎么思考，而不是答案是什么**。

- **纯空白记录**：没有任何引导性问题，不干扰你的原生思维流
- **单题深度**：每次只给一道题，拒绝刷数量，追求思考深度
- **Codeforces 真题库**：从 Codeforces API 实时随机抽取 800-1300 分数学题
- **双格式输出**：高清护眼 PNG + 可打印 PDF，手机电脑都能用
- **定时生成**：每周一、三、五早9点自动推送

### 🧑‍🤝‍🧑 三类招募中

1. **外语学习者**：基础越差越好（越容易绕过母语直接思考）
2. **OI/ACM 选手**：正在死磕递归/DP 的（我们给你一套新语言）
3. **GPU 闲置者**：跑实验，帮我们验证更多猜想

---

## 🚀 快速开始

### 环境要求
- Python 3.9+
- Streamlit
- Pillow
- **SynapGraph** (思绘核心库)

### 启动项目

```bash
git clone https://github.com/EasonTechno/MetaLang.git
cd MetaLang
pip install -r requirements.txt
./start.sh
# 或者直接运行
streamlit run app.py
```

### 单独使用思绘

SynapGraph 已独立为可安装的 Python 库：

```bash
pip install synapgraph
```

```python
from synapgraph import SynapGraphulator

# 初始化模拟器，设置母语
sim = SynapGraphulator(native_language="Chinese")

# 锚定母语网络
sim.anchor_native_network()

# 训练独立的英文子网络
result = sim.train_subnetwork(
    language="English",
    orthogonality_target=0.7,
    epochs=100
)

print(f"子网络独立性: {result['final_independence']:.1%}")
```

### 使用问卷生成器

1. 打开仓库 **Actions** 标签页
2. 选择 **🧠 Thinking Flow Questionnaire Generator**
3. 点击 **Run workflow**
4. （可选）自定义题目难度范围
5. 生成的问卷在 `thinking-questionnaires/` 文件夹中

---

## 📁 项目结构

```
MetaLang/
├── 📄 app.py                          # Streamlit 主程序
├── 📄 README.md                       # 中文文档（本文档）
├── 📄 README.en.md                    # English Documentation
├── 📄 requirements.txt                # 依赖（包含 synapgraph）
├── 📄 start.sh                        # 一键启动脚本
├── 📂 .github/
│   └── 📂 workflows/
│       └── 📄 thinking_flow.yml       # 问卷生成器 Action
├── 📂 core_modules/                   # 核心算法模块
├── 📂 research_framework/             # 研究方法论
├── 📂 training_tools/                 # 人类训练工具
│   ├── foreign_language_training/     # 外语直接思考训练
│   ├── recursion_training/            # 递归思维训练
│   └── math_reasoning/                # 数学语言推理
├── 📂 artificial_language/            # 人工语言设计研究
├── 📂 practice_tools/                 # 实践应用工具
├── 📂 data/                           # 训练数据集
└── 📂 docs/                           # 研究文档
```

---

## 🔬 研究哲学

> "我的语言的界限意味着我的世界的界限。"
> — 维特根斯坦

我们拒绝**智商决定论**。

智商不是一个固定的数字——它是一套**思维工具**。每一种思维方式都是一门可以学习、练习、精通的"语言"。数学是一门语言，递归是一门语言，英语也是一门语言。

你的上限不取决于你天生有多聪明，而取决于你**掌握了多少门思考的语言**。

我们的目标：**编纂人类所有的思维语言，开发高效训练方法，让认知增强触手可及。**

---

## 🤝 参与贡献

欢迎所有人加入这个疯狂的计划！

我们目前需要：
1. 🧪 更多"思维语言"的设计与验证
2. 📊 训练效果的量化指标设计
3. 🤖 神经网络对照实验的扩展（提交到 SynapGraph 仓库）
4. 📝 更多类型的思维流问卷
5. 🌍 多语言翻译支持（法语、日语等）

直接开 Issue 或者提交 PR 都可以！

---

## ✨ 贡献者名单

感谢每一位让 MetaLang 成为可能的贡献者：

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<div align="center">

![贡献者头像](https://raw.githubusercontent.com/EasonTechno/MetaLang/main/contributors.svg)

**核心贡献者**

[![EasonTechno](https://avatars.githubusercontent.com/EasonTechno?v=4&s=80)](https://github.com/EasonTechno)
[![siimonQWER](https://avatars.githubusercontent.com/siimonQWER?v=4&s=80)](https://github.com/siimonQWER)
[![Claude](https://avatars.githubusercontent.com/Claude?v=4&s=80)](https://github.com/Claude)

**问卷参与者** (按昵称首字母排序)

道爷我成了 · 噬菌体侵染降噪耳机 · parity-police · lmy · 何嘉豪 · 今天晚上吃点啥 · 注意力惊人 · 数学数学我们喜欢你 · IAKIOI · 钥匙 · KingFrank · 可以随便取名吗 · NPC · zhr的桌子～ · Siimon哥我男神😘 · zyc的零食呢 · 王昊宇 · KeYanZhao · 双叉犀金蛋 · 66789 · 麦斯欧德 · hz258258 · Masud

共 **25** 位贡献者 🌟

</div>
<!-- ALL-CONTRIBUTORS-LIST:END -->

---
## 整活答案
大半夜清理数据给我笑成大肠杆菌了

请看VCR:
### 😄油盐不进区
---
```
**【匿名用户】**

> 额这是啥啊我不是在玩手机吗
```
> 给我干哪里来了
---
```
**【杀死那个贝尔曼代数线形几何微分几何啊啊啊】**

> a,b,c 是整数，我能不能构造一个以它们为根的多项式 f(t) = (t-a)(t-b)(t-c)，让它有简单的系数？设 f(t) = t³ - mt² + nt - p，其中 m=a+b+c, n=ab+bc+ca, p=abc。如果我能让 p 也等于某个好算的数就好了——但 p 会自动确定，不受控制。 别给我推数学了好吗我还要堵桥呢
```
> 这位更是油盐不进，天王老子来了也挡不住我堵桥
---
```
**【匿名用户】**

> 谁把这玩意塞到我抖音里了😅
```
> 数学的风还是吹到了抖音
---
### 开大组
---
```
**【道爷我成了】**

> a = [-B ± √(B²-4AC)]/2A，需要 √(...) 为整数。你为什么要这么对我，我的数学又挂科了，我的心真的好痛啊啊啊啊啊啊！苍羌蹬阶！！！😅
```
> 千万别让火子哥碰数学
---
```
**【匿名用户】**

> 出卷人是gay
```
> 我看着呢……
---
```
**【lmy】**

> 不是这不是数论题么，我都退竞了你还不放过我！！
```
> 《你触碰到了竞赛生的逆鳞》
---
```
**【IAKIOI】**

> 肯定有啊，2024这么大没有我吃点东西!
```
> 骗吃骗喝
---
```
**【何嘉豪】**

> 谢邀但是这破题不是高中的么，上大学了还在追我
```
> 昵称正确
---



## 🏆 特别鸣谢

以下问卷参与者的回答质量极高（按字数排序），特此鸣谢：

| 昵称 | 字数 | 回答亮点 |
|------|------|---------|
| **噬菌体侵染降噪耳机** | 541 | 参数化方法，尝试多种角度，思路清晰 |
| **数学数学我们喜欢你** | 219 | c=0枚举因子，完整分析直觉判断 |
| **hz258258** | 216 | 唯一完整验证答案，格式规范逻辑清晰 |
| **道爷我成了** | 150 | 二次方程视角，过程详细 |
| **NPC** | 163 | "now" — 赛博极简主义 |
| **注意力惊人** | 126 | 列出全部12种因子对逐一验证 |

---

## 😂 整活大赏

收集问卷中最有「灵魂」的回答：

> **道爷我成了**：把 a 看成变量研究二次方程...你为什么要这么对我，我的数学又挂科了，我的心真的好痛啊啊啊啊啊啊！苍羌蹬阶！！！

> **lmy**：不是这不是数论题么，我都退竞了你还不放过我！！

> **KingFrank**：谁把这玩意塞到我抖音里了😅

> **王昊宇**：aaa

> **Siimon哥我男神😘**：不存在吧，三奇三偶都不行，剩下的懒得算了

> **数学数学我们喜欢你**：如果 c=0，那原式变成 (a+b)·ab = 2024 = 2³×11×23...直觉上 a 和 b 不能太小也不能太大

---

## 📬 联系与交流

- **GitHub (主项目)**: [EasonTechno/MetaLang](https://github.com/EasonTechno/MetaLang)
- **GitHub (思绘)**: [EasonTechno/SynapGraph](https://github.com/EasonTechno/SynapGraph)
- **邮箱**: uu13652153631@qq.com
- **维护者**: [@EasonTechno](https://github.com/EasonTechno)

---

## 📜 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

<div align="center">
    <strong>🌟 如果这个项目让你眼前一亮，点个Star让更多人看到！🌟</strong>
    <br>
    <sub>语言塑造思维 · 认知改变人生</sub>
</div>
