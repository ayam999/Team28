#exit
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want exit ?', icon="warning")
    if result == 'yes':
       app.destroy()
       exit()
#Exit()
