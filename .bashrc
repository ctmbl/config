[ -f "/usr/bin/vim" ] && export EDITOR="/usr/bin/vim"

export HISTCONTROL=ignoredups:ignorespace

export HISTFILE="${HOME}/.bash_history"
export HISTFILESIZE=200000
export HISTSIZE=100000

shopt -s histappend

[ -f ".bash_aliases" ] && source .bash_aliases 
