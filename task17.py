'''17. Session class
Task: Session classini yozing.

login(username) metodida foydalanuvchi tizimga kiradi
logout() metodida tizimdan chiqadi
'''

class Session:
    def __init__(self):
        self.user = None   

    def login(self, username):
        if self.user is None:
            self.user = username
            print(f"{username} logged in")
        

    def logout(self):
        if self.user is not None:
            print(f"{self.user} logged out")
            self.user = None
        
            

s = Session()
s.login("Ali")
s.login("Vali")
s.logout()
s.logout()
