def main(inputFile,idlist,radius):
  # fix the input file name expension and read the data
  try:
    file=open(inputFile,'r')
    if file==None:
      print("Error: file not found")
      # terminate the program
      return None,None,None,None
  except:
    print("File not found")
    # terminate the program
    return None,None,None,None
  # read the data
  with open(inputFile,'r') as f:
    data=[]
    # read header of the file
    line = f.readline()
    # read the rest of the file
    line = line.strip()
    data.append(line.split(','))
    # invalidate the header of the file
    try:
      if data[0] != ['LocId','Latitude','Longitude','Category','Reviews','RankReview']:
        print("Error: invalid file format")
        # terminate the program
        return None,None,None,None
    except:
      print("Error: invalid file format")
      # terminate the program
      return None,None,None,None
    l=len(data[0])
    lines=f.readlines()
    for line in lines:
      if len(line.strip().split(','))!=l:
        # skip the line if the number of items is not the same as the header or invalid
        pass
      else:
        data.append(line.strip().split(','))
    # Fixing Location ID error
    try:
      if len(idlist)==0:
        print("Error: no location ID is given")
        # terminate the program
        return None,None,None,None
      # make sure the location ID is valid
      for id in idlist:
        if Find(id,data)==-1:
          print("Error: location ID not found")
          # terminate the program
          return None,None,None,None
    except:
      print("Invalid location ID")
      # terminate the program
      return None,None,None,None
    # make sure the radius is valid
    try:
      if radius<0:
        # terminate the program
        print("Invalid radius")
        return None,None,None,None
    except:
      print("Invalid radius")
      # terminate the program
      return None,None,None,None
    # add the distance to the data for Location ID 1 and 2
    locId1=idlist[0]
    locId2=idlist[1]
    distancefromC1=[]
    distancefromC2=[]
    for i in range(1,len(data)):
      # append the distance from Location ID 1 to each item in the data
      distancefromC1.append(round(distance(float(data[i][1]),float(data[i][2]),float(data[Find(locId1, data)][1]),float(data[Find(locId1, data)][2])),4))
    for j in range(1,len(data)):
      # append the distance to the Location ID 2 to each item in the data
      distancefromC2.append(round(distance(float(data[j][1]),float(data[j][2]),float(data[Find(locId2, data)][1]),float(data[Find(locId2, data)][2])),4))
    #  add distance from locId1 and locId2 to data
    data[0].append('Distance from '+locId1)
    data[0].append('Distance from '+locId2)
    for i in range(1,len(data)):
      data[i].append(str(distancefromC1[i-1]))
      data[i].append(str(distancefromC2[i-1]))
    # find unique categories
    categories=[]
    for line in data[1:]:
      if line[3] not in categories:
        categories.append(line[3])
    # find C1 and C2 regions
    C1=[]
    C2=[]
    for i in range(1,len(data)):
      if distance(float(data[i][1]), float(data[i][2]), float(data[Find(locId1, data)][1]), float(data[Find(locId1, data)][2]))<=radius:
        C1.append(data[i])
      if distance(float(data[i][1]), float(data[i][2]), float(data[Find(locId2, data)][1]), float(data[Find(locId2, data)][2]))<=radius:
        C2.append(data[i])
    # find Lcount
    LDCount=[]
    # find the number of items in each category in C1
    LDCount.append(Countcat(categories, C1))
    # find the number of items in each category in C2
    LDCount.append(Countcat(categories, C2))
    # finding Common data
    # a list to store the common data
    common=[]
    # loop through the C1 and C2
    for i in range(len(C1)):
      for j in range(len(C2)):
        if C1[i][0]==C2[j][0]:
          # if the item is in both C1 and C2
          common.append(C1[i])
    # a dictionary to store the common data
    Dcommon={}
    # loop through the common data categories
    for category in categories:
      Dcommon[category]=[]
      for item in common:
        if item[3]==category:
          # if the item is in the category
          Dcommon[category].append(item[0])
    # Cosine Similarity of C1 and C2 using Function CosineSmilarity
    simScore=CosineSmilarity(LDCount[0],LDCount[1])
    # Lclose Section
    categories_P_C1=[]
    categories_H_C1=[]
    categories_R_C1=[]
    categories_C_C1=[]
    categories_S_C1=[]
    categories_P_C2=[]
    categories_H_C2=[]
    categories_R_C2=[]
    categories_C_C2=[]
    categories_S_C2=[]
    for i in range(0,len(C1)):
        if C1[i][3] == 'P':
            if float(C1[i][-2]) != 0.0000:
                categories_P_C1.append((C1[i][0],float(C1[i][-2])))
        elif C1[i][3] == 'H':
            if float(C1[i][-2]) != 0.0000:
                categories_H_C1.append((C1[i][0],float(C1[i][-2])))
        elif C1[i][3] == 'R':
            if float(C1[i][-2]) != 0.0000:
                categories_R_C1.append((C1[i][0],float(C1[i][-2])))
        elif C1[i][3] == 'C':
            if float(C1[i][-2]) != 0.0000:
                categories_C_C1.append((C1[i][0],float(C1[i][-2])))
        elif C1[i][3] == 'S':
            if float(C1[i][-2]) != 0.0000:
                categories_S_C1.append((C1[i][0],float(C1[i][-2])))
    for j in range(0,len(C2)):
        if C2[j][3] == 'P':
            if float(C2[j][-1]) != 0.0000:
                categories_P_C2.append((C2[j][0],float(C2[j][-1])))
        elif C2[j][3] == 'H':
            if float(C2[j][-1]) != 0.0000:
                categories_H_C2.append((C2[j][0],float(C2[j][-1])))
        elif C2[j][3] == 'R':
            if float(C2[j][-1]) != 0.0000:
                categories_R_C2.append((C2[j][0],float(C2[j][-1])))
        elif C2[j][3] == 'C':
            if float(C2[j][-1]) != 0.0000:
                categories_C_C2.append((C2[j][0],float(C2[j][-1])))
        elif C2[j][3] == 'S':
            if float(C2[j][-1]) != 0.0000:
                categories_S_C2.append((C2[j][0],float(C2[j][-1])))
    LDClose=[{},{}]
    # LDClose[0]['P']=lowest non-zero distance tuple from category_P_C1
    if len(categories_P_C1)!=0:
        LDClose[0]['P']=min(categories_P_C1, key=lambda x: x[1])
    # LDClose[0]['H']=lowest non-zero distance tuple from category_H_C1
    if len(categories_H_C1)!=0:
        LDClose[0]['H']=min(categories_H_C1, key=lambda x: x[1])
    # LDClose[0]['R']=lowest non-zero distance tuple from category_R_C1
    if len(categories_R_C1)!=0:
        LDClose[0]['R']=min(categories_R_C1, key=lambda x: x[1])
    # LDClose[0]['C']=lowest non-zero distance tuple from category_C_C1
    if len(categories_C_C1)!=0:
        LDClose[0]['C']=min(categories_C_C1, key=lambda x: x[1])
    # LDClose[0]['S']=lowest non-zero distance tuple from category_S_C1
    if len(categories_S_C1)!=0:
        LDClose[0]['S']=min(categories_S_C1, key=lambda x: x[1])
    # LDClose[1]['P']=lowest non-zero distance tuple from category_P_C2
    if len(categories_P_C2)!=0:
        LDClose[1]['P']=min(categories_P_C2, key=lambda x: x[1])
    # LDClose[1]['H']=lowest non-zero distance tuple from category_H_C2
    if len(categories_H_C2)!=0:
        LDClose[1]['H']=min(categories_H_C2, key=lambda x: x[1])
    # LDClose[1]['R']=lowest non-zero distance tuple from category_R_C2
    if len(categories_R_C2)!=0:
        LDClose[1]['R']=min(categories_R_C2, key=lambda x: x[1])
    # LDClose[1]['C']=lowest non-zero distance tuple from category_C_C2
    if len(categories_C_C2)!=0:
        LDClose[1]['C']=min(categories_C_C2, key=lambda x: x[1])
    # LDClose[1]['S']=lowest non-zero distance tuple from category_S_C2
    if len(categories_S_C2)!=0:
        LDClose[1]['S']=min(categories_S_C2, key=lambda x: x[1])            
    # return the data, categories, LDCount, LDClose, simScore
    return LDCount,simScore,Dcommon,LDClose

# function to calculate the distance between two points in a plane
def distance(lat1, lon1, lat2, lon2):
  return ((lat1-lat2)**2 + (lon1-lon2)**2)**0.5

# function to find the location ID in the data
def Find(locId, data):
  for i in range(len(data)):
    # if the location ID is found, return the index
    if data[i][0]==locId:
      return i
  return -1

# function to count the number of items in each category
def Countcat(categories, data):
  count={}
  for category in categories:
    # initialize the count of each category to 0
    count[category]=0
  for line in data:
    if line[3] in categories:
      # count the number of items in each category
      count[line[3]]+=1
  return count

# function to calculate the cosine similarity
def CosineSmilarity(Dict1,Dict2):
  # make sure the two dictionaries have the same keys
  keys1=list(Dict1.keys())
  keys2=list(Dict2.keys())
  if len(keys1) != len(keys2):
    # if the two dictionaries do not have the same keys, return 0
    return 0
  # calculate the sum of the squares of the differences
  sum=0
  for key in keys1:
    sum+=Dict1[key]*Dict2[key]
  # calculate the square root of the sum of the squares
  sqr1=0
  sqr2=0
  for key in keys1:
    sqr1+=Dict1[key]**2
    sqr2+=Dict2[key]**2
  sqr1=sqr1**0.5
  sqr2=sqr2**0.5
  k = sum/(sqr1*sqr2)
  # return only k 4 floting point numbers
  return round(k,4)

if __name__ == '__main__':
    # example 1:
    #Testing example 1 output
    # LDC1, SS1, DC1, LDCl1 = main("Locations.csv", ["L26", "L52"], 3.5)
    # LDCref = [{'P': 1, 'H': 3, 'R': 2, 'C': 2, 'S': 3}, {'P': 3, 'H': 2, 'R': 1, 'C': 0, 'S': 2}]
    # flag = True
    # for idx in range(2):
    #     for ditem in LDCref[idx]:
    #         if LDCref[idx][ditem] != LDC1[idx][ditem]:
    #             flag = False
    # print(flag)
    # # output 2:
    # SSref = 0.7711
    # print(SSref == SS1)
    # # output 3:
    # DCref = {'P': ['L26'], 'H': ['L52', 'L22'], 'R': ['L88'], 'C': [], 'S': ['L30']}
    # flag = True
    # for ditem in DCref:
    #     for litem in DCref[ditem]:
    #         if not (litem in DC1[ditem]):
    #             flag = False
    # print(flag)
    # # output 4:
    # LDClref = [{'H': ('L77', 2.3034), 'R': ('L88', 0.7736), 'C': ('L29', 2.0607), 'S': ('L65', 1.556)}, {'P': ('L46', 2.4717), 'H': ('L22', 1.4374), 'R': ('L88', 2.5338), 'S': ('L30', 2.0482)}]
    # flag = True
    # for idx in range(2):
    #     for ditem in LDClref[idx]:
    #         if LDClref[idx][ditem] != LDCl1[idx][ditem]:
    #             flag = False
    # print(flag)
    # example 2:
    #Testing example 2 output
    LDC1, SS1, DC1, LDCl1 = main("Locations.csv" , ["L89", "L15"], 4.3)
    LDCref = [{'P': 3, 'H': 2, 'R': 3, 'C': 4, 'S': 1}, {'P': 2, 'H': 4, 'R': 3, 'C': 1, 'S': 4}]
    SSref = 0.7319
    flag = True
    for idx in range(2):
        for ditem in LDCref[idx]:
            if LDCref[idx][ditem] != LDC1[idx][ditem]:
                flag = False
    print(flag)
    if SSref != SS1:
        flag = False
    print(flag)
    # output 5:
    DCref = {'P': ['L26'], 'H': ['L77'], 'R': ['L88'], 'C': ['L4'], 'S': []}
    flag = True
    for ditem in DCref:
        for litem in DCref[ditem]:
            if not (litem in DC1[ditem]):
                flag = False
    print(flag)
    # output 6:
    LDClref = [{'P': ('L31', 1.6058), 'H': ('L17', 3.0011), 'R': ('L48', 3.0555), 'C': ('L84', 1.7586), 'S': ('L65', 2.1059)}, {'P': ('L26', 3.2431), 'H': ('L77',1.4124), 'R': ('L38', 2.5739), 'C': ('L4', 4.2148), 'S': ('L30', 2.3415)}]
    flag = True
    for idx in range(2):
        for ditem in LDClref[idx]:
            if LDClref[idx][ditem] != LDCl1[idx][ditem]:
                    flag = False
    print(flag)
