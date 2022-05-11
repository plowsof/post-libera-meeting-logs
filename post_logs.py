from github import Github
import requests 
import datetime
import pprint
#https://libera.monerologs.net/monero-community/20220511/raw
#https://libera.monerologs.net/monero-research-lab/20220511
#https://libera.monerologs.net/monero-dev/20220511

git_token = "hunter2hunter2"
#git_repo =  "monero-project/meta"
issue_number = 1 
git_repo = "plowsof/multi-crypto-freelance"

moderator_name = "plowsof[m]"
room = "monero-community"

#msg_begin = "meeting start"
#msg_end = "meeting over"

msg_begin = "Shall we do one of those community meeting thingys this Sunday orr?"
msg_end = "cheekyleeks i thought i was going to get away with not moderating one if nobody said anything 😁 https://github.com/monero-project/meta/issues/704"

def post_comment(comment):
    global issue_number, git_repo, git_token
    g = Github(git_token)
    repo = g.get_repo(git_repo)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(f"Logs \n```\n{comment}\n```\nAutomated by [this](https://github.com/plowsof/post-libera-meeting-logs)")

def get_meeting_log():
    global room, moderator_name, msg_begin, msg_end
    todays_date = datetime.datetime.now().strftime("%Y%m%d")
    meeting_status = "none"
    log = ""
    r = requests.get(f"https://libera.monerologs.net/{room}/{todays_date}/raw")
    for line in r.iter_lines():
        if line: 
            line = line.decode("utf-8")
            split = line.split()
            username = split[1]
            comment = line.split(f"{split[0]} {split[1]}")[1][1:]
            if username == f"<{moderator_name}>":
                if comment == msg_begin:
                    print("begin")
                    meeting_status = "active"
                if comment == msg_end:
                    meeting_status = "ended"
            if meeting_status == "active":
                log += f"{line}\n"
            if meeting_status == "ended":
                log += f"{line}\n"
                print(log)
                post_comment(log)
                break
                

get_meeting_log()
