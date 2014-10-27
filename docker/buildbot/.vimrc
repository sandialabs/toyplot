:set tabstop=2
:set shiftwidth=2
:set expandtab
:set smartindent
:syntax enable

set hls

set exrc
set secure

if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal g'\"" | endif
endif

:highlight ExtraWhitespace ctermbg=red guibg=red
:match ExtraWhitespace /\s\+$/

