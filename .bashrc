[[ $- != *i* ]] && return

[ -f "/usr/bin/vim" ] && export EDITOR="/usr/bin/vim"

export HISTCONTROL=ignoredups:ignorespace;

export HISTFILE="${HOME}/.bash_history"
export HISTFILESIZE=200000
export HISTSIZE=100000

shopt -s histappend;

# git aliases
alias git-config='/usr/bin/git --git-dir=/home/ctmbl/config.git --work-tree=/home/ctmbl'
alias gconf='git-config'
# Correct typos
alias gcnof='git-config'
alias gocnf='git-config'

# Non-secure aliases to add color
alias ls='ls --color=auto'
alias grep='grep --color=auto'

# some more ls aliases
alias ll='ls -AlFh'
alias l='ls -1F'

# useful aliases
alias dua='du -h --summarize * | sort --human-numeric-sort' # TO UPDATE to add slash after directories' name

# ex = EXtractor for all kinds of archives (from ArcoLinux default .bashrc)
# usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   tar xf $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# Start the ssh-agent used to store unlocked ssh key, useful when pushing regularly with git
eval "$(ssh-agent -s)"

### Terminal setup and module loading
# Neofetch
[ -f "/usr/bin/neofetch" ] && [ -z "$NONEOFETCH" ] && echo $- | grep -q i 2>/dev/null && /usr/bin/neofetch;

# Only load liquidprompt in interactive shells, not from a script or from scp
# `liquidprompt`
[ -f "/usr/bin/liquidprompt" ] && echo $- | grep -q i 2>/dev/null && . /usr/bin/liquidprompt;
# `autojump`
[ -f "/usr/bin/autojump" ] && [ -f "/usr/share/autojump/autojump.bash" ] && echo $- | grep -q i 2>/dev/null && . /usr/share/autojump/autojump.bash;
