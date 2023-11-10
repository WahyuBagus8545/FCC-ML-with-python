# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


def player(prev_play, opponent_history=[], play_order={}):
  opponent_history.append(prev_play)

  if len(opponent_history) > 4:
    last_five = "".join(opponent_history[-5:])
    play_order[last_five] = play_order.get(last_five, 0) + 1

    potential_plays = ["".join([*opponent_history[-4:], v]) for v in 'RPS']
    sub_order = {k: play_order[k] for k in potential_plays if k in play_order}

    if sub_order:
      max_pattern = max(sub_order, key=sub_order.get)
      predicted_opponent_play = max_pattern[-1]

      # Counter the predicted play
      return {'P': 'S', 'R': 'P', 'S': 'R'}.get(predicted_opponent_play, 'P')

  # Introduce randomness to increase adaptability
  return random.choice(['R', 'P', 'S'])
