'''
Kesar Sampat 
Period 3 HCP
Unit 1 - IPO
Finding state facts and make a table using zone formatting 
'''

strFormatData = "{0:<16s}{1:>16f}{2:>16s}{3:>16s}"
strFormatTitles = "{0:^10s}{1:^12s}{2:^22s}{3:^14}"


print(strFormatTitles.format("State", "   \tPopulation (mil)" , "Area(sq mi)" , "Median"))
print(strFormatData.format("Pennsylvania" , 12784227/1000000 ,"46,055" , "$60,905"))
print(strFormatData.format("California" ,39512223/1000000 ,  "163,696" ,"$71,228"))
print(strFormatData.format("New York" , 19453561/1000000, "54,555" , "$50,825"))
print(strFormatData.format("Ohio" , 11689100/1000000 , "44,825" , "$56,111"))
print(strFormatData.format("Texas" , 28995881/1000000, "268,596" ,  "$59,570"))




