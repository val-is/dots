set encoding=UTF-8

syntax enable
syntax on

set tabstop=4
set shiftwidth=4
set softtabstop=4

set expandtab
set nosmartindent

set nu
set rnu
set wildmenu
set lazyredraw
set showmatch
set nofoldenable
set nowrap

set incsearch
set hlsearch

set conceallevel=2

inoremap kj <Esc>
nnoremap ow :w<CR>

nnoremap <C-g> :NERDTreeToggle<CR>

nmap <silent> <A-Up> :wincmd k<CR>
nmap <silent> <A-Down> :wincmd j<CR>
nmap <silent> <A-Left> :wincmd h<CR>
nmap <silent> <A-Right> :wincmd l<CR>
