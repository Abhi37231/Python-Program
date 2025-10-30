import pandas as pd 

data = { 
        
        'Name' : ['Abhinandan ', ' Bob' , ' charlie'],
        'Age': [21 , 22 , 30 ],
        'city' : ['Sangli' , 'pune'  , 'Mumbai']
        }

df = pd.DataFrame(data)

print("DataFrame:")
print(df)


print ("\nFirst 2 rows:\n",df)

print("\nInfo about dataFrame:")
print(df.info())

print ("\nNames column:\n",df[df['Age']>24])

df['Country']= 'India'
print("\nDataframe after adding country:\n",df)