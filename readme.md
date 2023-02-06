# Django scrapper

This is an very basic online app that scrapes rental properties from www.rent.com.au

In can be seen at [https://property-scraffer.herokuapp.com/](https://property-scraffer.herokuapp.com/)

It uses Beautiful Soup as a scrapping engine, and it's deployed in Django 4.


## Next steps:
- Let the user specify the postal code and self trigger the scrape instead of doing it automatically
- Let the user sort the results
- Let the user write notes on each rental, and remove it or star it
- Let the user know when the last scrape was

Also:
- Add a relational database (PosgreSQL?)
- Manage the images better (maybe scrape them all?)
- Scrape from another site (legally) and let the user search for both or each

And, **VERY IMPORTANT**
Improve it's styling (maybe use a color palette)


### Disclaimer
**The data scrapped is for personal, non-commercial use.**

Below is the rent.com.au robots.txt file content:
- User-agent: *
- Sitemap: https://www.rent.com.au/sitemaps/sitemap.xml.gz
- Sitemap: https://www.rent.com.au/blog/sitemap_index.xml
- Sitemap: https://www.rent.com.au/agents/blog/sitemap_index.xml
- Disallow: /share
- Disallow: /acreage_semi_rurals


