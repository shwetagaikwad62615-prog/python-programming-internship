msg="This is a Global Scope Variable"

def show_msg():
    local_msg="This is a Local Scope Variable."
    print(msg)
    print(local_msg)
show_msg()