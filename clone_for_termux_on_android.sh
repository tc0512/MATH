#!/bin/bash
echo -e "\033[32mVerifying environment...\033[0m"
if command -v pkg >/dev/null 2>&1; then
    echo "✓ Detected: Termux on Android"
else
    echo "::error::This script is not support this platform"
fi
echo -e "\033[32m[1/3] Install packages in isolated environment\033[0m"
if command -v python >/dev/null 2>&1; then
    echo "Python is already installed"
else
    echo "Python is not installed,so install it"
    pkg update -y &>/dev/null
    pkg install -y python 2>/dev/null 1>/dev/null
fi
if command -v git >/dev/null 2>&1; then
    echo "git is already installed"
else
    echo "git is not installed,so install it"
    pkg update -y &>/dev/null
    pkg install -y git 2>/dev/null 1>/dev/null
fi
echo -e "\033[32m[2/3] Install runtime dependencies\033[0m"
pkg update -y
pkg install -y matplotlib
if pip show sympy &>/dev/null; then
    echo "sympy is already installed"
else
    echo "sympy is not installed,so install it"
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ sympy
fi
echo -e "\033[32m[3/3] Clone repository\033[0m"
rm -rf MATH
git clone https://github.com/tc0512/MATH
