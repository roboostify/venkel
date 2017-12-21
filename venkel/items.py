"""Venkel item definitions."""
# -*- coding: utf-8 -*-
import scrapy


class VenkelItem(scrapy.Item):
    """Venkel product price definition."""
    url = scrapy.Field()
    site_name = scrapy.Field()
    mfg_part_id = scrapy.Field()
    qty_list = scrapy.Field()
