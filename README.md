# Termux AI Runner

**Termux AI Runner** is a beginner‑friendly command‑line tool that makes it easy to run local AI models (like LLaMA GGUF files) directly inside [Termux](https://termux.dev/).  

Instead of manually compiling libraries, setting up Proot environments, or juggling dependencies, this tool gives you **one simple command** to download and run models on your Android device.

---

## ✨ Why This Tool?

Running AI models in Termux is powerful but confusing for beginners. Common problems include:
- Installing the right dependencies (clang, cmake, Python, etc.)
- Compiling `llama.cpp` or KoboldCPP manually
- Downloading large GGUF models from Hugging Face
- Managing storage space and cleaning up unused models

**Termux AI Runner** solves these by:
- Automating dependency installation
- Providing a simple CLI (`termux-run-model`)
- Managing models in one folder (`~/termux-ai-runner/models`)
- Offering easy commands for download, run, and cleanup

---

## 📦 Installation

Open Termux and run:

```bash
git clone https://github.com/yourname/termux-ai-runner
cd termux-ai-runner
chmod +x setup.sh
./setup.sh
