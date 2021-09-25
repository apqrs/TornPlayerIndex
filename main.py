import requests
import time
from alive import keep_alive
import json
from random import choice


ranks = {'Absolute beginner': 0, 'Beginner': 1, 'Inexperienced': 2, 'Rookie': 3, 'Novice': 4, 'Below average': 5, 'Average': 6, 'Reasonable': 7, 'Above average': 8, 'Competent': 9, 'Highly competent': 10, 'Veteran': 11, 'Distinguished': 12, 'Highly distinguished': 13, 'Professional': 14, 'Star': 15, 'Master': 16, 'Outstanding': 17, 'Celebrity': 18, 'Supreme': 19, 'Idolized': 20, 'Champion': 21, 'Heroic': 22, 'Legendary': 23, 'Elite': 24, 'Invincible': 25}

battle_est = {0:'< 2k',1: '2k - 25k',2:'20k - 250k',3:'200k - 2.5m',4:'2m - 35m',5:'20m - 250m',6:'> 250m'}



api_key = 'NDErpdX4WW1qWLrg'

#5m	50m	500m	5b	50b  networth triggers
#100	5,000	10,000	20,000	30,000	50,000 crime triggers
def netScore(networth):
  if networth >= 50000000000:
    return 5
  if networth >= 5000000000:
    return 4
  if networth >= 500000000:
    return 3
  if networth >= 50000000:
    return 2
  if networth >= 5000000:
    return 1
  return 0

def crimeScore(crimes):
  crimeTriggers = [0,100,5000,10000,20000,30000,50000]

  for z in crimeTriggers[::-1]:
    if crimes >= z:
      return crimeTriggers.index(z)

def lvlScore(lvl):
  lvlTrigger = [0,2, 6, 11, 26, 31, 50, 71, 100]

  for t in lvlTrigger[::-1]:
    if lvl >= t:
      return lvlTrigger.index(t)



def stats_estimate(key):
  response = requests.get(f'https://api.torn.com/user/{key}?selections=profile,crimes,personalstats&key={api_key}').json()

  v=response["rank"]
  rank_ = ""
  for rank in ranks:
    if rank in v:
      rank_ = rank

    
  # v = " ".join(response["rank"].split()[:-1])
  # v = v.strip()
  totalScore = ranks[rank_]

  crimes = response["criminalrecord"]["total"]
  networth = response["personalstats"]["networth"]
  lvl = response["level"]

  #age calculation
  # age = response["age"]
  last_action = response["last_action"]["relative"]
  last_action = last_action.split()
  if last_action[0] == 'No':
    return -1, -1, -1, -1
  last_action = int(last_action[0])
  # dif = abs(age - last_action)
  score = crimeScore(crimes) + lvlScore(lvl) + netScore(networth)

  val = totalScore - score

  data = {
        "name": response["name"], 
        "life_current": response["life"]["current"], 
        "life_maximum":response["life"]["maximum"], 
        "status_description": response["status"]["description"],
        "status_color": response["status"]["color"],
        "status_state": response["status"]["state"],
        "status_until": response["status"]["until"],
        "level": response["level"],
        "last_action_relative": response["last_action"]["relative"],
        "last_action_timestamp": response["last_action"]["timestamp"],
        "last_action_status": response["last_action"]["status"],
        "update_timestamp":1632197311,
        "last_attack_attacker": True,
        "last_attack_timestamp":0,
        "note":"",
        "color":0,
        "result":"",
        "fair_fight":1.0,
        "flat_respect":0.0,
        "base_respect":0.0,
        "win":1
        }

  # print(data)

  if val > 6:val = 6

  return battle_est[val], val, last_action, data

keep_alive()
def main():
  print('Program started.')
  # no_of_players = 0
  start = 1805000
  desired = 2
  # lvD = 30
  desired_diff = 600

  for j in range(1000000):
    time.sleep(10)
    
    
    start += choice([1,2,3])
    # print(j, start)
    # if no_of_players > 5000:
    #   exit()
    try:
      stats, i, d, dat = stats_estimate(start)

      if stats == -1:
        continue

      print(f'Running analysis at {start} Stats:{stats}', end= '\r')
      # print(dat["status_description"])
      if d >= desired_diff and dat["status_description"]!="In federal jail permanently":

        if i == desired:
          # no_of_players += 1
          # print('Nayy')
          with open("list.json") as file:
            json_data = json.load(file)
          
          json_data[str(start)] = dat
          # print('Here')
          with open("list.json", 'w') as file:
            json.dump(json_data, file, indent=2)


          

        if i == 0:
          # no_of_players += 1
          with open("under2k.json") as file:
            json_data = json.load(file)
          
          json_data[str(start)] = dat

          with open("under2k.json", 'w') as file:
            json.dump(json_data, file, indent=2)

          

          

        if i == 1:
          # no_of_players += 1
          with open("under25k.json") as file:
            json_data = json.load(file)
          
          json_data[str(start)] = dat
          with open("under25k.json", 'w') as file:
            json.dump(json_data, file, indent=2)

        if i == 5:
          # no_of_players += 1
          with open("under200m.json") as file:
            json_data = json.load(file)
          
          json_data[str(start)] = dat

          with open("under200m.json", 'w') as file:
            json.dump(json_data, file, indent=2)

        if i == 3:
          # no_of_players += 1
          with open("under2m.json") as file:
            json_data = json.load(file)
          
          json_data[str(start)] = dat

          with open("under2m.json", 'w') as file:
            json.dump(json_data, file, indent=2)

        if i == 4:
          # no_of_players += 1
          with open("under20m.json") as file:
            json_data = json.load(file)
          
          json_data[str(start)] = dat

          with open("under20m.json", 'w') as file:
            json.dump(json_data, file, indent=2)

        if i == 6:
          # no_of_players += 1
          with open("over200m.json") as file:
            json_data = json.load(file)
          
          json_data[str(start)] = dat

          with open("over200m.json", 'w') as file:
            json.dump(json_data, file, indent=2)
      

    except Exception as e:
      print(f'Running analysis at {start} FAiled', end= '\r')
      with open("log.txt",'a') as file:
        file.write(str(e))
        file.write('\n')
        continue
      
    

      
    

if __name__ == "__main__":
  main()
  # print(stats_estimate(2669775))
