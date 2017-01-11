#!/bin/bash

cd $HOME
rm -rf .vim .vimrc devenv
git clone --recursive https://github.com/deft-code/devenv.git devenv
ln -s devenv/vim .vim
ln -s devenv/vimrc .vimrc
