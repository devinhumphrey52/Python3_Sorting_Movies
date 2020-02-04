# Build a dictionary containing the specified movie collection
movies_dict = {
     2005: [['Munich', 'Steven Spielberg']],
     2006: [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']],
     2007: [['Into the Wild', 'Sean Penn']],
     2008: [['The Dark Knight', 'Christopher Nolan']],
     2009: [['Mary and Max', 'Adam Elliot']],
     2010: [["The King's Speech", 'Tom Hooper']],
     2011: [['The Artist', 'Michel Hazanavicius'], ['The Help', 'Tate Taylor']],
     2012: [['Argo', 'Ben Affleck']],
     2013: [['12 Years a Slave', 'Steve McQueen']],
     2014: [['Birdman', 'Alejandro G. Inarritu']],
     2015: [['Spotlight', 'Tom McCarthy']],
     2016: [['The BFG', 'Steven Spielberg']]
    };

# Prompt the user for a year
user_year = int(input('Enter a year between 2005 and 2016:\n'))

# Displaying the title(s) and directors(s) from that year
if (user_year < 2005) or (user_year > 2016):
    print('N/A\n')
elif user_year == 2005:
    print('%s, %s\n' % (movies_dict[2005][0][0], movies_dict[2005][0][1]))
elif user_year == 2006:
    print('%s,' % movies_dict[2006][0][0], movies_dict[2006][0][1])
    print('%s, %s\n' % (movies_dict[2006][1][0], movies_dict[2006][1][1]))
elif user_year == 2007:
    print('%s, %s\n' % (movies_dict[2007][0][0], movies_dict[2007][0][1]))
elif user_year == 2008:
    print('%s, %s\n' % (movies_dict[2008][0][0], movies_dict[2008][0][1]))
elif user_year == 2009:
    print('%s, %s\n' % (movies_dict[2009][0][0], movies_dict[2009][0][1]))
elif user_year == 2010:
    print('%s, %s\n' % (movies_dict[2010][0][0], movies_dict[2010][0][1]))
elif user_year == 2011:
    print('%s,' % movies_dict[2011][0][0], movies_dict[2011][0][1])
    print('%s, %s\n' % (movies_dict[2011][1][0], movies_dict[2011][1][1]))
elif user_year == 2012:
    print('%s, %s\n' % (movies_dict[2012][0][0], movies_dict[2012][0][1]))
elif user_year == 2013:
    print('%s, %s\n' % (movies_dict[2013][0][0], movies_dict[2013][0][1]))
elif user_year == 2014:
    print('%s, %s\n' % (movies_dict[2014][0][0], movies_dict[2014][0][1]))
elif user_year == 2015:
    print('%s, %s\n' % (movies_dict[2015][0][0], movies_dict[2015][0][1]))
else:
    print('%s, %s\n' % (movies_dict[2016][0][0], movies_dict[2016][0][1]))

# Displays menu and carries out the desired option: Display movies by year, display movies by director, display movies by movie title, or quit
while True:
    movie_menu_input = input('MENU\nSort by:\ny - Year\nd - Director\nt - Movie title\nq - Quit\n\nChoose an option:\n')
    if movie_menu_input != 'q':
        if movie_menu_input == 'y':
            for year in sorted(movies_dict.keys()):
                print(year, end = ':\n')
                for movie in movies_dict[year]:
                    print('\t%s, %s' % (movie[0], movie[1]))
                print('')
        if movie_menu_input == 'd':
            directors_dict = {}
            for key in sorted(movies_dict.keys()):
                for movie in movies_dict[key]:
                    director = movie[1]
                    if director in directors_dict:
                        directors_dict[director].append([movie[0],key])
                    else:
                        directors_dict[director] = [[movie[0],key]]
            for key in sorted(directors_dict.keys()):
                print(key, end = ':')
                print('')
                for director in directors_dict[key]:
                    print("\t"+ str(director[0])+ ", "+str(director[1]))
                print('')
        if movie_menu_input == 't':
            titles_dict = {}
            for key in sorted(movies_dict.keys()):
                for movie in movies_dict[key]:
                    title = movie[0]
                    if title in titles_dict:
                        titles_dict[title].append([movie[1],key])
                    else:
                        titles_dict[title] = [[movie[1],key]]
            for key in sorted(titles_dict.keys()):
                print(key, end = ':')
                print('')
                for title in titles_dict[key]:
                    print("\t"+str(title[0])+", "+str(title[1]))
                print('')
    else:
        break
