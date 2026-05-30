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
<table>
  <tr>
    <td align="center"><a href="https://github.com/EasonTechno"><img src="https://avatars.githubusercontent.com/EasonTechno?v=4&s=120" width="100px;" alt="EasonTechno"/><br /><sub><b>EasonTechno</b></sub></a><br /><a href="#projectManagement-EasonTechno" title="Project Management">📆</a> <a href="#ideas-EasonTechno" title="Ideas & Planning">🤔</a></td>
    <td align="center"><a href="https://github.com/siimonQWER"><img src="https://avatars.githubusercontent.com/siimonQWER?v=4&s=120" width="100px;" alt="siimonQWER"/><br /><sub><b>siimonQWER</b></sub></a><br /><a href="#test-siimonQWER" title="Testing">⚠️</a> <a href="#feedback-siimonQWER" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/Claude"><img src="https://avatars.githubusercontent.com/Claude?v=4&s=120" width="100px;" alt="Claude"/><br /><sub><b>Claude</b></sub></a><br /><a href="#code-Claude" title="Code">💻</a> <a href="#ai-anthropics" title="AI Research">🤖</a></td>
    
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/道爷我成了"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="道爷我成了"/><br /><sub><b>道爷我成了</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/噬菌体侵染降噪耳机"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="噬菌体侵染降噪耳机"/><br /><sub><b>噬菌体侵染降噪耳机</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/parity-police"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="parity-police"/><br /><sub><b>parity-police</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/lmy"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="lmy"/><br /><sub><b>lmy</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/何嘉豪"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="何嘉豪"/><br /><sub><b>何嘉豪</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/今天晚上吃点啥"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="今天晚上吃点啥"/><br /><sub><b>今天晚上吃点啥</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/注意力惊人"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="注意力惊人"/><br /><sub><b>注意力惊人</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/数学数学我们喜欢你"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="数学数学我们喜欢你"/><br /><sub><b>数学数学我们喜欢你</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/IAKIOI"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="IAKIOI"/><br /><sub><b>IAKIOI</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/钥匙"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="钥匙"/><br /><sub><b>钥匙</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/KingFrank"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="KingFrank"/><br /><sub><b>KingFrank</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/可以随便取名吗"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="可以随便取名吗"/><br /><sub><b>可以随便取名吗</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/NPC"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="NPC"/><br /><sub><b>NPC</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/zhr的桌子～"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="zhr的桌子～"/><br /><sub><b>zhr的桌子～</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/Siimon哥我男神😘"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="Siimon哥我男神😘"/><br /><sub><b>Siimon哥我男神😘</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/zyc的零食呢"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="zyc的零食呢"/><br /><sub><b>zyc的零食呢</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/王昊宇"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="王昊宇"/><br /><sub><b>王昊宇</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/KeYanZhao"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="KeYanZhao"/><br /><sub><b>KeYanZhao</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/双叉犀金蛋"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="双叉犀金蛋"/><br /><sub><b>双叉犀金蛋</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/66789"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="66789"/><br /><sub><b>66789</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/麦斯欧德"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="麦斯欧德"/><br /><sub><b>麦斯欧德</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/hz258258"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="hz258258"/><br /><sub><b>hz258258</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
    <td align="center"><a href="https://github.com/Masud"><img src="https://avatars.githubusercontent.com/u/0?v=4&s=120" width="100px;" alt="Masud"/><br /><sub><b>Masud</b></sub></a><br /><a href="#test" title="Testing">⚠️</a> <a href="#feedback" title="Feedback">💬</a></td>
  </tr>
</table>
<!-- ALL-CONTRIBUTORS-LIST:END -->

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
