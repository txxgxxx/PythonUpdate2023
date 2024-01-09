class Player:

    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")

class Team:

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def remove_player(self, name):
        for remove_player in self.players:
            if remove_player.name == name:
                self.players.remove(remove_player)
                print(f"{name} was expelled from the team {self.team_name}")
                return
        print("Cant find player")
    
    def team_xp(self):
        team_xp = 0
        for player in self.players:
            team_xp += player.xp
            print(f"🍀 {player.name} contributes || {player.xp} || xp for {self.team_name}! \n Thank you for your dedication.")
        print(f"🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉 \n {self.team_name}'s total xp is {team_xp} \n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        
    
    def show_players(self):
        for player in self.players:
            player.introduce()

team_t1 = Team("SKT T1")

team_t1.add_player("geon")
team_t1.add_player("Faker")

team_t1.remove_player("geon")
team_t1.show_players()
team_t1.add_player("geon")
team_t1.add_player("Oner")

team_blue = Team("DRX")

team_blue.add_player("Beryl")

team_t1.team_xp()
team_blue.team_xp()