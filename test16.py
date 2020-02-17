##import re
##mo = re.search("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")
##print(mo.group(), '************1')
##print(mo.group(1), '***********2')
##print(mo.group(2), '************3')
##print(mo.group(1,2), '************4')
##mo = re.search("([0-9]+).*", "Customer number: 232454, Date: February 12, 2011")
##print(mo.group(), '************1')
##print(mo.group(1), '***********2')
##print(mo.group(2), '************3')
##print(mo.group(1,2), '************4')
############################################################
##import re
##mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
##print(mo.group(), '******1')
##print(mo.span(), '*********2')
##s=mo.start()
##print(s, '**********3')
##print("Customer number: 232454, Date: February 12, 2011"[s])
##e=mo.end()
##print(e, '**********4')
##print("Customer number: 232454, Date: February 12, 2011"[e])
##print(mo.span()[0])
##print(mo.span()[1])
###################################################################
##import re
##fh = open("tags.txt")
##for i in fh:
##     res = re.search(r"<([a-z]+)>(.*)</\1>",i)
##     print(res.group(1) + ": " + res.group(2))
###################################################################
##import re
##l = ["555-8396 Neu, Allison", 
##     "Burns, C. Montgomery", 
##     "555-5299 Putz, Lionel",
##     "555-7334 Simpson, Homer Jay"]
##for i in l:
##    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
##    print(res.group(3) + " " + res.group(2) + " " + res.group(1))

























