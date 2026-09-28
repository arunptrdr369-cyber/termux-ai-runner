#!/usr/bin/env python3
import argparse, os, subprocess

MODELS_DIR = os.path.expanduser("~/termux-ai-runner/models")

def download_model(name, url):
    os.makedirs(MODELS_DIR, exist_ok=True)
    path = os.path.join(MODELS_DIR, f"{name}.gguf")
    print(f"[*] Downloading {name}...")
    subprocess.run(["wget", "-O", path, url])

def run_model(name):
    path = os.path.join(MODELS_DIR, f"{name}.gguf")
    if not os.path.exists(path):
        print(f"[!] Model {name} not found. Use --download first.")
        return
    print(f"[*] Running {name}...")
    subprocess.run(["./llama.cpp/main", "-m", path, "-p", "Hello Arun!"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Termux AI Runner")
    parser.add_argument("--download", help="Download model by name")
    parser.add_argument("--url", help="Model URL (required with --download)")
    parser.add_argument("--run", help="Run model by name")
    args = parser.parse_args()

    if args.download and args.url:
        download_model(args.download, args.url)
    elif args.run:
        run_model(args.run)
    else:
        parser.print_help()
