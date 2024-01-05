def create_player_for_team(name, xp, team):
    return

def create_player(name, xp, team):
    return { 
        "name": name,
        "XP": xp,
        "team": team}

def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

geon = create_player("taegeon", 1500, "T1")
tae = create_player("leetae", 15000, "DRX")

teams = {
    "T1" : [geon],
    "DRX" : [tae]
}