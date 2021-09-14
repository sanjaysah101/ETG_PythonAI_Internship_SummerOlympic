import pandas as pd
import matplotlib.pyplot as plt

# 1. In how many cities Summer Olympics is held so far?

df = pd.read_csv(r"C:\Users\Bibek\OneDrive\Desktop\Internship\Assignment 2\CSV\summer.csv")
# print(df)
city = len(df['City'].unique())
print(f'In {city} Cities Summer Olympics was held so far.')
# len(df['City'].unique())


# 2. Which sport is having most number of Gold Medals so far? (Top 5)

gold= df[df['Medal']=='Gold']
# print(gold)
data = []
for sport in gold['Sport'].unique():
  data.append([sport, len(gold[gold['Sport']==sport])])

data = pd.DataFrame(data, columns=['Sport', 'Gold']).sort_values(by='Gold', ascending=False).head()
# data.plot(x='Sport', y='Gold', kind='bar', color='gold')
plt.bar(data['Sport'], data['Gold'], color = 'gold')
plt.title('Sports Vs Gold', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Gold', fontsize= 14)
print(data)
plt.show()



# 3. Which sport is having most number of medals so far? (Top 5)

most = df.groupby('Sport').count()['Medal'].sort_values(ascending=False).head()

print(most)

most.plot.bar(color='orange')
plt.show()


# 4. Which player has won most number of medals? (Top 5)

df.groupby('Athlete').count()['Medal'].sort_values(ascending=False).head().plot.bar(color='#49a7c3')
plt.show()





# 5. Which player has won most number Gold Medals of medals? (Top 5)
gold.groupby('Athlete').count()['Medal'].sort_values(ascending=False).head(5).plot.bar(color='orange')
plt.show()

# 6. In which year India won first Gold Medal in Summer Olympics?
firstGolod = gold[gold['Country']=='IND']['Year'].min()
print(firstGolod)

# 7. Which event is most popular in terms on number of players? (Top 5)

event = df.groupby("Event").count()['Athlete'].sort_values(ascending=False).head(5).plot.bar(color='green')
plt.show()



# 8. Which sport is having most female Gold Medalists?
goldFemale = gold[gold['Gender']=='Women']
data=[]
for sport in goldFemale['Sport'].unique():
  data.append([sport, len(goldFemale[goldFemale['Sport']==sport])])

data= pd.DataFrame(data, columns=['Sport', 'GoldFemale']).sort_values(by='GoldFemale', ascending=False).head()
data.plot(x='Sport' ,y='GoldFemale', kind='bar', figsize=(10, 5))
plt.show()