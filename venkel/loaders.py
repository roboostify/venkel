"""Venkel scraper item loaders."""
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose


class ProductLoader(ItemLoader):
    """Product item loader for VenkelItem."""
    url_in = MapCompose()
    url_out = Join()

    site_name_in = MapCompose()
    site_name_out = Join()

    mfg_part_id_in = MapCompose()
    mfg_part_id_out = Join()

    qty_list_in = MapCompose()
    qty_list_out = MapCompose()
