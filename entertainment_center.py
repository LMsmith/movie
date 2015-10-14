import fresh_tomatoes
import media

# define instances of the Movie class
sleepwalk_with_me = media.Movie("Sleepwalk With Me", "A comedy for anyone who ever had a drea"
                                "m. And then jumped out a window", "http://ia.media-imdb.com/images/M/MV5B"
                                "MTM3MDUzMDQwNF5BMl5BanBnXkFtZTcwMDk1NjM4OA@@._V1_SX214_A"
                                "L_.jpg", "https://www.youtube.com/watch?v=iYw3OtjhK0E", "2012", "Mike Birbigl"
                                "ia, Lauren Ambrose, James Rebhorn", "A burgeoning stand-up comedian struggl"
                                "es with the stress of a stalled career, a stale relationship, and the wild spurts of "
                                "severe sleepwalking he is desperate to ignore.")
the_dark_knight_rises = media.Movie("The Dark Knight Rises", "Rise", "http://ia.media-imdb.com/ima"
                                    "ges/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@."
                                    "_V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=GokKUqLcvD8",
                                    "2012", "Christian Bale, Tom Hardy, Anne Hathaway", "Eight years after the Jo"
                                    "ker's reign of anarchy, the Dark Knight is forced to return from his imposed exi"
                                    "le to save Gotham City from the brutal guerrilla terrorist Bane with the help of "
                                    "the enigmatic Catwoman.")
silver_linings_playbook = media.Movie("Silver Linings Playbook", "Watch for the signs", "http://ia.med"
                                      "ia-imdb.com/images/M/MV5BMTM2MTI5NzA3MF5BMl5BanBnXkFtZTcwOD"
                                      "ExNTc0OA@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v="
                                      "Lj5_FhLaaQQ", "2012", "Bradley Cooper, Jennifer Lawrence, Robert De Nir"
                                      "o", "After a stint in a mental institution, former teacher Pat Solitano moves ba"
                                      "ck in with his parents and tries to reconcile with his ex-wife. Things get more"
                                      "challenging when Pat meets Tiffany, a mysterious girl with problems of her o"
                                      "wn.")
fight_club = media.Movie("Fight Club", "When you wake up in a different place at a different time, can"
                         "you wake up as a different person?", "http://ia.media-imdb.com/images/M/MV5BMjIw"
                         "NTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_SX214_AL_.jpg", "http"
                         "s://www.youtube.com/watch?v=SUXWAEX2jlg", "1999", "Brad Pitt, Edward Norton, "
                         "Helena Bonham Carter", "An insomniac office worker, looking for a way to change "
                         "his life, crosses paths with a devil-may-care soap maker, forming an underground fig"
                         "ht club that evolves into something much, much more...")
usual_suspects = media.Movie("The Usual Suspects", "The truth is always in the last place you look",
                             "http://ia.media-imdb.com/images/M/MV5BMzI1MjI5MDQyOV5BMl5BanBnXkFtZTc"
                             "wNzE4Mjg3NA@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=9"
                             "MjV4EwR7Mg", "1995", "Kevin Spacey, Gabriel Byrne, Chazz Palminteri", "A sole "
                             "survivor tells of the twisty events leading up to a horrific gun battle on a boat, which"
                             "begin when five criminals meet at a seemingly random police lineup.")
short_term_12 = media.Movie("Short Term 12", "The lock is broken, but everything else works", "http:"
                            "//ia.media-imdb.com/images/M/MV5BMTEwNjE2OTM4NDZeQTJeQWpwZ15BbW"
                            "U3MDE2MTE4OTk@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=2"
                            "g0Z7oWMjfo", "2013", "Brie Larson, John Gallagher, Jr., Rami Malek", "A 20-some"
                            "thing supervising staff member of a residential treatment facility navigates the troub"
                            "led waters of that world alongside her co-worker and longtime boyfriend.")

# put movies into an array
movies = [sleepwalk_with_me, the_dark_knight_rises, silver_linings_playbook, fight_club,
          usual_suspects, short_term_12]

# open the fresh_tomatoes movies pages
fresh_tomatoes.open_movies_page(movies)
