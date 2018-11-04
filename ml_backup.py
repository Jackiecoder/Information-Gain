from mldata import parse_c45
from math import log2

print(' ')
dataset = parse_c45("example")
print(dataset.schema[4].type)
print(dataset.schema[4].values)
print(dataset[1])
print(set(dataset[1]))


# def entropy(p)
#     summary = 0
#     #H(X)=-sum(px*log2(px))
#     for px in p:
#         px = px/sum(p)
#         if p != 0:
#             summary += px * log2(px,2)
    
#     reture (summary* -1)

# def informationGain(data, x=None)
#     #IG = H(y) - H(y|x)
#     summary = 0
#     for i in x:
#         summary += sum(i)/sum(d)*entropy(i)
        
#     ig = entropy(data)- summary

#     reture ig
