movies = [
    {"title": "Avatar", "rating": 8.5, "year": 2009},
    {"title": "Titanic", "rating": 8.0, "year": 1997},
    {"title": "Interstellar", "rating": 9.0, "year": 2014},
    {"title": "Inception", "rating": 8.8, "year": 2010}
]
print ("Retingi 8.5 yuqori bolgan filimlar")
for film in movies:
    if film['rating'] >= 8.5:
        print(film['title'], end=', ') 
        
        
print ('2010 yil chiqqan filimlar')     
for film in movies:
    if film['year'] >= 2010:
        print(film['title'], end=', ') 
