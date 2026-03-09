import pandas as pd

df = pd.read_csv("US_Accidents_March23.csv", encoding="latin1")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df = df.dropna(subset=['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
import matplotlib.pyplot as plt

df['Hour'].value_counts().sort_index().plot(kind='bar')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()
print(df['Weather_Condition'].value_counts().head(10))
df['Weather_Condition'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Weather Conditions During Accidents")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.show()
df['Severity'].value_counts().plot(kind='bar')
plt.title("Accident Severity Distribution")
plt.xlabel("Severity Level")
plt.ylabel("Number of Accidents")
plt.show()
road_conditions = df[['Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal']]

print(road_conditions.sum().sort_values(ascending=False))
sample_df = df.sample(10000, random_state=42)

plt.figure(figsize=(8,6))
plt.scatter(sample_df['Start_Lng'], sample_df['Start_Lat'], s=1)
plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
df.groupby('Weather_Condition')['Severity'].mean().sort_values(ascending=False)
