from github import Github
import requests 
import datetime
import pprint
import pprint
#https://libera.monerologs.net/monero-community/20220511/raw
#https://libera.monerologs.net/monero-research-lab/20220511
#https://libera.monerologs.net/monero-dev/20220511

git_token = "hunter2hunter2lol"

git_repo = "monero-project/meta"
#moderator_name = "plowsof[m]"
#moderator_name = "ErCiccione"
#room = "monero-dev"
#msg_begin = "meeting time"
#msg_end = "meeting over"
issue_number = 711
moderator_name = "UkoeHB"
room = "monero-research-lab"
msg_begin = "meeting time"
msg_end = "productive day"
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
    todays_date = datetime.datetime.now().strftime("%Y%m%d")
    meeting_status = "none"
    log = ""
    r = requests.get(f"https://libera.monerologs.net/{room}/{todays_date}/raw")
    for line in r.iter_lines():
        if line: 
            line = line.decode("utf-8")
            split = line.split(' ')[1:]
            comment = ' '.join(split)
            comment = comment.replace("<m-relay> ", "")
            split = comment.split(' ')
            username = split[0].replace("<","< ")
            username = username.replace(">"," >")
            split[0] = "> __" + username + "__"
            comment = ' '.join(split) + "     \n"
            if username == f"< {moderator_name}> ":
                if msg_begin in comment:
                    meeting_status = "active"
                if msg_end in comment:
                    meeting_status = "ended"
            if meeting_status == "active":
                log += f"{comment}\n"
            if meeting_status == "ended":
                log += f"{comment}\n"
                post_comment(log)
                break
get_meeting_log()
