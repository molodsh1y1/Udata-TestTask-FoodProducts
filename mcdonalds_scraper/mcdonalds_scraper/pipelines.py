# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class McdonaldScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get("name"):
            adapter["name"] = self.clean_string(adapter["name"])

        if not adapter.get("description"):
            adapter["description"] = None

        numeric_fields = [
            "calories",
            "fats",
            "carbs",
            "proteins",
            "unsaturated_fats",
            "sugar",
            "salt",
            "portion",
        ]

        for field in numeric_fields:
            try:
                if field in ["calories", "portion"]:
                    adapter[field] = int(adapter[field])
                else:
                    adapter[field] = float(adapter[field])
            except (ValueError, TypeError):
                adapter[field] = None

        return item

    def clean_string(self, text: str):
        text = re.sub(r'\\"', "'", text)
        text = re.sub(r'(?<!\\)"', "'", text)
        text = re.sub(r'®', '', text)

        return text
