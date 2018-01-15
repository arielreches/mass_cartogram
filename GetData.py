import pandas as pd
import numpy as np
import json

def fix_town(ss):
    for s in ss:
        try:
            s = s.upper()
            splitted = s.split()

            first = splitted[0]
            second = splitted[1]

            if(first == "NORTH" or first == "SOUTH" or first == "EAST" or first == "WEST" or first== "NEW" or first == "FALL" or first == "GREAT"):

                return (first + " " +second)
            else:
                return first
        except:
            return "N?A"


def age():

    my_data = pd.read_csv('age/age.csv', delimiter=',', header=0)[[2, 3,9,15]]

    my_data['GEO.display-label'] = pd.Series(((my_data[[0]].apply(fix_town, 1))))
    my_data.columns = ['town', 'child', 'old', 'age']
    print(my_data)
    return my_data

def income():

    my_data = pd.read_csv('income/income.csv', delimiter=',', header=0)[[2, 3]]

    my_data['GEO.display-label'] = pd.Series(((my_data[[0]].apply(fix_town, 1))))
    my_data.columns = ['town', 'income']

    return my_data
    # print (townss)

def education():
    my_data = pd.read_csv('education/education.csv', delimiter=',', header=0)[[2, 5]]

    my_data['GEO.display-label'] = pd.Series(((my_data[[0]].apply(fix_town, 1))))
    my_data.columns = ['town', 'education']
    print(my_data)

    return my_data
    # print (townss)



def towns():
    json_data = open("MASS.JSON").read()
    towns = []
    data = json.loads(json_data)
    for town in data['features']:
        towns.append((town['properties']['TOWN']))

    return towns

def election2016():

    def removeComma(s):
        return s.replace(',', '')

    def upper(s):
        return s.upper()

    my_data = pd.read_csv('election2016.csv', delimiter=',')[['City/Town','Clinton/ Kaine', 'Trump/ Pence', 'Total Votes Cast']]
    my_data['City/Town'] = my_data['City/Town'].apply(upper)
    my_data['Clinton%'] = my_data['Clinton/ Kaine'].apply(removeComma).apply(int) / my_data['Total Votes Cast'].apply(removeComma).apply(int) * 100
    my_data['Trump%'] = my_data['Trump/ Pence'].apply(removeComma).apply(int) / my_data['Total Votes Cast'].apply(removeComma).apply(int) * 100
    return (my_data[['City/Town','Clinton%','Trump%']])



def starbucks():
    my_data = pd.read_csv('Starbucks.csv', delimiter=',')[['City','Country Subdivision', 'Country']]
    my_data = my_data[my_data['Country'].str.contains("US")]
    my_data = my_data[my_data['Country Subdivision'].str.contains("MA")]['City']
    z = (my_data.value_counts().index)
    starbucks_towns =  (map(lambda x: x.upper(), z))
    shared_towns = list((set(towns()) & set(starbucks_towns)))
    counts = my_data.value_counts()
    counts.index = (map(lambda x: x.upper(), z))
    return (counts[shared_towns])


def dunks():
    my_data = pd.read_csv('DunkinDonuts.csv', delimiter=',')[['Name']]
    my_data = my_data[my_data['Name'].str.contains("MA")]


    def toRegularName(ugly_city):
        if "MA" in ugly_city:
            return (ugly_city[3:][-4::-1][::-1])


        # for i, x in enumerate(clistx):
        #     if x in filter(str.isalnum, ugly_city.lower()).strip():
        #         return city_list[i]

    my_data['Name'] = my_data['Name'].apply(toRegularName)
    my_data = my_data[my_data.columns[0]]
    # print(my_data[my_data.columns[0]])
    # print(towns())
    z = (my_data.value_counts().index)
    dunks_towns =  (map(lambda x: x.upper(), z))
    # print(dunks_towns)
    # print(set(dunks_towns) - set(towns()))
    shared_towns = list((set(towns()) & set(dunks_towns)))
    counts = my_data.value_counts()
    counts.index =  (map(lambda x: x.upper(), z))
    return (counts[shared_towns])



def gen_data_json():



 # #income
 #
 #    json_data = open("masscart/data/demo2.json").read()
 #    data = json.loads(json_data)
 #    inc = income()
 #    for town in data :
 #        # print(town)
 #        if town:
 #            town['name'] = town['name'].upper()
 #            try:
 #              x = inc.loc[inc['town'] == town['name']]
 #              town['inc'] = int((x['income']))
 #              # print ("not fucked", town['inc'])
 #            except:
 #                # print ("DICKED", town['name'])
 #                town['inc'] = 40000

    # education

    # json_data = open("masscart/data/demo2.json").read()
    # data = json.loads(json_data)
    # edu = education()
    # for town in data:
    #     # print(town)
    #     if town:
    #         try:
    #             x = edu.loc[edu['town'] == town['name']]
    #             town['edu'] = float((x['education']))
    #             # print ("not fucked", town['inc'])
    #         except:
    #             # print ("DICKED", town['name'])
    #             town['edu'] = .25


    #age
    # json_data = open("masscart/data/demo2.json").read()
    # data = json.loads(json_data)
    # ag = age()
    # for town in data:
    #     # print(town)
    #     if town:
    #         try:
    #             x = ag.loc[ag['town'] == town['name']]
    #             town['child'] = float((x['child']))
    #             town['old'] = float((x['old']))
    #             town['age'] = float((x['age']))
    #
    #             # print ("not fucked", town['inc'])
    #         except:
    #             # print ("DICKED", town['name'])
    #             town['child'] = .1
    #             town['old'] = .1
    #             town['age'] = 40




        # Starbucks
    # json_data = open("demo2.json").read()
    # data = json.loads(json_data)
    # bucks = starbucks()
    # for town in data :
    #     # print(town)
    #     if town:
    #         town['name'] = town['name'].upper()
    #         try:
    #             town['starbucks'] = int(bucks[town['name']])
    #             print(town['starbucks'])
    #         except:
    #             town['starbucks'] = 0
    #             print(town['starbucks'])


    # ELection
    # json_data = open("demo2.json").read()
    # data = json.loads(json_data)
    # election = election2016()
    # electionTrump = election['Trump%']
    # electionClinton = election['Clinton%']
    # electiontowns = election['City/Town']
    #
    # for town in data :
    #     # print(town)
    #     if town:
    #         try:
    #
    #             x = election.loc[election['City/Town'] == town['name']]
    #             print float((x['Clinton%']))
    #             town['clinton'] = round(float((x['Clinton%'])), 2 )
    #             town['trump'] = round(float((x['Trump%'])), 2 )
    #
    #         except:
    #             print('problem')
    #             town['clinton'] = 65
    #             town['trump'] = 35






        #Add dunkins data
    # json_data = open("demo.JSON").read()
    # data = json.loads(json_data)
    # dunk = dunks()
    # print(type(data))
    # for town in data :
    #     if town:
    #         town['name'] = town['name'].upper()
    #         try:
    #             town['dunks'] = int(dunk[town['name']])
    #         except:
    #             town['dunks'] = 0
            # print[town['name']], town['dunks']

  # Add area
  json_data = open("masscart/data/demo2.json").read()
  data = json.loads(json_data)
  area_data = open('MASStop.json').read()
  a_data = json.loads(area_data)
  for a_town in a_data['objects']['MASS']['geomefries']:
      for town in data:
          if town:
            if town['name'] == a_town['properties']['TOWN']:
                town['area'] = int((a_town['properties']['SHAPE_AREA']/1000))

  # with open('demo2.json', 'w') as outfile:
  #   json.dump(data, outfile)
  with open('masscart/data/demo2.json', 'w') as outfile:
        json.dump(data, outfile)


  # json_data = open("demo2.json").read()
  # data = json.loads(json_data)
  # # area_data = open('MASStop.json').read()
  # for town in data:
  #     if town:
  #       town['p0p'] = town['pop']['2010']




            # print data[0]

gen_data_json()
# age()
# election2016()
#
#











