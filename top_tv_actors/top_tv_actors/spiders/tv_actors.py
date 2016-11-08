import scrapy

class Actor(scrapy.Item):
    name = scrapy.Field()
    episodes = scrapy.Field()
    actor_year = scrapy.Field()
    show = scrapy.Field()
    show_year = scrapy.Field()
    imdb_rating = scrapy.Field()

class TvActors(scrapy.Spider):
    name = "tv_actors"
    start_urls = [
        'http://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_3',
    ]

    def parse(self, response):
        for show_list in response.css('tbody.lister-list tr'):
            actor = Actor()
            actor['show'] = show_list.css('td.titleColumn a::text').extract_first()
            actor['show_year'] = show_list.css('td.titleColumn span.secondaryInfo::text').extract_first()
            actor['imdb_rating'] = show_list.css('td.ratingColumn.imdbRating strong::text').extract_first()

            #navigate to show_page
            show_page = show_list.css('td.titleColumn a::attr(href)').extract_first()
                
            request = scrapy.Request(response.urljoin(show_page), callback=self.parse_show_page)
            request.meta['actor'] = actor
            yield request

    def parse_show_page(self, response):
        actor = response.meta['actor']
        cast_page = response.css('div#titleCast.article div.see-more a::attr(href)').extract_first()

        yield scrapy.Request(response.urljoin(cast_page), callback=self.parse_cast_page, meta={'actor': actor}) 

    def parse_cast_page(self, response):
        actor = response.meta['actor']
        for full_cast in response.css('table.cast_list'):
            actor['name'] =  full_cast.css('span.itemprop::text').extract_first()
            actor['episodes'] = full_cast.css('td.character div').re(r'\((\d.*)[,]')[0]
            actor['actor_year'] = full_cast.css('td.character div').re(r'[,]\s(.*\d.*)\)')[0]
            yield actor

































"""

    def parse(self, response):
        for show in response.css('tbody.lister-list tr'):
            first_page_yield = {
                'show': show.css('td.titleColumn a::text').extract_first(),
                'show_year': show.css('td.titleColumn span.secondaryInfo::text').extract_first(),
                'imdb_rating': show.css('td.ratingColumn.imdbRating strong::text').extract_first(),
            }

        show_page = show.css('td.titleColumn a::attr(href)').extract_first()
            
        request = scrapy.Request(show_page, callback=self.parse_show_page)
        request.meta['item'] = Item()
        yield request

    def parse_show_page(self, response):
        item = response.meta['item']
        cast_page = response.css('div.see-more a::attr(href)').extract_first()
        yield scrapy.Request(cast_page, callback=self.parse_cast_page, meta={'item': item}) 
        

    def parse_cast_page(self, response):
        item = response.meta['item']
        for cast in response.css('table.cast_list'):
            casts = {
                    'name': cast.css('span.itemprop::text').extract_first(),
                    'episodes': cast.css('td.character div').re(r'\((\d.*)[,]')[0]
                    'actor_year': cast.css('td.character div').re(r'[,]\s(.*\d.*)\)')[0]
            }
            casts.update(item)
            yield item
"""

