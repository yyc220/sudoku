# sudoku！

## Version Introduction

- version1

  基本实现功能的机械风数独。

- version2

  美化了界面，但是有一些bug，比如点击“清空”的时候会留下用户填写正确的数字；有提示信息，初步判断不符合规则的数字会标红。

- version3

  解决2的bug；为了增加难度，标红功能被注释掉；增加提示信息，哪个面板还需要改正；增加草稿板便于做题。

- version4

  添加题目三宫格分界线；点击文本也可以触发按钮功能，但是“清除”没办法实现（后面发现是忘记传递参数）。

- version5

  这个是最新的版本，画面更加美观，点击”清除“可以实现九宫格的清除功能。
  
- version6

  更新版本6，使用方法：运行app.py ,点击start.html 。

## Guidance

- 下载本文件夹，点击start.html即可开始游戏。

- test.mjs对solveSudoku()函数进行测试，使用的是Mocha框架进行测试，需要导入Chai框架中的expect方法用于断言结果是否正确。在命令行中进入该代码所在的目录，并执行命令：mocha。
