'''=============================================================='''
''' Generate dictionaries and lists to store data of parsed files'''
'''=============================================================='''


''' Populates genre dictionary after parsing file genre.data'''
def generate_genreDict(genre_file_name):
    with open(genre_file_name,"r") as genre_file:
        for line in genre_file:
            line = line.rstrip('\n')
            temp = line.split('|')
            genreDict[temp[1]] = temp[0]
    #print genreDict
    genre_file.closed

''' Populates movie dictionary after parsing file movie.data'''
def generate_movieDict(movie_file_name):
    with open(movie_file_name,"r") as movie_file:
        for line in movie_file:
            movie_info={}
            line = line.rstrip('\n')
            line = line.replace("||", '|')
            temp = line.split('|')
            movie_info['movieId'] = temp[0]
            movie_info['movieName'] = temp[1]
            movie_info['movieReleasedOn'] = temp[2]
            movie_info['movieUrl'] = temp[3]
            movie_info['movieGenre'] = []
            for i in range(4, 22):
                if(temp[i] == '1'):
                    j = i-4
                    movie_info['movieGenre'].append(genreDict.get(str(j)))
            movie_info['countOfMovieRatings'] = 0
            movie_info['sumOfMovieRatings'] = 0
            movie_info['averageOfMovieRatings'] = 0
            movieDict[temp[0]] = movie_info
    #print movieDict
    movie_file.closed

''' Populates user dictionary after parsing file user.data'''
def generate_userDict(user_file_name):
    with open(user_file_name,"r") as user_file:
        for line in user_file:
            user_info={}
            line = line.rstrip('\n')
            temp = line.split('|')
            user_info['userId'] = temp[0]
            user_info['userAge'] = int(temp[1])
            user_info['userGender'] = temp[2]
            user_info['userOccupation'] = temp[3]
            user_info['userPincode'] = temp[4]
            user_info['countOfUserRatings'] = 0
            userDict[temp[0]] = user_info
    #print userDict
    user_file.closed

''' Populates ratings list after parsing file ratings.data'''
def generate_ratingsDict(ratings_file_name):
    with open(ratings_file_name,"r") as ratings_file:
        for line in ratings_file:
            ratings_info={}
            line = line.rstrip('\n')
            line = line.replace("\t", ' ')
            temp = line.split(' ')
            ratings_info['ratingUserId'] = temp[0]
            ratings_info['ratingMovieId'] = temp[1]
            ratings_info['ratingScore'] = temp[2]
            ratings_info['ratingTimeStamp'] = temp[3]
            ratingsList.append(ratings_info)
    #print ratingsList
    ratings_file.closed


'''========================================================='''
''' Business Logics for use cases are implemented below this'''
'''========================================================='''

def updateMovieRatings():
    for aRating in ratingsList:
        movie_info = movieDict.get(aRating['ratingMovieId'])
        movie_info['countOfMovieRatings'] = movie_info['countOfMovieRatings'] + 1
        movie_info['sumOfMovieRatings'] = aRating['ratingScore'] + movie_info['sumOfMovieRatings']
        # print movie['totalRating']
    for movie in movieDict.keys():
            movieDict.get(movie)["averageOfMovieRatings"]=movieDict.get(movie)["sumOfMovieRatings"] / movieDict.get(movie)["countOfMovieRatings"]


def updateUserRatingsCount():
    for aRating in ratingsList:
        user = userDict.get(aRating['ratingUserId'])
        user['countOfUserRatings']=user['countOfUserRatings'] + 1


def mostActiveUser(userDict):
    maxItem = max(item['countOfUserRatings'] for item in userDict.values())
    for users in userDict.values():
        if(users['countOfUserRatings']==maxItem):
            print "Most Active User"
            print users['userId']

def MostWatchedMovie(movieDict):
    maxItem = max(item['countOfMovieRatings'] for item in movieDict.values())
    for movies in movieDict.values():
        if(movies['countOfMovieRatings']==maxItem):
            print "\nMost watched Movie"
            print movies['movieName']

'''
def highestRatedMovieByGenre(movieDict):
    for aRating in ratingsList:
        movie_info = movieDict.get(aRating['ratingMovieId'])
    for movies in movieDict.keys():
        movieDict.get(movies)["averageOfMovieRatings"]=movieDict.get(movies)["sumOfMovieRatings"] / movieDict.get(movies)["countOfMovieRatings"]
'''

''' Main function '''
genreDict={}
movieDict={}
userDict={}
ratingsList=[]

generate_genreDict("genre.data")
generate_movieDict("movie.data")
generate_userDict("user.data")
generate_ratingsDict("ratings.data")

updateMovieRatings()
updateUserRatingsCount()

mostActiveUser(userDict)
MostWatchedMovie(movieDict)



