[ -f "/usr/bin/vim" ] && export EDITOR="/usr/bin/vim"

alias git-config='/usr/bin/git --git-dir=/home/ctmbl/config.git --work-tree=/home/ctmbl'
alias gconf='git-config'

# some more ls aliases
alias ll='ls -AlF'
alias l='ls -CF'

# Only load liquidprompt in interactive shells, not from a script or from scp
echo $- | grep -q i 2>/dev/null && . /usr/share/liquidprompt/liquidprompt