#!/bin/bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

TARGET=~/.bashrc

printf '\n# pyenv configuration begins here\n' >>$TARGET
echo 'export PYENV_ROOT=~/.pyenv' >>$TARGET
echo 'export PATH=$PYENV_ROOT/bin:$PATH' >>$TARGET

printf 'if command -v pyenv 1>/dev/null 2>&1; then
	eval "$(pyenv init --path)"
fi' >>$TARGET

printf '\n# pyenv configuration ends here\n' >>$TARGET

echo 'Please close the terminal or restart the shell'
