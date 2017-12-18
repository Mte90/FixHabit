# Fix your bad habits

The idea behind this tool is improve my personal habits.  
In the past I developed to improve myself different scripts like [SyntaxAlert](https://github.com/Mte90/SyntaxAlert) or [Bash Remainder](https://github.com/Mte90/My-Scripts/blob/master/misc/bashremainder.sh) ([QAsana](https://github.com/Mte90/Qasana) was the first tentative).  
In few words to let you understand, seems that get alerts on my workstation is a good way to improve myself from knowledge or things to do.  
So one of the first rule of productivity is doing the most important things as firsts and this script help on that.

![screenshot_20171219_002152](https://user-images.githubusercontent.com/403283/34132971-b0da5f86-e452-11e7-9aaa-f5e12ad15891.png)

# How Works

# Settings

On the `config-example.json` (to rename as config.json) there is an example of tasks with the various settings of this scripts.

## Behaviour

### Hide and Show
If you execute again the script (launched the first time with `--hide` parameter) will happen that the window is hidden and will show only again if you execute again the script. Also the window will shown after 15 minutes if you press the button (default 900 seconds).  

### Alert
Many study say that to get an habit there are required 21 days so you can configure the date you want and the time to alert you (that as default is 21).  

### Checkboxes 
The rest of the tiny window is a tiny checkbox list to use as you prefer.  

### Run scripts
A task can have a script to launch that is executed atutomatically with the script.