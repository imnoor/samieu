# samieu
Program to send voice activated commands to a specific window

## pre-requisites

install the following libraries and dependencies

1. pywinauto (For sending keys to windows)
2. pyaudio (For reading from microphone)
3. SpeechRecognition (obviously)

If there is issues with installing pyaudio
```
pip install pipwin
pipwin install pyaudio
```

## running program

navigate to samieu folder
run
```
python sameiu.py
```

## Customization
Edit the settings.txt file in data folder has all the configurations that can be customized

### settings.txt in data folder
Edit the program to run
```
"global" :{"program": "path\to\program"},
```

### Stop Key 
Edit "stop":"stop", the second stop value to youd like for example "stop" : "exit"

### lib/command.py
To cutomize the commands and the code that needs to be send to the window edit the following code
```
"commands": {"follow" : "1", "copy" : "2", "paste" :"3"},
```
each word key would correspond to the code that would be send to the program
