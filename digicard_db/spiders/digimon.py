import scrapy

from digicard_db.items import DigimonCardItem


class DigimonSpider(scrapy.Spider):
    name = "digimon"

    def start_requests(self):
        return [scrapy.Request('https://world.digimoncard.com/cardlist/?search=true&category=522001', callback=self.parse_list)]

    def parse_list(self, response):
        card_items = response.css(
            '.image_lists_item > .popup > .card_detail > .card_detail_inner')
        for card_item in card_items:
            yield(DigimonCardItem(
                name=card_item.css('.card_name::text').get(),
                number=card_item.css('.cardno::text').get(),
                rarity=card_item.css(
                    '.cardinfo_head > li:nth-child(2)::text').get(),
                cardType=card_item.css('.cardtype::text').get(),
                cardImage=card_item.css('.card_img > img::attr(src)').get(),
                form=card_item.css(
                    '.cardinfo_top_body > dl:nth-child(1) > dd:nth-child(2)::text').get(),
                attribute=card_item.css(
                    '.cardinfo_top_body > dl:nth-child(2) > dd:nth-child(2)::text').get(),
                digimonType=card_item.css(
                    '.cardinfo_top_body > dl:nth-child(3) > dd:nth-child(2)::text').get(),
                dp=card_item.css(
                    '.cardinfo_top_body > dl:nth-child(4) > dd:nth-child(2)::text').get(),
                playCost=card_item.css(
                    '.cardinfo_top_body > dl:nth-child(5) > dd:nth-child(2)::text').get(),
                digivolve1Cost=card_item.css(
                    '.cardinfo_top_body > dl:nth-child(6) > dd:nth-child(2)::text').get(),
                digivolve2Cost=card_item.css(
                    '.cardinfo_top_body > dl:nth-child(7) > dd:nth-child(2)::text').get(),
                effect=card_item.css(
                    '.cardinfo_bottom > dl:nth-child(1) > dd:nth-child(2)::text').get(),
                digivoluveEffect=card_item.css(
                    '.cardinfo_bottom > dl:nth-child(2) > dd:nth-child(2)::text').get(),
                securityEffect=card_item.css(
                    '.cardinfo_bottom > dl:nth-child(2) > dd:nth-child(2)::text').get(),
            ))
