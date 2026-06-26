#StarWars Project by KnoX | Good Luck <3
#Start  (

#My Color Library EasyColor (
import Easycolor as es
#My library )

#Imports (
import random
import os
import time
import json
import threading
from datetime import datetime, timedelta
#Imports )

#Variables (
Admin = False
Trooper = 0
Money = 0
Energy = 150
MaxEnergy = 150
LastDaily = ""
EnergyLevel = 1
HasSword = False
SwordDurability = 0
SwordLevel = 1
SwordMaxDurability = 10
Level = 1
XP = 0
LastCloseTime = ""
SAVE_FILE = "starwars_save.json"
#Variables )

#Welcome Message (
print(es.BRIGHT_GREEN + "+=============================+" + es.RESET)
print(es.BRIGHT_GREEN + "|     STAR WARS PROJECT ⭐    |" + es.RESET)
print(es.BRIGHT_GREEN + "|        by KnoX              |" + es.RESET)
print(es.BRIGHT_GREEN + "|     Good Luck & Have Fun    |" + es.RESET)
print(es.BRIGHT_GREEN + "+=============================+" + es.RESET)
print(es.BRIGHT_CYAN + "Type 'help' to see all commands." + es.RESET)
print(es.CYAN + "⚡ Energy auto-regenerates every 30 seconds (even when offline)." + es.RESET)
print()
#Welcome Message )

#Defines (

#Save game (
def save_game():
    data = {
        "Trooper": Trooper,
        "Money": Money,
        "Admin": Admin,
        "Energy": Energy,
        "LastDaily": LastDaily,
        "EnergyLevel": EnergyLevel,
        "HasSword": HasSword,
        "SwordDurability": SwordDurability,
        "SwordLevel": SwordLevel,
        "SwordMaxDurability": SwordMaxDurability,
        "Level": Level,
        "XP": XP,
        "LastCloseTime": LastCloseTime
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
        #Save Game )

#Load game (
def load_game():
    global Trooper, Money, Admin, Energy, LastDaily, EnergyLevel, MaxEnergy, HasSword, SwordDurability, SwordLevel, SwordMaxDurability, Level, XP, LastCloseTime
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                Trooper = data.get("Trooper", 0)
                Money = data.get("Money", 0)
                Admin = data.get("Admin", False)
                Energy = data.get("Energy", 100)
                LastDaily = data.get("LastDaily", "")
                EnergyLevel = data.get("EnergyLevel", 1)
                HasSword = data.get("HasSword", False)
                SwordDurability = data.get("SwordDurability", 0)
                SwordLevel = data.get("SwordLevel", 1)
                SwordMaxDurability = data.get("SwordMaxDurability", 10)
                Level = data.get("Level", 1)
                XP = data.get("XP", 0)
                LastCloseTime = data.get("LastCloseTime", "")
                
                MaxEnergy = 80 + (EnergyLevel * 20)
                
                if Energy > MaxEnergy:
                    Energy = MaxEnergy
                if Energy < 0:
                    Energy = 0
        except:
            pass
            #Loadgame )

#Calculate offline energy regen (
def calculate_offline_energy():
    global Energy, MaxEnergy, LastCloseTime
    if LastCloseTime != "":
        try:
            last_time = float(LastCloseTime)
            current_time = time.time()
            time_passed = current_time - last_time
            energy_gained = int(time_passed / 30)
            if energy_gained > 0:
                old_energy = Energy
                Energy = min(MaxEnergy, Energy + energy_gained)
                gained = Energy - old_energy
                if gained > 0:
                    print(es.CYAN + f"⚡ While you were away, you gained {gained} energy." + es.RESET)
                save_game()
        except:
            pass
    LastCloseTime = ""
    save_game()
    #Calculate offline energy regen ) 

#Update max energy (
def update_max_energy():
    global MaxEnergy
    MaxEnergy = 80 + (EnergyLevel * 20)
    #Update max energy )
    
#Load at start (
load_game()
update_max_energy()
calculate_offline_energy()
#Load at start )

#Energy Regen System (
def auto_regen_energy():
    global Energy, MaxEnergy
    while True:
        time.sleep(30)
        if Energy < MaxEnergy:
            Energy = min(MaxEnergy, Energy + 1)
            save_game()
            #Energy Regen System )

#Start background thread for auto energy regen (
regen_thread = threading.Thread(target=auto_regen_energy, daemon=True)
regen_thread.start()
#Start background thread for auto energy regen )

#Rank System based on Level (
def get_rank():
    if Level <= 5:
        return 'Bronze'
    elif Level <= 8:
        return 'Silver'
    elif Level <= 14:
        return 'Gold'
    elif Level <= 18:
        return 'Platinum'
    elif Level <= 22:
        return 'Epic'
    elif Level <= 25:
        return 'Legend'
    else:
        return 'God of War'
        #Rank System based on Level )

#Get XP needed for next level (
def get_xp_needed():
    if Level < 5:
        return 4 + (Level - 1) * 2
    elif Level < 8:
        return 12 + (Level - 5) * 2
    elif Level < 14:
        return 18 + (Level - 8) * 2
    elif Level < 18:
        return 30 + (Level - 14) * 2
    elif Level < 22:
        return 38 + (Level - 18) * 2
    elif Level < 25:
        return 46 + (Level - 22) * 2
    else:
        return 52 + (Level - 25) * 2
        #Get XP needed for next level )

#Chance on Attack With Rank (
def get_attack_stats():
    rank = get_rank()
    
    if rank == 'Bronze':
        return {'win': 35, 'lose': 35, 'draw': 30, 'power_bonus': 1.0, 'money_bonus': 1.0, 'energy_cost': 18}
    elif rank == 'Silver':
        return {'win': 38, 'lose': 32, 'draw': 30, 'power_bonus': 1.05, 'money_bonus': 1.05, 'energy_cost': 17}
    elif rank == 'Gold':
        return {'win': 41, 'lose': 29, 'draw': 30, 'power_bonus': 1.1, 'money_bonus': 1.1, 'energy_cost': 16}
    elif rank == 'Platinum':
        return {'win': 44, 'lose': 26, 'draw': 30, 'power_bonus': 1.15, 'money_bonus': 1.15, 'energy_cost': 15}
    elif rank == 'Epic':
        return {'win': 47, 'lose': 23, 'draw': 30, 'power_bonus': 1.2, 'money_bonus': 1.2, 'energy_cost': 14}
    elif rank == 'Legend':
        return {'win': 50, 'lose': 20, 'draw': 30, 'power_bonus': 1.25, 'money_bonus': 1.25, 'energy_cost': 13}
    else:
        return {'win': 53, 'lose': 17, 'draw': 30, 'power_bonus': 1.3, 'money_bonus': 1.3, 'energy_cost': 12}
#Chance on Attack With Rank )

#Defines )

#All Commands (
while True:
               
    #cmd Input (
    cmd = input(es.YELLOW + 'Enter command: ' + es.RESET).lower()
    #cmd input )
    
    #Admin (
    if cmd == 'imadmin':
        try:
            pas = int(input(es.BRIGHT_RED + 'Enter password: ' + es.RESET))
            if pas == 9061:
                Admin = True
                save_game()
                print(es.GREEN + 'You are now admin.' + es.RESET)
            else:
                print(es.RED + 'Error: Wrong password.' + es.RESET)
        except ValueError:
            print(es.RED + 'Error: Please enter a number.'+ es.RESET)
            #Admin )
     
    #Player Commands (
    elif cmd == 'mysword':
        if HasSword:
            print(es.CYAN + f"Sword Level {SwordLevel} - {SwordDurability}/{SwordMaxDurability} uses left." + es.RESET)
            if SwordDurability <= 3:
                print(es.YELLOW + "⚠️ Warning: Your Sword is almost broken, Use 'repairsword' to fix it." + es.RESET)
        else:
            print(es.RED + "Error: You don't have a Sword Use 'buysword' to buy one." + es.RESET)
     
    elif cmd == 'buysword':
        if HasSword:
            print(es.RED + "Error: You already have a Sword, Use 'upgradesword' to upgrade it." + es.RESET)
        elif Money >= 9:
            Money -= 9
            HasSword = True
            SwordLevel = 1
            SwordMaxDurability = 10
            SwordDurability = 10
            save_game()
            print(es.GREEN + "You bought a Level 1 Sword, It has 10 uses remaining." + es.RESET)
            print(es.CYAN + "Use 'upgradesword' to increase capacity, 'repairsword' to fix it." + es.RESET)
        else:
            print(es.RED + f"Error: Need $9 to buy a Sword, You have ${Money}." + es.RESET)
     
    elif cmd == 'repairsword':
        if not HasSword:
            print(es.RED + "Error: You don't have a Sword Use 'buysword' to buy one." + es.RESET)
        elif SwordDurability >= SwordMaxDurability:
            print(es.CYAN + f"Your Sword is already fully repaired ({SwordDurability}/{SwordMaxDurability})." + es.RESET)
        else:
            repair_cost = 5 + (SwordLevel - 1) * 3
            if Money >= repair_cost:
                Money -= repair_cost
                SwordDurability = SwordMaxDurability
                save_game()
                print(es.GREEN + f"Sword repaired, It now has {SwordMaxDurability} uses remaining (Cost: ${repair_cost})." + es.RESET)
            else:
                print(es.RED + f"Error: Need ${repair_cost} to repair, You have ${Money}." + es.RESET)
    
    elif cmd == 'upgradesword':
        if not HasSword:
            print(es.RED + "Error: You don't have a Sword, Use 'buysword' first." + es.RESET)
            continue
        
        if SwordLevel >= 5:
            print(es.RED + "Error: Your Sword is already at max level (Level 5 - 50 uses)." + es.RESET)
            continue
        
        upgrade_costs = {1: 50, 2: 100, 3: 200, 4: 400}
        next_capacity = {1: 15, 2: 20, 3: 30, 4: 50}
        
        upgrade_cost = upgrade_costs[SwordLevel]
        next_max = next_capacity[SwordLevel]
        
        print(es.CYAN + f"Current Sword Level: {SwordLevel} (Max {SwordMaxDurability} uses)." + es.RESET)
        print(es.YELLOW + f"Next Level: {SwordLevel + 1} (Max {next_max} uses)." + es.RESET)
        print(es.YELLOW + f"Upgrade Cost: ${upgrade_cost}." + es.RESET)
        
        if Money >= upgrade_cost:
            confirm = input(es.WHITE + "Upgrade your Sword? (yes/no): " + es.RESET).lower()
            if confirm == 'yes' or confirm == 'y':
                Money -= upgrade_cost
                SwordLevel += 1
                SwordMaxDurability = next_max
                SwordDurability = SwordMaxDurability
                save_game()
                print(es.GREEN + f"Sword upgraded to Level {SwordLevel}." + es.RESET)
                print(es.GREEN + f"Max durability is now {SwordMaxDurability} uses." + es.RESET)
            else:
                print(es.YELLOW + "Upgrade cancelled." + es.RESET)
        else:
            print(es.RED + f"Error: Need ${upgrade_cost} to upgrade You have ${Money}." + es.RESET)
     
    elif cmd == 'dailyreward':
        current_time = time.time()
        
        if LastDaily == "":
            LastDaily = str(current_time)
            Trooper += 30
            Money += 10
            save_game()
            print(es.CYAN + "Daily reward claimed +30 Troopers and +$10." + es.RESET)
            print(es.CYAN + "Next reward available in 24 hours." + es.RESET)
        else:
            try:
                last_time = float(LastDaily)
                time_passed = current_time - last_time
                hours_passed = time_passed / 3600
                
                if hours_passed >= 24:
                    LastDaily = str(current_time)
                    Trooper += 30
                    Money += 10
                    save_game()
                    print(es.CYAN + "Daily reward claimed +30 Troopers and +$10." + es.RESET)
                    print(es.CYAN + "Next reward available in 24 hours." + es.RESET)
                else:
                    remaining_seconds = (24 * 3600) - time_passed
                    remaining_hours = int(remaining_seconds // 3600)
                    remaining_minutes = int((remaining_seconds % 3600) // 60)
                    remaining_seconds = int(remaining_seconds % 60)
                    
                    print(es.RED + f"Error: You already claimed today's reward." + es.RESET)
                    print(es.YELLOW + f"Time remaining: {remaining_hours}h {remaining_minutes}m {remaining_seconds}s." + es.RESET)
            except ValueError:
                LastDaily = str(current_time)
                Trooper += 30
                Money += 10
                save_game()
                print(es.CYAN + "Daily reward claimed +30 Troopers and +$10." + es.RESET)
                print(es.CYAN + "Next reward available in 24 hours." + es.RESET)
                  
    elif cmd == 'stats':
        stats = get_attack_stats()
        xp_needed = get_xp_needed()
        print(es.BLUE + 'Your Money = $' + str(Money) + es.RESET)
        print(es.BLUE + 'Your Troopers = ' + str(Trooper) + es.RESET)
        if HasSword:
            print(es.BLUE + f'Your Sword = Level {SwordLevel} ({SwordDurability}/{SwordMaxDurability} uses)' + es.RESET)
        else:
            print(es.BLUE + 'Your Sword = None (use buysword)' + es.RESET)
        print(es.BLUE + f'Your Level = {Level} (XP: {XP}/{xp_needed})' + es.RESET)
        print(es.BLUE + 'Your Rank = ' + get_rank() + es.RESET)
        print(es.BLUE + 'Your Energy = ' + str(Energy) + '/' + str(MaxEnergy) + es.RESET)
        print(es.BLUE + 'Rank Bonus: +' + str(int((stats['power_bonus']-1)*100)) + '% Troopers, +' + str(int((stats['money_bonus']-1)*100)) + '% Money' + es.RESET)
        print(es.BLUE + 'Energy Cost: ' + str(stats['energy_cost']) + ' per attack' + es.RESET)

    elif cmd == 'help':
        print(es.BRIGHT_BLUE + 'Player commands:' + es.RESET)
        print(es.BRIGHT_BLUE + 'stats, dailyreward, attack,' + es.RESET)
        print(es.BRIGHT_BLUE + 'myrank, rankhelp, myenergy, upgradeenergy,' + es.RESET)
        print(es.BRIGHT_BLUE + 'shop, prices, mysword, buysword, repairsword,' + es.RESET)
        print(es.BRIGHT_BLUE + 'upgradesword, buyenergy' + es.RESET)
        if Admin == True:
            print(es.BRIGHT_GREEN + '=================' + es.RESET)
            print(es.BRIGHT_BLUE + 'Admin commands:' + es.RESET)
            print(es.BRIGHT_BLUE + 'givemoney, givetroopers,' + es.RESET)
            print(es.BRIGHT_BLUE + 'settroopers, setmoney' + es.RESET)
    
    elif cmd == 'attack': 
        if not HasSword:
            print(es.RED + "Error: You don't have a Sword, Use 'buysword' to buy one." + es.RESET)
            continue
        
        if SwordDurability <= 0:
            print(es.RED + "Error: Your Sword is broken, Use 'buysword' to buy a new one." + es.RESET)
            HasSword = False
            save_game()
            continue
        
        if SwordDurability == 1:
            print(es.YELLOW + "⚠️ WARNING: Your Sword will break after this attack." + es.RESET)
            confirm = input(es.WHITE + "Are you sure you want to attack? (yes/no): " + es.RESET).lower()
            if confirm != 'yes':
                print(es.CYAN + "Attack cancelled. Use 'repairsword' to fix it." + es.RESET)
                continue
        
        attack_stats = get_attack_stats()
        energy_cost = attack_stats['energy_cost']
        
        if Energy < energy_cost:
            print(es.RED + f'Error: Not enough energy You need {energy_cost} energy (Current: {Energy}/{MaxEnergy}).' + es.RESET)
            continue
        
        try:
            Attackers = float(input(es.WHITE + 'How many Troopers do you want to attack with: ' + es.RESET))
            if Attackers.is_integer():
                Attackers = int(Attackers)
            else:
                print(es.RED + 'Error: Please enter a whole number (integer).' + es.RESET)
                continue
        except ValueError:
            print(es.RED + 'Error: Please enter a valid number.' + es.RESET)
            continue

        if Attackers <= 0:
            print(es.RED + 'Error: You cannot attack with 0 or negative Troopers.' + es.RESET)
        elif Attackers > Trooper:
            print(es.RED + "Error: You don't have that many Troopers." + es.RESET)
        else:
            Energy -= energy_cost
            if Energy < 0:
                Energy = 0
            
            SwordDurability -= 1
            if SwordDurability <= 0:
                HasSword = False
                print(es.RED + "Your Sword broke during the attack." + es.RESET)
            
            result_num = random.randint(1, 100)
            win_chance = attack_stats['win']
            lose_chance = attack_stats['lose']
            
            if result_num <= win_chance:
                result = 'win'
            elif result_num <= win_chance + lose_chance:
                result = 'lose'
            else:
                result = 'draw'
        
            if result == 'lose':
                Trooper = max(0, Trooper - Attackers)
                print(es.RED + f'Attack failed You lost all {Attackers} Troopers Energy left: {Energy}/{MaxEnergy}.' + es.RESET)
        
            elif result == 'win':
                gain_trooper = int(Attackers * random.uniform(0.25, 0.6))
                if gain_trooper < 1:
                    gain_trooper = 1
                gain_money = int(Attackers * random.uniform(1.0, 2.0))
                if gain_money < 1:
                    gain_money = 1
                
                gain_trooper = int(gain_trooper * attack_stats['power_bonus'])
                gain_money = int(gain_money * attack_stats['money_bonus'])
                
                critical = random.randint(1, 100)
                if critical <= 15:
                    gain_trooper = int(gain_trooper * 1.5)
                    gain_money = int(gain_money * 1.5)
                    print(es.BRIGHT_YELLOW + "🔥 CRITICAL HIT +50% more! 🔥" + es.RESET)
                
                Trooper = Trooper + gain_trooper
                Money = Money + gain_money
                print(es.GREEN + f'Attack successful You gained {gain_trooper} Troopers and ${gain_money} Energy left: {Energy}/{MaxEnergy}.' + es.RESET)
                
                XP += 1
                xp_needed = get_xp_needed()
                print(es.CYAN + f"You gained 1 XP ({XP}/{xp_needed})." + es.RESET)
                
                if XP >= xp_needed:
                    XP = XP - xp_needed
                    Level += 1
                    print(es.BRIGHT_GREEN + f"🎉 LEVEL UP You are now Level {Level}! 🎉" + es.RESET)
                    print(es.GREEN + f"Your rank is now {get_rank()}." + es.RESET)
                    save_game()
        
            else:
                print(es.CYAN + f'Attack finished Your {Attackers} Troopers returned safely Energy left: {Energy}/{MaxEnergy}.' + es.RESET)
                
            save_game()
                
    elif cmd == 'shop':
                
          print(es.ORANGE + 'Use Prices to see shop prices.' + es.RESET)
          print(es.ORANGE + '1.Buy Troopers with Money.' + es.RESET)
          print(es.ORANGE + '2.Buy Money with Troopers.' + es.RESET)
          
          try:
              Choice = int(input(es.GOLD + 'Enter your choice: ' + es.RESET))
          except ValueError:
              print(es.RED + 'Error: Please enter 1 or 2.' + es.RESET)
              continue
          
          if Choice == 1:
              try:
                  Buytrooper = float(input(es.MAGENTA + 'How many Troopers do you want to buy: ' + es.RESET))
                  if Buytrooper.is_integer():
                      Buytrooper = int(Buytrooper)
                  else:
                      print(es.RED + 'Error: Please enter a whole number.' + es.RESET)
                      continue
              except ValueError:
                  print(es.RED + 'Error: Please enter a number.' + es.RESET)
                  continue
          
              price = Buytrooper * 3
          
              if Buytrooper <= 0:
                  print(es.RED + 'Error: You cannot buy 0 or negative Troopers.' + es.RESET)
              elif Money >= price:
                  Money = Money - price
                  Trooper = Trooper + Buytrooper
                  save_game()
                  print(es.CYAN + 'You bought ' + str(Buytrooper) + ' Troopers with $' + str(price) + ' Money.' + es.RESET)
              else:
                  print(es.RED + "Error: You don't have enough Money." + es.RESET)
                  
          elif Choice == 2:
              try:
                  Buymoney = float(input(es.MAGENTA + 'How much Money do you want to buy: ' + es.RESET))
                  if Buymoney.is_integer():
                      Buymoney = int(Buymoney)
                  else:
                      print(es.RED + 'Error: Please enter a whole number.' + es.RESET)
                      continue
              except ValueError:
                  print(es.RED + 'Error: Please enter a number.' + es.RESET)
                  continue
          
              price2 = Buymoney * 3
          
              if Buymoney <= 0:
                  print(es.RED + 'Error: You cannot buy 0 or negative Money.' + es.RESET)
              elif Trooper >= price2:
                  Trooper = Trooper - price2
                  Money = Money + Buymoney
                  save_game()
                  print(es.CYAN + 'You bought $' + str(Buymoney) + ' Money with ' + str(price2) + ' Troopers.' + es.RESET)
              else:
                  print(es.RED + "Error: You don't have enough Troopers." + es.RESET)
      
    elif cmd == 'prices':
        print(es.GOLD + "========= Shop Prices =========" + es.RESET)
        print(es.CYAN + "Buy Troopers: $3 Money = 1 Trooper" + es.RESET)
        print(es.CYAN + "Buy Money: 3 Troopers = $1 Money" + es.RESET)
        print(es.GOLD + "===============================" + es.RESET)
        
    elif cmd == 'myrank':
            
        print(es.GOLD + 'Your rank is: ' + get_rank() + es.RESET)
            
    elif cmd == 'rankhelp':
        print(es.BRIGHT_CYAN +
"""Level 1-5: Bronze
Level 6-8: Silver
Level 9-14: Gold
Level 15-18: Platinum
Level 19-22: Epic
Level 23-25: Legend
Level +26: God of War

XP needed for next level increases by 2 each level
Win an attack to gain 1 XP.""" + es.RESET)
    
    elif cmd == 'myenergy':
        print(es.CYAN + f'Energy: {Energy}/{MaxEnergy}' + es.RESET)
        print(es.BRIGHT_BLUE + 'Energy regenerates 1 point every 30 seconds (even offline).' + es.RESET)
        print(es.BRIGHT_BLUE + 'Each attack costs energy based on your rank.' + es.RESET)
        
    elif cmd == 'upgradeenergy':
        if EnergyLevel >= 10:
            print(es.RED + "Error: Energy already at max level (Level 10 = 280 max energy)." + es.RESET)
        else:
            upgrade_cost = EnergyLevel * 110
        
            print(es.CYAN + f"Current Energy Level: {EnergyLevel}." + es.RESET)
            print(es.CYAN + f"Current Max Energy: {MaxEnergy}." + es.RESET)
            print(es.YELLOW + f"Next Level: {EnergyLevel + 1} (+20 max energy)." + es.RESET)
            print(es.YELLOW + f"Upgrade Cost: ${upgrade_cost}." + es.RESET)
        
            if Money >= upgrade_cost:
                confirm = input(es.WHITE + "Do you want to upgrade? (yes/no): " + es.RESET).lower()
                if confirm == 'yes' or confirm == 'y':
                    Money -= upgrade_cost
                    EnergyLevel += 1
                    update_max_energy()
                                
                    Energy = MaxEnergy
                    
                    save_game()
                    
                    print(es.GREEN + f"Energy upgraded to Level {EnergyLevel}." + es.RESET)
                    print(es.GREEN + f"Max Energy is now {MaxEnergy}." + es.RESET)
                else:
                    print(es.YELLOW + "Upgrade cancelled." + es.RESET)
            else:
                print(es.RED + f"Error: You need ${upgrade_cost} to upgrade You have ${Money}." + es.RESET)
        
    elif cmd == 'buyenergy':
        print(es.GOLD + "========= Energy Elixirs =========" + es.RESET)
        print(es.CYAN + "1. Small Elixir (+25 Energy) - $95" + es.RESET)
        print(es.CYAN + "2. Medium Elixir (+60 Energy) - $225" + es.RESET)
        print(es.CYAN + "3. Large Elixir (+120 Energy) - $450" + es.RESET)
        print(es.CYAN + "4. Massive Elixir (+200 Energy) - $750" + es.RESET)
        print(es.GOLD + "==================================" + es.RESET)
    
        try:
            elixir_choice = int(input(es.WHITE + "Choose elixir (1-4): " + es.RESET))
        except ValueError:
            print(es.RED + "Error: Please enter a number." + es.RESET)
            continue
    
        if elixir_choice == 1:
            price = 95
            energy_gain = 25
            name = "Small Elixir"
        elif elixir_choice == 2:
            price = 225
            energy_gain = 60
            name = "Medium Elixir"
        elif elixir_choice == 3:
            price = 450
            energy_gain = 120
            name = "Large Elixir"
        elif elixir_choice == 4:
            price = 750
            energy_gain = 200
            name = "Massive Elixir"
        else:
            print(es.RED + "Error: Invalid choice, Please enter 1-4." + es.RESET)
            continue
    
        if Money < price:
            print(es.RED + f"Error: Need ${price} You have ${Money}." + es.RESET)
            continue
    
        if Energy >= MaxEnergy:
            print(es.RED + f"Error: Your energy is already full ({Energy}/{MaxEnergy})." + es.RESET)
            continue
        
        space_left = MaxEnergy - Energy
        if energy_gain > space_left:
            actual_gain = space_left
            print(es.YELLOW + f"Warning: You only have {space_left} energy space left." + es.RESET)
            confirm = input(es.WHITE + f"Buy {name} for ${price} to gain {actual_gain} energy? (yes/no): " + es.RESET).lower()
            if confirm != 'yes':
                print(es.CYAN + "Purchase cancelled." + es.RESET)
                continue
        else:
            actual_gain = energy_gain
            confirm = input(es.WHITE + f"Buy {name} for ${price} to gain {actual_gain} energy? (yes/no): " + es.RESET).lower()
            if confirm != 'yes':
                print(es.CYAN + "Purchase cancelled." + es.RESET)
                continue
    
        Money -= price
        Energy = min(MaxEnergy, Energy + actual_gain)
        save_game()
        print(es.GREEN + f"You bought {name} and gained {actual_gain} energy." + es.RESET)
        print(es.CYAN + f"Energy: {Energy}/{MaxEnergy}" + es.RESET) 
        #Player Commands )  
                  
    #Admin Commands  (
    elif cmd == 'givemoney':
        if Admin == True:
            try:
                Givemoney = float(input(es.BRIGHT_MAGENTA + 'How much money do you want to give: ' + es.RESET))
                if Givemoney.is_integer():
                    Givemoney = int(Givemoney)
                else:
                    print(es.RED + 'Error: Please enter a whole number.' + es.RESET)
                    continue
                if Givemoney >= 0:
                    Money += Givemoney
                    save_game()
                    print(es.CYAN + 'You successfully give ' + str(Givemoney) + ' dollars to yourself.')
                else:
                    print(es.RED + 'Error: Cannot give negative money.' + es.RESET)
            except ValueError: 
                print(es.RED + 'Error: Please enter a number.' + es.RESET)
        else:
            print(es.RED + 'Error: You are not admin!' + es.RESET)
            
    elif cmd == 'givetroopers':
        if Admin == True:
            try:
                Givetrooper = float(input(es.BRIGHT_MAGENTA + 'How many Troopers do you want to give: ' + es.RESET))
                if Givetrooper.is_integer():
                    Givetrooper = int(Givetrooper)
                else:
                    print(es.RED + 'Error: Please enter a whole number.' + es.RESET)
                    continue
                if Givetrooper >= 0:
                    Trooper += Givetrooper
                    save_game() 
                    print(es.CYAN + 'You successfully give ' + str(Givetrooper) + ' Troopers to yourself.')
                else:
                    print(es.RED + 'Error: Cannot give negative Troopers.' + es.RESET)
            except ValueError:
                print(es.RED + 'Error: Please enter a number.' + es.RESET)
        else:
            print(es.RED + 'Error: You are not admin!' + es.RESET)
           
    elif cmd == 'setmoney':
        if Admin == True:
            try:
                Setmoney = float(input(es.BRIGHT_MAGENTA + 'How much money do you want to set: ' + es.RESET))
                if Setmoney.is_integer():
                    Setmoney = int(Setmoney)
                else:
                    print(es.RED + 'Error: Please enter a whole number.' + es.RESET)
                    continue
                if Setmoney >= 0:
                    Money = Setmoney
                    save_game()
                    print(es.CYAN + 'You successfully set ' + str(Setmoney) + ' dollars to yourself.')
                else:
                    print(es.RED + 'Error: Cannot set negative money.' + es.RESET)
            except ValueError:
                print(es.RED + 'Error: Please enter a number.' + es.RESET)
        else:
            print(es.RED + 'Error: You are not admin!' + es.RESET)
            
    elif cmd == 'settroopers':
        if Admin == True:
            try:
                Settrooper = float(input(es.BRIGHT_MAGENTA + 'How many Troopers do you want to set: ' + es.RESET))
                if Settrooper.is_integer():
                    Settrooper = int(Settrooper)
                else:
                    print(es.RED + 'Error: Please enter a whole number.' + es.RESET)
                    continue
                if Settrooper >= 0:
                    Trooper = Settrooper
                    save_game()
                    print(es.CYAN + 'You successfully set ' + str(Settrooper) + ' Troopers to yourself.')
                else:
                    print(es.RED + 'Error: Cannot set negative Troopers.' + es.RESET)
            except ValueError:
                print(es.RED + 'Error: Please enter a number.' + es.RESET)
        else:
            print(es.RED + 'Error: You are not admin!' + es.RESET)
            #Admin Commands )
            
            #All Commands )
     
     #Exit (
    elif cmd == 'exit' or cmd == 'quit':
        LastCloseTime = str(time.time())
        save_game()
        print(es.MAGENTA + "Goodbye." + es.RESET)
        break
        #Exit )
       
     #Wrong Command (
    else:
        print(es.RED + "Error: Unknown command." + es.RESET)
        #Wrong Command )
       
       #EnD )
