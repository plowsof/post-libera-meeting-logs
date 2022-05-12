# post-libera-meeting-logs
Auto post the logs to the correct monero meeting issue + close it too

The git token can be obtained here https://github.com/settings/tokens

The token only needs 1 permission ' public_repo '     
![token permission](https://raw.githubusercontent.com/plowsof/post-libera-meeting-logs/main/gitkey.png)    
modify the variables accordingly 
```
msg_begin = "Meeting begin"
msg_end = "Meeting over"
moderator_name = "plowsof[m]" #exactly how it appears on libera logs
issue_number = 1 
```
run the script at the end of the meeting, making sure that you have typed the ```msg_end``` string
