##import re
##t="A fat cat doesn't eat oat but a rat eats bats."
##mo = re.findall("[forceb]at", t)
##print(mo)
###############################################3
##import re
##str = "Course location is London and Paris!"
##mo = re.search(r"location.*(London|Paris|Zurich|Strasbourg)",str)
##if mo: print(mo.group())
#######
##str = "Course location is Bangkok and Paris!"
##mo = re.search(r"location.*(London|Paris|Zurich|Strasbourg)",str)
##if mo: print(mo.group())
#######
##str = "Course location is Bangkok and New York!"
##mo = re.search(r"location.*(London|Paris|Zurich|Strasbourg)",str)
##if mo: print(mo.group())
