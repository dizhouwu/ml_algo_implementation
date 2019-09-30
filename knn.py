#!/usr/bin/env python
# coding: utf-8

# In[49]:


import math
from typing import List


# In[50]:


def euclidean_dist(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += pow((instance1[i]-instance2[i]),2)
    return math.sqrt(distance)


# In[51]:


import operator

def get_neighbors(train, test, k):
    distances = []
    length = len(test)-1
    for i in range(len(train)):
        dist = euclidean_dist(test, train[i],length)
        distances.append((train[i],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors


# In[52]:


train = [[2,2,2,'a'],[4,4,4,'b']]
test = [5,5,5]
neighbors = get_neighbors(train=train,test=test, k=2)
print(neighbors)


# In[53]:


def get_response(neighbors):
    class_votes={}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in class_votes:
            class_votes[response] +=1
        else:
            class_votes[response]=1
    sorted_votes = sorted(class_votes.items(),key=operator.itemgetter(1))
    return sorted_votes[0][0]


# In[54]:


neighbors = [[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
response = get_response(neighbors)
print(response)


# In[55]:


def get_accuracy(test, predictions):
    correct = 0
    for i in range(len(test)):
        if test[i][-1] == predictions[i]:
            correct +=1
    return (correct/float(len(test)))*100.0


# In[56]:


test = [[1,1,1,'a'],
       [2,2,2,'a'],
        [3,3,3,'b']]


# In[57]:


predictions = ['a','a','a']
accuracy = get_accuracy(test, predictions)
accuracy


# In[ ]:





# In[ ]:




