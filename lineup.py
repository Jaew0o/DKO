import webbrowser
import csv
import random
import time

teams = int(input('How many teams to search for? > '))
minScore = int(input('What in the point floor? > '))

webbrowser.open('https://www.draftkings.com/lineup/getavailableplayerscsv?contestTypeId=21&draftGroupId=89525')
time.sleep(10)
filename = r'C:\Users\woodj\Desktop\DKSalaries.csv'

#https://www.rotowire.com/football/injury-report.php
filename1 = r'C:\Users\woodj\Desktop\nfl-injury-report.csv'

iPlayer = []

with open(filename1) as injury_report:
    readerIR = csv.reader(injury_report)
    headerIR = next(readerIR)

    for i in readerIR:
        iPlayer.append(i[0])

with open(filename) as salary:
    reader = csv.reader(salary)
    header_row = next(reader)

    position = ['qb','rb','wr','te','dst']

    position_list = {place: [] for place in position}
    
    for row in reader:
        
        for place in position:
            
            if row[0].lower() == place and float(row[8]) > 4:
                position_list[place].append(row)

    position_list['flex'] = position_list['rb'] + position_list['wr']
                
line_count = 0 
draft = []
    
while line_count < teams:
        
    pick_order = ['qb','rb','rb','wr','wr','wr','te','flex','dst']
    team = []
    budget = 0
    points = 0

    for pick in pick_order:
        condition_met = False
    
        while not condition_met:
            player = random.choice(position_list[pick])
        
            if player[2] not in iPlayer and player[2] not in team:
                team.append(player[2])
                budget += int(player[5])
                points += float(player[8])               
                condition_met = True  

    if points >= minScore and budget <= 50000:
        team.append(budget)
        team.append(points)
        draft.append(team.copy())
        line_count += 1
        print(f'{line_count} team(s) selected')
        team.clear()

with open(r'C:\Users\woodj\Desktop\Python\Python310\python_work\Projects\DKO\dk_nfl.csv', 'w', newline='') as dk:
    writer = csv.writer(dk)
    writer.writerows(draft)
                






