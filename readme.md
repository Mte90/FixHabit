# Fix your bad habits

The idea behind this tool is improve my personal habits.  
In the past I developed to improve myself different scripts like [SyntaxAlert](https://github.com/Mte90/SyntaxAlert) or [Bash Remainder](https://github.com/Mte90/My-Scripts/blob/master/misc/bashremainder.sh) ([QAsana](https://github.com/Mte90/Qasana) was the first tentative).  
In few words to let you understand, seems that get alerts on my workstation is a good way to improve myself from knowledge or things to do.  
So one of the first rule of productivity is doing the most important things as firsts and this script help on that.

# How Works

Show a window that support the hide and show. What mean? if you execute again the script and you launch with `--hide` parameter will happen that the window is hidden and will show only if you execute again. Also the window will shown after 15 minutes if you press the button (default 900 seconds).  
Another feature based on the `config-example.json` (to rename as config.json) is to alert after the date you configured. What mean? many study say that to get an habit there are required 21 days so you can configure the date you want and the time to alert you (that as default is 21).  
The rest of the tiny window is a tiny checkbox list to use as you prefer.  
Another feature is that a task can have a script to launch that is executed atuomatically with the script.