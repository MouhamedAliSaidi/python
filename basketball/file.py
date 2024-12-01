#1
class Player:
    def __init__(self, player_dict):
        self.name = player_dict.get("name")
        self.age = player_dict.get("age")
        self.position = player_dict.get("position")
        self.team = player_dict.get("team")


#2 

kevin = {
    "name": "Kevin Durant", 
	"age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
        }
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
        }
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
        }
player_kevin = Player(kevin) 
player_jason = Player(jason)
player_kyrie = Player(kyrie)


#3
players = [
    {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age": 32, "position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age": 33, "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age": 32, "position": "Power Forward", "team": "Philadelphia 76ers"},
    {"name": "", "age": 16, "position": "P", "team": "en"}
        ]

new_team = [Player(player) for player in players]

#test print for players in new team
for player in new_team: print(player.name)




