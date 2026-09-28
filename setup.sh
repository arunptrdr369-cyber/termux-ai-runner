#!/data/data/com.termux/files/usr/bin/bash
# setup.sh - Installer for Termux AI Runner

echo "[*] Installing dependencies..."
pkg update -y
pkg install -y git wget python clang cmake

echo "[*] Setting up llama.cpp..."
if [ ! -d "llama.cpp" ]; then
  git clone https://github.com/ggerganov/llama.cpp
  cd llama.cpp && make && cd ..
fi

echo "[*] Linking runner..."
chmod +x runner.py
ln -sf $(pwd)/runner.py $PREFIX/bin/termux-run-model

echo "[*] Installation complete!"
