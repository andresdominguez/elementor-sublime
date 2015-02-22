elementor-sublime
=================

A Sublime 3 plugin to test your protractor locators with
[elementor](https://github.com/andresdominguez/elementor).

Here is the [Sublime 2 plugin version](https://github.com/andresdominguez/elementor-sublime/tree/master)

## How to install it

Clone this repo

```shell
$ git clone https://github.com/andresdominguez/elementor-sublime.git
```

Create a directory called *Elementor* under Sublime's Packages directory and
copy the cloned directory

```shell
$ mkdir ~/Library/Application Support/Sublime Text 3/Packages/Elementor
$ cp elementor-sublime/* ~/Library/Application Support/Sublime Text 3/Packages/Elementor
```

## How to use it

Start [elementor](https://github.com/andresdominguez/elementor).

Go to a protractor test file, select the text you want to run on elementor,
right-click, and Choose "Run selection in elementor".

![elementor screenshot](screenshot.png)

See the results in the status bar.

## Shortcuts

|Platform  | Shortcut        |
|----------|-----------------|
| Mac      | control Shift E |
| Windows  | Alt Shift P     |
| Linux    | Alt Shift P     |
