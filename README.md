Termux AI Runner

Termux AI Runner is a simple command‑line tool that helps you run local AI models (like LLaMA GGUF files) directly inside Termux on Android.  

It is designed for beginners who want to experiment with AI models but find the manual setup process confusing. With this tool, you can install dependencies, download models, and run them with one command.

---

🌱 Why Do We Need This?

Running AI models in Termux is powerful but tricky for newcomers. Common beginner problems include:

- Complicated setup: Installing clang, cmake, python, and compiling llama.cpp manually.  
- Model downloads: Figuring out how to fetch GGUF files from Hugging Face.  
- Storage issues: Models are large, and beginners often don’t know how to manage them.  
- Confusing commands: Long compilation and run commands can overwhelm new users.  

Termux AI Runner solves these by:
- Automating dependency installation.  
- Providing a beginner‑friendly CLI (termux-run-model).  
- Managing models in one folder (~/termux-ai-runner/models).  
- Offering simple flags for download, run, and cleanup.  

---

📦 Installation (Step‑by‑Step for Beginners)

Open Termux and run:

`bash
git clone https://github.com/arunptrdr369-cyber/termux-ai-runner
cd termux-ai-runner
chmod +x setup.sh
./setup.sh
`

This will:
- Install required packages (Python, clang, cmake, git, wget).  
- Compile llama.cpp automatically.  
- Link the runner script as termux-run-model.  

---

📖 Step‑by‑Step Walkthrough

This section is designed for absolute beginners in Termux. Follow along carefully, and you’ll have your first AI model running in minutes.

---

1️⃣ Install Termux
- Download Termux from F‑Droid (recommended).  
- Open Termux — you’ll see a Linux terminal on your Android device.

---

2️⃣ Clone the Project
`bash
git clone https://github.com/arunptrdr369-cyber/termux-ai-runner
cd termux-ai-runner
`

---

3️⃣ Run Setup Script
`bash
chmod +x setup.sh
./setup.sh
`

This installs dependencies, compiles llama.cpp, and creates the shortcut command termux-run-model.

---

4️⃣ Download Your First Model
`bash
termux-run-model --download TinyLlama --url https://huggingface.co/.../tinyllama.gguf
`

This saves the model in:
`
~/termux-ai-runner/models/
`

---

5️⃣ Run the Model
`bash
termux-run-model --run TinyLlama
`

You’ll see the model start up and respond to your prompts.

---

6️⃣ Manage Models
- List models:
  `bash
  ls ~/termux-ai-runner/models
  `
- Delete unused models:
  `bash
  rm ~/termux-ai-runner/models/*.gguf
  `

---

🚀 Usage Examples

Download a model
`bash
termux-run-model --download TinyLlama --url https://huggingface.co/.../tinyllama.gguf
`

Run a model
`bash
termux-run-model --run TinyLlama
`

List available models
`bash
ls ~/termux-ai-runner/models
`

Clean up unused models
`bash
rm ~/termux-ai-runner/models/*.gguf
`

---

⚙️ Features
- One‑command runner — no manual compilation needed.  
- Model manager — download, list, and clean models easily.  
- Beginner‑friendly CLI — simple flags for common tasks.  
- Lightweight design — no Proot or heavy frameworks.  

---

📖 Beginner Notes

- What is Termux? → A terminal emulator for Android that lets you run Linux tools.  
- What is GGUF? → A file format for LLaMA models optimized for local execution.  
- Do I need a powerful phone? → Small models (like TinyLlama) run fine on mid‑range devices. Larger models may require more RAM and storage.  
- Where are models stored? → In ~/termux-ai-runner/models/. You can delete them anytime to free space.  

---

📝 License
Released under the MIT License — free to use, modify, and share.

---

🤝 Contributing
Pull requests are welcome! If you add new features (like ONNX support, thread control, or better cleanup), please document them in the README.

---
`

---

