# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

stats = {}

def player(prev_play, opponent_history=[]):
  global stats

  n = 5

  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  if len(opponent_history)<=n:
    return "R"
    
  last = "".join(opponent_history[-n:])

  if "".join(opponent_history[-(n+1):]) in stats.keys():
    stats["".join(opponent_history[-(n+1):])]+=1
    
  else:
    stats["".join(opponent_history[-(n+1):])]=1

  possible = [last + "R", last + "P", last + "S"]

  for pair in possible:
    if not pair in stats.keys():
      stats[pair] = 0

  prediction = max(possible, key=lambda key: stats[key])

  if prediction[-1] == "P":
    return "S"
  if prediction[-1] == "R":
    return "P"
  if prediction[-1] == "S":
    return "R"
