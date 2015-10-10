import fresh_tomatoes
import media

sleepwalk_with_me = media.Movie("Sleepwalk With Me", "A comedy for anyone who ever had a dream. And then jumped out a window", "http://ia.media-imdb.com/images/M/MV5BMTM3MDUzMDQwNF5BMl5BanBnXkFtZTcwMDk1NjM4OA@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=iYw3OtjhK0E")
the_dark_knight_rises = media.Movie("The Dark Knight Rises", "Rise", "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=GokKUqLcvD8")
silver_linings_playbook = media.Movie("Silver Linings Playbook", "Watch for the signs", "http://ia.media-imdb.com/images/M/MV5BMTM2MTI5NzA3MF5BMl5BanBnXkFtZTcwODExNTc0OA@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=Lj5_FhLaaQQ")
fight_club = media.Movie("Fight Club", "When you wake up in a different place at a different time, can you wake up as a different person?", "http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=SUXWAEX2jlg")
usual_suspects = media.Movie("The Usual Suspects", "The truth is always in the last place you look", "http://ia.media-imdb.com/images/M/MV5BMzI1MjI5MDQyOV5BMl5BanBnXkFtZTcwNzE4Mjg3NA@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=9MjV4EwR7Mg")
short_term_12 = media.Movie("Short Term 12", "The lock is broken, but everything else works", "http://ia.media-imdb.com/images/M/MV5BMTEwNjE2OTM4NDZeQTJeQWpwZ15BbWU3MDE2MTE4OTk@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=2g0Z7oWMjfo")
role_models = media.Movie("Role Models", "I am not a ROLE MODEL", "http://ia.media-imdb.com/images/M/MV5BMTg3MTk4NzQ0NV5BMl5BanBnXkFtZTcwNjM0OTc5MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=yZGYswlbU8w")
million_dollar_hotel = media.Movie("The Million Dollar Hotel", "Everyone has something to hide", "http://ia.media-imdb.com/images/M/MV5BMzA5NTIwNzUxM15BMl5BanBnXkFtZTcwMTUyNjYyMQ@@._V1_SY317_CR11,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=S4Ft6C8LTKU")
best_in_show = media.Movie("Best in Show", "Some pets deserve a little more respect than others", "http://ia.media-imdb.com/images/M/MV5BMTQ5OTc0NDU1MF5BMl5BanBnXkFtZTYwNzk1OTI3._V1_SY317_CR0,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=yeifMjqpsg0")

movies = [sleepwalk_with_me, the_dark_knight_rises, silver_linings_playbook, fight_club, usual_suspects, short_term_12, role_models, million_dollar_hotel, best_in_show]
fresh_tomatoes.open_movies_page(movies)

