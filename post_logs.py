from github import Github
import requests 
import datetime
import pprint
#https://libera.monerologs.net/monero-community/20220511/raw
#https://libera.monerologs.net/monero-research-lab/20220511
#https://libera.monerologs.net/monero-dev/20220511

git_token = "hunter2hunter2"
issue_number = 703
git_repo = "monero-project/meta"
#moderator_name = "plowsof[m]"
moderator_name = "ErCiccione"
#room = "monero-community"
room = "monero-dev"
#msg_begin = "meeting start"
#msg_end = "meeting over"
msg_begin = "Hey folks"
msg_end = "the meeting is over, but obviously feel free to continue the conversations above 🙂"
def post_comment(comment):
    global issue_number, git_repo, git_token
    g = Github(git_token)
    repo = g.get_repo(git_repo)
    issue = repo.get_issue(number=issue_number)
    print(issue.state) 
    pprint.pprint(comment)
    issue.create_comment(f"Logs \n```\n{comment}\n```\nAutomated by [this](https://github.com/plowsof/post-libera-meeting-logs)")
    issue.edit(state="closed")

def get_meeting_log():
    global room, moderator_name, msg_begin, msg_end
    todays_date = datetime.datetime.now().strftime("%Y%m14")
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
                if msg_begin in comment:
                    print("begin")
                    meeting_status = "active"
                if msg_end in comment:
                    meeting_status = "ended"
            if meeting_status == "active":
                log += f"{line}\n"
            if meeting_status == "ended":
                log += f"{line}\n"
                print(log)
                post_comment(log)
                break
                
get_meeting_log()



