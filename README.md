# Compiler Calculator Project

- [Compiler Calculator Project](#compiler-calculator-project)
  - [Dependencies](#dependencies)
  - [How To Run](#how-to-run)
    - [Run on Local Machine](#run-on-local-machine)
    - [Run on Docker](#run-on-docker)
  - [Grammar](#grammar)
  - [Type of Parser](#type-of-parser)
  - [Method of Translation](#method-of-translation)
  - [Code Explain](#code-explain)
    - [components/lexica.py](#componentslexicapy)
    - [components/parsers.py](#componentsparserspy)
    - [components/translator.py](#componentstranslatorpy)
    - [main.py and components/main.ui](#mainpy-and-componentsmainui)
  - [Design a GUI](#design-a-gui)


This is the Calculator Project with two operators + and * for AT70.07 course @ AIT. 

## Dependencies
- Python version 3.9.18
- `sly` as a submodule [link](https://github.com/dabeaz/sly)
- `PyQt6` for GUI development

## How To Run

### Run on Local Machine

1. Clone the project to your local machine.
2. Clone submodule with this `git submodule update --init --recursive`.
3. Set `PYTHONPATH` to include `/path/to/sly`.
4. Run `pipenv install` inside `src/`.
5. You might also need to install `PyQt6` separately.

### Run on Docker

Once you install `Docker` in your system, you can do the following.

1. Clone the project to your local machine.
2. Clone submodule with this `git submodule update --init --recursive`.
3. (Optional) Install X11Client if you want to use GUI in docker. 
   - For `Windows`: [X410](https://x410.dev) is the best but you will need to pay. 
   - For `Mac`: [XQuartz](https://www.xquartz.org) is the one I used. 
   - For `Linux`/`Ubuntu`: You can simply map `DISPLAY`. No additional app is needed.
4. Run `docker compose up -d --build` to build and run the container.
5. Use `VSCode` to dev the project remotely.


## Grammar
```txt
S -> E
E -> T * E
E -> T
T -> F + T
T -> F
F -> ( E )
F -> num
```

The + operator has higher priority than the * operator.
The numbers are integers.


## Type of Parser

SLR Parser

## Method of Translation

Prefix Notation and Postfix Notation

## Code Explain

Inside `src/` folder is all the code developed.

```txt
src/
  |- components/
      |- lexica.py
      |- main.ui
      |- parsers.py
      |- translator.py
  |- main.py
  |- Pipfile
  |- Pipfile.lock
```

### components/lexica.py

This file showcases the Lexical analyzer component. It has a `MyLexer` class that extends `sly.Lexer`.
It will translate a code/string into `token` stream/generator that feeds to a `Parser`.

### components/parsers.py

This file showcases the Lexical analyzer component. It has a `MyParser` class that extends `sly.Parser`.
It is used for immediate evaluation of each semantics.

### components/translator.py

This file includes `MyTranslator` class that translates infix expression into prefix and postfix notations.

### main.py and components/main.ui

Finally, the `main.py` is the main file to run the entire project.
It will render a GUI from `components/main.ui` that was designed from `PyQt6`.
This shows how to bind a function with a button and how to display the result back to the GUI.

## Design a GUI

We use `PyQt6` and `qt designer 6` for GUI.
You can start to learn this tool from [here](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/#:~:text=To%20load%20.,a%20fully%2Dfunctional%20PyQt6%20object).

To launch `QT designer`, use `pipenv run pyqt6-tools designer` and to open the existing UI use `pipenv run pyqt6-tools designer <path/to/file.ui>`