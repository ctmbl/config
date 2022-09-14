[ -f "/usr/bin/vim" ] && export EDITOR="/usr/bin/vim"

HISTCONTROL=ignoredups:ignorespace

HISTFILE="${HOME}/.bash_history"
HISTFILESIZE=200000
HISTSIZE=100000

shopt -s histappend

alias git-config='/usr/bin/git --git-dir=/home/ctmbl/config.git --work-tree=/home/ctmbl'
alias gconf='git-config'

# Non-secure aliases to add color
alias ls='ls --color=auto'
alias grep='grep --color=auto'

# some more ls aliases
alias ll='ls -AlFh'
alias l='ls -1F'

# Only load liquidprompt in interactive shells, not from a script or from scp
# `liquidprompt`
[ -f "/usr/bin/liquidprompt" ] && echo $- | grep -q i 2>/dev/null && . /usr/bin/liquidprompt
# `autojump`
[ -f "/usr/bin/autojump" ] && [ -f "/usr/share/autojump/autojump.bash" ] && echo $- | grep -q i 2>/dev/null && . /usr/share/autojump/autojump.bash
