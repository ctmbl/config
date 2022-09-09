[ -f "/usr/bin/vim" ] && export EDITOR="/usr/bin/vim"

HISTCONTROL=ignoredups:ignorespace

HISTFILE=".bash_history"
HISTFILESIZE=200000
HISTSIZE=100000

shopt -s histappend

alias git-config='/usr/bin/git --git-dir=/home/ctmbl/config.git --work-tree=/home/ctmbl'
alias gconf='git-config'

# some more ls aliases
alias ll='ls -AlF'
alias l='ls -CF'

# Only load liquidprompt in interactive shells, not from a script or from scp
[ -f "/usr/share/liquidprompt/liquidprompt" ] && echo $- | grep -q i 2>/dev/null && . /usr/share/liquidprompt/liquidprompt
