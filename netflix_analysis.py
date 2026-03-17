# Netflix Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# -------------------- Data Cleaning --------------------

# Drop rows with missing important values
df = df.dropna(subset=['country', 'rating'])

# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Extract year added
df['year_added'] = df['date_added'].dt.year

# -------------------- Most Popular Genres --------------------

# Split and explode genres
df['listed_in'] = df['listed_in'].str.split(',')
df['listed_in'] = df['listed_in'].apply(lambda x: [i.strip() for i in x])
genres = df.explode('listed_in')

# Count top 10 genres
genre_count = genres['listed_in'].value_counts().head(10)

# Plot genres
plt.figure()
sns.barplot(x=genre_count.values, y=genre_count.index, palette="viridis")
plt.title("Top 10 Genres on Netflix", fontsize=14)
plt.xlabel("Count", fontsize=12)
plt.ylabel("Genre", fontsize=12)
plt.show()

# -------------------- Release Trends --------------------

release_trend = df['release_year'].value_counts().sort_index()

plt.figure()
release_trend.plot()
plt.title("Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.show()

# -------------------- Ratings Analysis --------------------

rating_count = df['rating'].value_counts()

plt.figure()
rating_count.plot(kind='bar')
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# -------------------- Movies vs TV Shows --------------------

type_count = df['type'].value_counts()

plt.figure()
type_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Movies vs TV Shows")
plt.ylabel("")
plt.show()

# -------------------- Top Countries --------------------

country_count = df['country'].value_counts().head(10)

plt.figure()
country_count.plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()