[[ $- != *i* ]] && return

[ -f "/usr/bin/vim" ] && export EDITOR="/usr/bin/vim"

export HISTCONTROL=ignoredups:ignorespace

export HISTFILE="${HOME}/.bash_history"
export HISTFILESIZE=200000
export HISTSIZE=100000

shopt -s histappend

[ -f ".bash_aliases" ] && source .bash_aliases 

### Terminal setup and module loading
# Neofetch
[ -f "/usr/bin/neofetch" ] && echo $- | grep -q i 2>/dev/null && /usr/bin/neofetch

# Only load liquidprompt in interactive shells, not from a script or from scp
# `liquidprompt`
[ -f "/usr/bin/liquidprompt" ] && echo $- | grep -q i 2>/dev/null && . /usr/bin/liquidprompt
# `autojump`
[ -f "/usr/bin/autojump" ] && [ -f "/usr/share/autojump/autojump.bash" ] && echo $- | grep -q i 2>/dev/null && . /usr/share/autojump/autojump.bash
