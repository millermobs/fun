"""A Dirt Road

You wake up on the ground surrounded by nothing. You are lying next to a dirt path that leads out of your view.
All around is grass and nothing else. You must chose to continue or you shall never remember why you are here and who you are.

"""

prompt = "f=forward, b=back"
forward = "install"

def parse(s):
    line = s.action_line
    if "what" in line:
        print("you heard me")
    elif "what should I do" in line:
        print("get up")
