# YC Companies Scraper

Downloads YC companies by using the Algolia API that powers https://www.ycombinator.com/companies, and processes them into a more structured format.

## Usage

Either use output dataset at `data/companies.json`, or retrieve the latest results by executing

```python src/main.py --start_year 2005 --end_year 2023```

## Todo

This repo is a WIP. For example, fields such as 'locations' and 'regions' should be consolidated into a single field.