# Path to oh-my-zsh installation.
# this will vary from system to system for sure
export ZSH="$HOME/.oh-my-zsh"
source $ZSH/oh-my-zsh.sh

ZSH_THEME="avit"
plugins=(git common-aliases pip)

# for wal
cat $HOME/.cache/wal/sequences

export PATH=$PATH:~/.local/bin

export EDITOR=vim
export TERM=kitty

alias vim="nvim"

HISTFILE=~/.histfile
HISTSIZE=10000
SAVEHIST=10000

setopt autocd
unsetopt beep
