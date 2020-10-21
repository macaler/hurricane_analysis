# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages_list):
  for i in range(len(damages_list)):
    damage = damages_list[i]
    if damage == 'Damages not recorded':
      damages_list[i] = damage
    elif 'B' in damage:
      damage = damage.strip('B')
      damage = float(damage)
      damages_list[i] = damage*1000000000
    elif 'M' in damage:
      damage = damage.strip('M')
      damage = float(damage)
      damages_list[i] = damage*1000000
  return damages_list

updated_damages = update_damages(damages)
#print('List of updated hurricane damages:")
#print(updated_damages)


# write your construct hurricane dictionary function here:
def make_hurricane_dictionary(name_list, month_list, year_list, max_sustained_winds_list, areas_affected_list, damage_list, death_list):
  hurricane_dictionary = {}
  for i in range(len(name_list)):
    hurricane_dictionary[name_list[i]] = {"Name": name_list[i], "Month": month_list[i],\
                                                                 "Year": year_list[i], \
                                                                 "Max Sustained Wind": max_sustained_winds_list[i], \
                                                                 "Areas Affected": areas_affected_list[i], \
                                                                 "Damage": damage_list[i], "Deaths": death_list[i]}
  return hurricane_dictionary

master_hurricane_dictionary = make_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print("Here is the master hurricanes dictionary:")
#print(master_hurricane_dictionary)


# write your construct hurricane by year dictionary function here:
# Not gonna lie, I peeked at the Codecademy hint to help me with this one:

def make_hurricane_dictionary_by_year(hurricanes_dictionary):
  new_hurricanes_dictionary = {}
  for hurricane in hurricanes_dictionary.keys():
    thisherehurricane = hurricanes_dictionary[hurricane]
    thishereyear = thisherehurricane["Year"]
    inalready = new_hurricanes_dictionary.get(thishereyear, "Nope")
    if inalready == "Nope":
      new_hurricanes_dictionary[thishereyear] = [thisherehurricane]
    else:
      new_hurricanes_dictionary[thishereyear] = new_hurricanes_dictionary[thishereyear] + [thisherehurricane]
  return new_hurricanes_dictionary

hurricane_dictionary_by_year = make_hurricane_dictionary_by_year(master_hurricane_dictionary)
#print("Here is the dictionary of hurricane dictionaries grouped by year:")
#print(hurricane_dictionary_by_year)


# write your count affected areas function here:

def count_affected_areas(hurricanes_dictionary):
  affected_areas_dictionary = {}
  for hurricane in hurricanes_dictionary.keys():
    thisherehurricane = hurricanes_dictionary[hurricane]
    theseareas = thisherehurricane["Areas Affected"]
    for area in theseareas:
        inalready = affected_areas_dictionary.get(area, "Nope")
        if inalready == "Nope":
            affected_areas_dictionary[area] = 1
        else:
            affected_areas_dictionary[area] = affected_areas_dictionary[area] + 1
  return affected_areas_dictionary

dictionary_of_areas_affected = count_affected_areas(master_hurricane_dictionary)
#print("Here is a dictionary of areas affected by Carribean Sea hurricanes, and how often those areas were affected:")
#print(dictionary_of_areas_affected)


# write your find most affected area function here:

def get_most_affected_area(affected_areas_dictionary):
    affectedcount = 0
    for area in affected_areas_dictionary.keys():
        if affected_areas_dictionary[area] > affectedcount:
            affectedcount = affected_areas_dictionary[area]
    for area, affected in affected_areas_dictionary.items():
        if affectedcount == affected:
            affectedarea = area
    return affectedarea, affectedcount

most_impacted_area, impact = get_most_affected_area(dictionary_of_areas_affected)
print("The most impaced area was " + most_impacted_area + "; it was impaced " + str(impact) + " times.")


# write your greatest number of deaths function here:

def greatest_death_toll(hurricanes_dictionary):
    death_toll = 0
    deadliest_hurricane = ''
    for hurricane in hurricanes_dictionary.keys():
        thisherehurricane = hurricanes_dictionary[hurricane]
        if thisherehurricane["Deaths"] > death_toll:
            death_toll = thisherehurricane["Deaths"]
            deadliest_hurricane = thisherehurricane["Name"]
    return deadliest_hurricane, death_toll
    
deadliest_hurricane, death_toll = greatest_death_toll(master_hurricane_dictionary)
print("The deadliest hurricane was " + deadliest_hurricane + ", which had a death toll of " + str(death_toll) + ".")


# write your catgeorize by mortality function here:

def mortality_rating(hurricanes_dictionary):
    mortality_rating_dictionary = {"0":[], "1":[], "2":[], "3":[], "4":[], "5":[]}
    for hurricane in hurricanes_dictionary.keys():
        thisherehurricane = hurricanes_dictionary[hurricane]
        thisheredeathtoll = thisherehurricane["Deaths"]
        if thisheredeathtoll > 10000:
            mortality_rating_dictionary["5"].append(thisherehurricane)
        elif thisheredeathtoll <= 10000 and thisheredeathtoll > 1000:
            mortality_rating_dictionary["4"].append(thisherehurricane)
        elif thisheredeathtoll <= 1000 and thisheredeathtoll > 500:
            mortality_rating_dictionary["3"].append(thisherehurricane)
        elif thisheredeathtoll >= 500 and thisheredeathtoll < 100:
            mortality_rating_dictionary["2"].append(thisherehurricane)
        elif thisheredeathtoll <= 100 and thisheredeathtoll > 0:
            mortality_rating_dictionary["1"].append(thisherehurricane)
        else:
            mortality_rating_dictionary["0"].append(thisherehurricane)
    return mortality_rating_dictionary

hurricanes_by_mortality_scale = mortality_rating(master_hurricane_dictionary)
#print("Here is a dictionary of hurricane dictionaries grouped by mortality rating:")
#print(hurricanes_by_mortality_scale)


# write your greatest damage function here:

def costliest_hurricane(hurricanes_dictionary):
    highest_cost = 0
    highest_cost_hurricane = ''
    for hurricane in hurricanes_dictionary.keys():
        thisherehurricane = hurricanes_dictionary[hurricane]
        if thisherehurricane["Damage"] == 'Damages not recorded':
            continue
        elif thisherehurricane["Damage"] > highest_cost:
            highest_cost = thisherehurricane["Damage"]
            highest_cost_hurricane = thisherehurricane["Name"]
    return highest_cost_hurricane, highest_cost
    
highest_cost_hurricane, itscost = costliest_hurricane(master_hurricane_dictionary)
print("The hurricane which caused the most damage was " + highest_cost_hurricane + ", which caused " + str(itscost) + " U.S. dollars in damage.")
    

# write your catgeorize by damage function here:

def damage_rating(hurricanes_dictionary):
    damage_rating_dictionary = {'Damages not recorded': [], "0": [], "1": [], "2": [], "3": [], "4":[], "5":[]}
    for hurricane in hurricanes_dictionary.keys():
        thisherehurricane = hurricanes_dictionary[hurricane]
        thisherecost = thisherehurricane["Damage"]
        if thisherecost == 'Damages not recorded':
            damage_rating_dictionary['Damages not recorded'].append(thisherehurricane)
        elif thisherecost > 50000000000:
            damage_rating_dictionary["5"].append(thisherehurricane)
        elif thisherecost <= 50000000000 and thisherecost > 10000000000:
            damage_rating_dictionary["4"].append(thisherehurricane)
        elif thisherecost <= 10000000000 and thisherecost > 1000000000:
            damage_rating_dictionary["3"].append(thisherehurricane)
        elif thisherecost >= 1000000000 and thisherecost < 100000000:
            damage_rating_dictionary["2"].append(thisherehurricane)
        elif thisherecost <= 100000000 and thisherecost > 0:
            damage_rating_dictionary["1"].append(thisherehurricane)
        else:
            damage_rating_dictionary["0"].append(thisherehurricane)
    return damage_rating_dictionary

hurricanes_by_damage_scale = damage_rating(master_hurricane_dictionary)
#print("Here is a dictionary of hurricane dictionaries grouped by damage cost rating:")
#print(hurricanes_by_damage_scale)
