This project includes scraping imdb site going three levels deep. My spider gathers data from different levels by following links and finally outputing the data into a comma delimited JSON file which is ready to beconverted to another file type or loaded into a data analysis tool such as Python's Numpy or Excel.

This project starts at the top 250 rated shows page (http://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_3) and iterates through the 250 links while following links on subsequent pages until it gets to the full cast page (such as : http://www.imdb.com/title/tt0903747/fullcredits?ref_=tt_cl_sm#cast) where it iterates again, through all the cast members and finally saves all data to a JSON file. 

Full JSON file can be found at:
https://github.com/lbrian357/imdb_top_tv_actors_scraper/blob/master/top_tv_actors/tv_actors.json

Sample of data gathered: 
{"name": "Neil deGrasse Tyson", "show": "Cosmos: A Spacetime Odyssey", "show_year": "(2014)", "episodes": "13 episodes", "imdb_rating": "9.3", "actor_year": "2014"},
{"name": "David Attenborough", "show": "Life", "show_year": "(2009)", "episodes": "10 episodes", "imdb_rating": "9.1", "actor_year": "2009"},
{"name": "David Attenborough", "show": "Planet Earth", "show_year": "(2006)", "episodes": "11 episodes", "imdb_rating": "9.5", "actor_year": "2006"},
{"name": "Bryan Cranston", "show": "Breaking Bad", "show_year": "(2008)", "episodes": "62 episodes", "imdb_rating": "9.4", "actor_year": "2008-2013"},
