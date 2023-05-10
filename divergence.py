"""hehjhdhj"""

class DivergenceCalculator:
    """hfhejhf"""
    sensors=[]
    environments ={}

    def addsensors(self,sensor):
        """adds a new sensor to the sensors list"""
        if ((sensor == 'mono' or sensor == 'monoi' or sensor == 'stereo' or sensor == 'stereoi' or sensor == 'RGB') and not(sensor in self.sensors)):
            self.sensors.append(sensor)

    def addenvironments(self,environment, difficulty):
        """adds a new environment to the environments list"""
        if (difficulty == 'easy' or difficulty == 'medium' or difficulty == 'difficult'):
            self.environments[environment] = difficulty

    def readfiles(self,file1):
        """Returns a dictionnary where the values represent a line in the file"""
        file1 = 'ressources/TextFiles/'+file1
        with open(file1, 'r') as f:
            content = f.readlines()
        endcontent = {}
        for indexi,elementi in enumerate(content):
            newcontent = content[indexi].strip()
            for indexj,elementj in enumerate(newcontent):
                endcontent[indexj] = newcontent.split(' ')
        return endcontent
    
    def keyframedivergence(self,sensor, groundtruth):
        """Returns the percentage of keyframes captured by the selected sensor"""

        sensorkf = len(sensor)
        groundtruthkf = len(groundtruth)
        return str(round((sensorkf/groundtruthkf)*100, 2))+"%"
    
    def allkfdivergence(self):
        """Return a dictionnary with all the keyframes percentages"""

        final = {}
        environmentsnames = list(self.environments.keys())
        for i,elementj in enumerate(environmentsnames):
            for j,elementi in enumerate(self.sensors):
                file1 = 'kf_dataset-'+elementj+'_'+elementi+'.txt'
                file2 = elementj+'_GT.txt'
                final[elementj+'_'+elementi
                     ] = (self.keyframedivergence(self.readfiles(file1), self.readfiles(file2)))
        return final
    
    def kfenvironment(self):
        """ghfhfhbj"""
        allkfdivergencelist=list(self.allkfdivergence().values())
        final=[]
        for i, element in enumerate(allkfdivergencelist):
            final.append(float(element[:len(element)-1]))
        return final
    
    def kfenvironmenttostring(self, kf):
        """jifj"""
        result=""
        for i, element in enumerate(kf):
            if(i<len(kf)-1):
                result= result+str(element)+"%, "
            else:
                result= result+str(element)+"%"
        return result

    def sensorkfbydifficultyincreasing(self,name):
        """hfh"""
        result=[]
        for i, element in enumerate(self.environments):
            if(element[:2]==name):
                result.append(element)
        return result

"""
d= DivergenceCalculator()
d.addenvironments("MH01","easy")
d.addenvironments("MH03","easy")
d.addenvironments("MH05","easy")
d.addsensors("mono")
print(d.allkfdivergence())
print(d.sensorkfbydifficultyincreasing("MH"))
"""