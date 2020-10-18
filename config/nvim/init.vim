call plug#begin()
Plug 'preservim/nerdtree'
Plug 'airblade/vim-gitgutter'
Plug 'dylanaraps/wal.vim'
Plug 'vimlab/split-term.vim'
Plug 'tpope/vim-fugitive'
call plug#end()

set encoding=UTF-8

syntax enable
syntax on

colorscheme wal

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

set incsearch
set hlsearch

set conceallevel=2

inoremap kj <Esc>

nnoremap <C-g> :NERDTreeToggle<CR>

nmap <silent> <A-Up> :wincmd k<CR>
nmap <silent> <A-Down> :wincmd j<CR>
nmap <silent> <A-Left> :wincmd h<CR>
nmap <silent> <A-Right> :wincmd l<CR>

let g:airline_theme='violet'
let g:airline_powerline_fonts=1

let g:vim_markdown_math=1

let NERDTreeShowHidden=1
