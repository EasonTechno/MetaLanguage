# 🧠 MetaLang

[![GitHub Stars](https://img.shields.io/github/stars/EasonTechno/MetaLang?style=social)](https://github.com/EasonTechno/MetaLang/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/EasonTechno/MetaLang)](https://github.com/EasonTechno/MetaLang/issues)
[![License](https://img.shields.io/github/license/EasonTechno/MetaLang)](LICENSE)

> **Language shapes thought, cognition changes lives.**

---

## 🌍 [中文版 README](README.zh-CN.md)

---

## 🎯 Project Philosophy

This is not an ordinary project. This is an **exploration of the nature of human cognition**.

Based on the **Sapir-Whorf Hypothesis (Linguistic Relativity)**, we propose a radical hypothesis:

> **The language you think in determines how intelligent you are.**

- Doing math in Chinese? Too slow. The brain needs to translate formal logic into everyday language first, losing 30% computational power in the process.
- Learning English with grammar-translation? You'll never master it. You're not thinking in English; you're doing mental gymnastics of Chinese-English translation.
- Can't grasp recursion and dynamic programming? It's not you—it's your native language that's not good at expressing state transitions.

### 🔬 Experimental Validation

We use **neural networks to replicate the human language learning process**:
1. Implant a "native language" into the model (fixed, unchangeable)
2. Train the model to learn second, third languages
3. Observe if the model can **completely bypass the native language and think directly in the foreign language**
4. Verify thinking efficiency differences across languages for specific problems

The core thinking simulation engine has been spun off as the **SynapGraph** library, available for standalone installation.

### 🚀 Human Applications

We turn AI experiment conclusions into training tools for humans:

| Training Module | Core Idea | Real Effect |
|----------------|-----------|-------------|
| 📚 **Direct Foreign Language Thinking** | Skip native language translation, build concepts directly in foreign language | 20-30% score improvement in English exams |
| 🔄 **Recursive Thinking Language** | No subject-predicate-object, describe problems using "state-transition" | Dramatic improvement in OI/ACM algorithm abilities |
| 🧮 **Mathematical Language Reasoning** | Abandon natural language for pure formal logic derivation | No more headaches with advanced math/physics problems |
| 🎯 **Artificial Language Design** | Design optimal languages for specific cognitive tasks | Unlock entirely new dimensions of thinking |

---

## ✨ Features

### 🤖 SynapGraph Thinking Simulator (Standalone Library)
- Strictly controlled variables for quantifiable validation of linguistic relativity
- Controlled experiments with same model architecture but different "native language" initializations
- Quantifiable thinking style difference metrics
- **Independent Open Source Project**: [EasonTechno/SynapGraph](https://github.com/EasonTechno/SynapGraph)

### 🛠️ Human Training Tools
- No AI background required, accessible to everyone
- Every thinking style is a "language" that can be learned
- Learn "recursion language" and "math language" like learning a second foreign language

### 📋 Thinking Flow Questionnaire Generator
This is not an ordinary problem-solving tool—**we study HOW you think, not what the answer is**.

- **Pure blank recording**: No leading questions, no interference with your native thinking flow
- **Deep single-problem focus**: One problem at a time, quality over quantity
- **Real Codeforces problem bank**: Live random sampling of 800-1300 difficulty math problems from Codeforces API
- **Dual format output**: Eye-friendly PNG + printable PDF, works on phones and computers
- **Scheduled generation**: Auto-push every Monday, Wednesday, Friday at 9 AM

---

## 🚀 Quick Start

### Requirements
- Python 3.9+
- Streamlit
- Pillow
- **SynapGraph** (core thinking simulator library)

### Launch Project

```bash
git clone https://github.com/EasonTechno/MetaLang.git
cd MetaLang
pip install -r requirements.txt
./start.sh
# Or run directly
streamlit run app.py
```

### Using Thinking Simulator Standalone

SynapGraph is available as an installable Python library:

```bash
pip install synapgraph
```

```python
from synapgraph import SynapGraphulator

# Initialize simulator with native language
sim = SynapGraphulator(native_language="Chinese")

# Anchor the native language network
sim.anchor_native_network()

# Train an independent English subnetwork
result = sim.train_subnetwork(
    language="English",
    orthogonality_target=0.7,
    epochs=100
)

print(f"Subnetwork independence: {result['final_independence']:.1%}")
```

---

## 📁 Project Structure

```
MetaLang/
├── 📄 app.py                          # Streamlit main program
├── 📄 README.md                       # English documentation (this file)
├── 📄 README.zh-CN.md                 # Chinese documentation
├── 📄 requirements.txt                # Dependencies (includes synapgraph)
├── 📄 start.sh                        # One-click startup script
├── 📂 .github/
│   └── 📂 workflows/
│       └── 📄 thinking_flow.yml       # Questionnaire generator Action
├── 📂 core_modules/                   # Core algorithm modules
├── 📂 research_framework/             # Research methodology
├── 📂 training_tools/                 # Human training tools
├── 📂 artificial_language/            # Artificial language design research
├── 📂 practice_tools/                 # Practice application tools
├── 📂 data/                           # Training datasets
└── 📂 docs/                           # Research documentation
```

---

## 🤝 Contributing

Everyone is welcome to join this crazy project!

We currently need:
1. 🧪 Design and validation of more "thinking languages"
2. 📊 Design of quantitative metrics for training effectiveness
3. 🤖 Expansion of neural network controlled experiments (submit to SynapGraph repo)
4. 📝 More types of thinking flow questionnaires
5. 🌍 Multi-language translation support (French, Japanese, etc.)

Feel free to open Issues or submit PRs!

---

## ✨ Contributors

Thanks to everyone who made MetaLang possible:

<!-- ALL-CONTRIBUTORS-LIST:START -->

### 🏆 Core Contributors

<div align="center">

| | | |
|:---:|:---:|:---:|
| <img src="https://avatars.githubusercontent.com/EasonTechno?v=4&s=100" width="80"><br>**EasonTechno**<br>📆PM 🤖Creator | <img src="https://avatars.githubusercontent.com/siimonQWER?v=4&s=100" width="80"><br>**siimonQWER**<br>⚠️Testing 💬Feedback | <img src="https://avatars.githubusercontent.com/Claude?v=4&s=100" width="80"><br>**Claude**<br>💻Code 🤖AI Research |

</div>

### 🙏 Special Thanks

<div align="center">

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**注意力惊人** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**parity-police** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**何嘉豪** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**杀死那个贝尔曼...** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**今天晚上吃点啥** |
| <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**数学数学我们喜欢你** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**道爷我成了** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**噬菌体侵染降噪耳机** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**KeYanZhao** | <img src="https://avatars.githubusercontent.com/u/0?v=4&s=60" width="50"><br>**IAKIOI** |

</div>

### 🎯 Other Testers

<div align="center">

lmy · 钥匙 · KingFrank · 可以随便取名吗 · NPC · zhr的桌子～ · Siimon哥我男神😘 · zyc的零食呢 · 王昊宇 · 双叉犀金蛋 · 66789 · 麦斯欧德 · hz258258 · Masud

**26 Contributors** 🌟

</div>
<!-- ALL-CONTRIBUTORS-LIST:END -->

---

## 😂 Best Responses

Funny answers collected from the questionnaire:

> **Anonymous**: 额这是啥啊我不是在玩手机吗

> **杀死那个贝尔曼代数线形几何微分几何啊啊啊**: a,b,c 是整数，我能不能构造一个以它们为根的多项式...别给我推数学了好吗我还要堵桥呢

> **Anonymous**: 谁把这玩意塞到我抖音里了😅

> **道爷我成了**: a = [-B ± √(B²-4AC)]/2A...你为什么要这么对我，我的数学又挂科了，我的心真的好痛啊啊啊啊啊啊！苍羌蹬阶！！！

> **Anonymous**: 出卷人是gay

> **lmy**: 不是这不是数论题么，我都退竞了你还不放过我！！

> **IAKIOI**: 肯定有啊，2024这么大没有我吃点东西!

> **何嘉豪**: 知乎体回答，"谢邀但是这破题不是高中的么，上大学了还在追我"

---

## 🏆 Special Thanks

High-quality questionnaire responses (sorted by length):

| Nickname | Words | Highlight |
|----------|-------|-----------|
| **噬菌体侵染降噪耳机** | 108 | Parametric method |
| **数学数学我们喜欢你** | 114 | c=0 enumeration |
| **道爷我成了** | 202 | Quadratic equation |
| **注意力惊人** | 185 | Factor pairs |
| **parity-police** | 182 | Mod 2 analysis |
| **杀死那个贝尔曼代数线形几何微分几何啊啊啊** | 170 | Polynomial construction |
| **何嘉豪** | 172 | Cubic equation |
| **今天晚上吃点啥** | 168 | Cubic structure |
| **KeYanZhao** | 87 | Symmetry |
| **IAKIOI** | 20 | Naive intuition |

---

## 📬 Contact

- **GitHub (Main Project)**: [EasonTechno/MetaLang](https://github.com/EasonTechno/MetaLang)
- **GitHub (Thinking Simulator)**: [EasonTechno/SynapGraph](https://github.com/EasonTechno/SynapGraph)
- **Email**: uu13652153631@qq.com
- **Maintainer**: [@EasonTechno](https://github.com/EasonTechno)

---

## 📜 License

MIT License - See [LICENSE](LICENSE) file for details

---

<div align="center">
    <strong>🌟 If this project blew your mind, give it a Star so more people can see it! 🌟</strong>
    <br>
    <sub>Language shapes thought · Cognition changes lives</sub>
</div>
