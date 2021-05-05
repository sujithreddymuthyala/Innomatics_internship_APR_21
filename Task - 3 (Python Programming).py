#!/usr/bin/env python
# coding: utf-8

# ### Integers Come In All Sizes
# 
# 

# In[ ]:


a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(pow(a,b)+pow(c,d))


# ### Power - Mod Power

# In[ ]:


a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
print(pow(a,b,m))


# ### Mod Divmod

# In[ ]:


a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a,b))


# ### Triangle Quest 2
# 
# 

# In[66]:


for i in range(1,int(input())+1):
     print((10**i//9)**2)
    
    
    


# ### Polar Coordinates

# In[70]:


complex(2,3)


# In[89]:


import cmath
from cmath import phase

c=complex(input())
r=((c.real)**2+(c.imag)**2)**0.5
n=phase(c)
print(r)
print(n)


# ### triangle quest 

# In[39]:


for i in range(1,int(input())):
    print(i*(10**i)//9)
    
    


# ### Find Angle MBC
# 

# In[110]:


from math import asin
ab=int(input())
bc=int(input())
ac=((ab)**2+(bc)**2)**0.5
mc=ac/2
angle=(asin(mc/bc))
q=math.degrees(angle)
print(round(q))


# In[29]:


import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle 
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')


# In[ ]:




