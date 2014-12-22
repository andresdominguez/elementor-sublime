#!/bin/sh

rm -fr dist/
mkdir dist

zip dist/elementor.sublime-package Elementor.py *.sublime-keymap *.sublime-menu
