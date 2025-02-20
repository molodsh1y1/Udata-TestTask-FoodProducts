import scrapy

from mcdonalds_scraper.items import McDonaldMenuItem


class McdonaldSpider(scrapy.Spider):
    name = "mcdonald"
    allowed_domains = ["www.mcdonalds.com"]
    start_urls = ["https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"]

    def parse(self, response):
        product_ids = response.css(
            "li.cmp-category__item::attr(data-product-id)"
        ).getall()

        base_url = "https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item="

        for product_id in product_ids:
            product_url = base_url + product_id
            yield scrapy.Request(product_url, callback=self.parse_product)

    def get_nutrient_value(self, product_data: dict, nutrient_name: str):
        nutrient_list = product_data.get("nutrient_facts").get("nutrient")

        return next(
            item["value"] for item in nutrient_list if item["name"] == nutrient_name
        )

    def parse_product(self, response):
        product_data = response.json().get("item")

        name = product_data.get("item_name")
        description = product_data.get("description")
        calories = self.get_nutrient_value(product_data, "Калорійність")
        fats = self.get_nutrient_value(product_data, "Жири")
        carbs = self.get_nutrient_value(product_data, "Вуглеводи")
        proteins = self.get_nutrient_value(product_data, "Білки")
        unsaturated_fats = self.get_nutrient_value(product_data, "НЖК")
        sugar = self.get_nutrient_value(product_data, "Цукор")
        salt = self.get_nutrient_value(product_data, "Сіль")
        portion = self.get_nutrient_value(product_data, "Вага порції")

        yield McDonaldMenuItem(
            name=name,
            description=description,
            calories=calories,
            fats=fats,
            carbs=carbs,
            proteins=proteins,
            unsaturated_fats=unsaturated_fats,
            sugar=sugar,
            salt=salt,
            portion=portion,
        )
