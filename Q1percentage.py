# The company produces a nutrition bar that contains 50g of raisins, 60g of almonds, and 20g of apricots. 
# The head of the manufacturing department wants you to create an ingredient percentage list for the nutrition bar using python.
# Equipped with the knowledge of int, 
# float and booleans in python, how would you approach this situation?

almonds= 60
raisins= 50
apricots=20

total=almonds+raisins+apricots

percentage_of_almonds = (almonds/total)*100
percentage_of_raisins= (raisins/total)*100
percentage_of_apricots= (apricots/total)*100

print("% of almonds=",percentage_of_almonds," % of raisins=",percentage_of_raisins,"% of apricots=",percentage_of_apricots)
