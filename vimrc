call pathogen#infect()
set nocompatible
syntax on
filetype plugin indent on

colorscheme molokai
set background=dark
set guioptions=m

let c_no_curly_error=1

let g:CSApprox_konsole=1
let NERDTreeChDirMode=2
let NERDTreeShowBookmarks=1
"let Tlist_Show_One_File=1
"let Tlist_Use_Right_Window = 1
"let Tlist_WinWidth = 40

set relativenumber
set t_Co=256
set nowrap
set tabstop=2
set shiftwidth=2
set softtabstop=2
set backspace=start,indent,eol
set autowrite
set vb t_vb=
set expandtab
set encoding=utf-8
set wildmode=longest,list,full
set wildmenu



map <F4> :cnext<CR>
map <S-F4> :cprevious<CR>

map <F5> :make<Up><CR>

map <F6> :set wrap!<CR>
map <S-F6> :set list!<CR>

map <F7> :bnext<CR>
map <S-F7> :bprevious<CR>
imap <F7> <C-o>:bnext<CR>
imap <S-F7> <C-o>:bprevious<CR>

map <Leader>b :b#<CR>
map <Leader>a :A<CR>
map <Leader>q :NERDTreeClose<CR>
map <Leader>f :NERDTreeFind<CR>

noremap <tab> 

autocmd BufEnter /usr/include/c++/* setf cpp

