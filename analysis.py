import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#read the dataset
df=pd.read_csv("dataset.csv")
print(df.head())
#Size of Dataset:
df.shape
#information of dataset
print("\nInformation:\n")
print(df.describe())
#adding a new column of Sorted Names Alphabatically:
df['Sorted_Name']=sorted(df['Name'])
print(df)
#calclate average age:
avg_age=df["Age"].mean()
print(f"Average Age:{avg_age}")
#calculating Maxium age:
max_age=df["Age"].max()
print(f"Maximum age:{max_age}")
#Calculating minimum age:
min_age=df["Age"].min()
print(f"Minimum age:{min_age}")
#Adding a new column by sorting age:
df['Sorted_Age']=sorted(df['Age'])
print(df)
#counting number of males and females:
print(df['Gender'].value_counts())
df['Is_Male']=(df['Gender']=='Male').astype(int)
df['Is_Female']=(df['Gender']=='Male').astype(int)
print(df)
#count of current educational level:
print(df['Current educational level'].value_counts())
df['Is_Graduate']=(df['Current educational level']=='Graduate').astype(int)
df['Is_Undergraduate']=(df['Current educational level']=='Undergraduate').astype(int)
df['Is_HighSchool']=(df['Current educational level']=='High School').astype(int)
print(df)
#Calulating Highest Spending category for each student:
df['Highest_Spending']=df[['Rent/Room Accommodation','Utilities','Groceries','Dining Out/Eating Outside','Public Transportation','Fuel/Car Maintenance','Tuition Fees','Books and Supplies','Online Courses/Subscriptions','Clothing/Shoes','Entertainment','Health Insurance/Medical Expenses','Gym Memberships/Physical Activities','Mobile Phone/Internet Bill']].idxmax(axis=1)
print(df)
#calculating highest spending student:
i=df['Final Monthly Expense'].idxmax()
print(f"Highest Spending Student:{df['Name'][i]}")
#Average Spending on Each category:
avg_spending=df[['Rent/Room Accommodation','Utilities','Groceries','Dining Out/Eating Outside','Public Transportation','Fuel/Car Maintenance','Tuition Fees','Books and Supplies','Online Courses/Subscriptions','Clothing/Shoes','Entertainment','Health Insurance/Medical Expenses','Gym Memberships/Physical Activities','Mobile Phone/Internet Bill']].mean()    
print(avg_spending)
#Spending by Gender:
print(df.groupby('Gender')['Final Monthly Expense'].mean())
#category wise total:
category_total=df[['Rent/Room Accommodation','Utilities','Groceries','Dining Out/Eating Outside','Public Transportation','Fuel/Car Maintenance','Tuition Fees','Books and Supplies','Online Courses/Subscriptions','Clothing/Shoes','Entertainment','Health Insurance/Medical Expenses','Gym Memberships/Physical Activities','Mobile Phone/Internet Bill']].sum()
print(f"category wise toal:{category_total}")
#total spendings:
total_spending=category_total.sum()
print(f"Total Spendings: {total_spending}")
#percentage of spendings:
Percentage=(category_total/total_spending)*100
print(f"Percentage Spendings:{Percentage}")
#calculate correlation:
correlation=df.select_dtypes(include='number').corr()
print(f"Correlations:{correlation}")
#visualizations:
#1. Pie chart for male female distribution:
categories=(["Males","Females"])
values=df['Gender'].value_counts()
colors=["blue","pink"]
plt.figure(figsize=(6,6))
plt.pie(values,labels=categories,autopct="%1.1f%%",colors=colors,shadow=True)
plt.title("Gender Distribution",fontsize=25,
                                fontweight="bold",
                                color="red")
plt.show()   
#Count Plot for male female distribution:
plt.figure(figsize=(8,5))
sns.set_style('darkgrid')
sns.countplot(x='Gender',data=df,color='darkblue')
plt.title("Gender Distribution",fontsize=25,
                                fontweight="bold",
                                color="red")
plt.show() 
#2.Pie chart for current educational status distribution:
categories=(["Graduate","Undergraduate","Highschool"]) 
values=df['Current educational level'].value_counts()
colors=["red","green","yellow"] 
plt.figure(figsize=(6,6))
plt.pie(values,labels=categories,autopct="%1.1f%%",colors=colors,shadow=True)
plt.title("Current educational level distribution",fontsize=15,
                                                   fontweight="bold",
                                                   color="darkblue")
plt.show()  
#count plot for current educational level distribution:  
plt.figure(figsize=(8,5))
sns.set_style('darkgrid')
sns.countplot(x='Current educational level',data=df,color='darkblue') 
plt.title("Current educational level distribution",fontsize=15,
                                                   fontweight="bold",
                                                   color="black")
plt.show() 
#3.countplot of highest spending catogiery for each student :
plt.figure(figsize=(8,5))
sns.set_style('darkgrid')
sns.countplot(x='Highest_Spending',data=df,color='darkblue',linewidth=2,edgecolor='white')
plt.title("Highest Spending Catogiery For Each Student",fontsize=15,
                                                        fontweight="bold",
                                                        color="black") 
plt.show() 
#4.bar plot for highest spending student with highest spender:
top=df.sort_values(by='Final Monthly Expense',ascending=False).head(10)
colors=['skyblue']*len(top)
colors[0]='red'
plt.figure(figsize=(8,4))
plt.barh(top['Name'],top['Final Monthly Expense'],color=colors)
plt.title("Top 10 Highest Spending Students (Highlighted)",fontsize=15,
                                                           fontweight="bold",
                                                           color="black") 
plt.xlabel("Names",fontsize=12,
                   fontweight="bold",
                   color="darkblue")                                                                                                                
plt.ylabel("Final Monthly Expenses",fontsize=12,
                                    fontweight="bold",
                                    color="darkblue") 
plt.yticks(fontsize=8)                                     
plt.show()
#Bar plot for catogory wise avg:
avg_spending=df[['Rent/Room Accommodation','Utilities','Groceries','Dining Out/Eating Outside','Public Transportation','Fuel/Car Maintenance','Tuition Fees','Books and Supplies','Online Courses/Subscriptions','Clothing/Shoes','Entertainment','Health Insurance/Medical Expenses','Gym Memberships/Physical Activities','Mobile Phone/Internet Bill']].mean().to_numpy()                                        
categories=np.array(['Rent/Room Accommodation','Utilities','Groceries','Dining Out/Eating Outside','Public Transportation','Fuel/Car Maintenance','Tuition Fees','Books and Supplies','Online Courses/Subscriptions','Clothing/Shoes','Entertainment','Health Insurance/Medical Expenses','Gym Memberships/Physical Activities','Mobile Phone/Internet Bill'])
plt.barh(categories,avg_spending,color='darkblue')
plt.title("Category wise Avg. spendings",fontsize=12,
                                         fontweight="bold",
                                         color="darkblue")
plt.xlabel('Categories',fontsize=12,
                         fontweight='bold',
                         color='black')  
plt.ylabel('Avg. Spendings',fontsize=12,
                            fontweight='bold',
                            color='black')  
plt.yticks(fontsize=5,rotation=45,ha='right')                             
plt.show()  
#5.pie chart for spending by gender:
values=df.groupby('Gender')['Final Monthly Expense'].mean().to_numpy()
categories=(['spendings by male','spending by female'])
colors=['blue','pink']
plt.figure(figsize=(6,6))
plt.pie(values,labels=categories,autopct="%1.1f%%",colors=colors,shadow=True,startangle=45)
plt.title("Spendings By Gender",fontsize=25,
                                fontweight='bold',
                                color='red')  
plt.show()  
#6.pie chart for percentage spending:
plt.figure(figsize=(10,10))

plt.pie(Percentage,autopct='%1.1f%%',
        startangle=90,labeldistance=1.1,pctdistance=0.8, shadow=True)

plt.title("Percentage Spending by Category", fontsize=14, fontweight='bold')
plt.legend(Percentage.index,loc="best")

plt.show()   
#7.Heatmap for correlation:
plt.figure(figsize=(12,8))

sns.heatmap(correlation)

plt.title("Correlation Matrix", fontsize=25, fontweight='bold')
plt.xticks(fontsize=10)

plt.show()                          






