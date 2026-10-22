# GPU Price Tracker

Collecting and forecasting graphics card prices in the Greek market.

> Status: work in progress

## Goal

GPU prices change over time, driven by many different market factors.
This project collects current prices once a day, builds its own price
history, and explores which factors actually affect prices and how.

## Roadmap

- [x] 1. Environment setup
- [ ] 2. Price collection script
- [ ] 3. Daily automated collection with GitHub Actions
- [ ] 4. "Fair price" model from specs (regression)
- [ ] 5. Price forecasting with external factors
- [ ] 6. Streamlit dashboard

## Responsible data collection

- robots.txt is respected
- Only public category pages with current prices are used
- No price history pages and no API endpoints
- Few requests, with a delay between them, once per day
- If a CAPTCHA or block appears, collection stops

## Project structure

- `data/raw/` - daily price snapshots, as collected
- `data/processed/` - cleaned data, ready for analysis
- `notebooks/` - exploration and experiments
- `src/` - project source code
- `tests/` - automated tests

## Data source

Prices are collected from the public graphics cards category page of [Plaisio](https://www.plaisio.gr/list/anavathmisi-diktia/anavathmisi-pc/kartes-grafikon), a Greek electronics retailer.

### What is collected

Each run saves one CSV file to `data/raw/`, named after the collection date (e.g. `2026-10-21.csv`), with these columns:

- `id`: the product ID used by the site
- `name`: the product name as listed
- `price`: the listed price in euros
- `date`: the collection date

The raw files are kept exactly as collected. Cleaning and filtering happen in later steps.

### How it is collected

The scraper follows the site's `robots.txt` and only reads the category listing pages with current prices. It does not access price history pages or APIs.

- Requests are few (one per listing page) with a 2-second delay between them.
- Every request identifies the project through its User-Agent.
- If the site returns an error or blocks the request, the scraper stops. It never tries to bypass blocks or CAPTCHAs.
- Collection runs once a day on a local Windows machine, using Windows Task Scheduler and the `run_daily.ps1` script..


GitHub Actions was tested first, but the site returns `403 Forbidden` to GitHub's servers. Since the project does not bypass blocks, collection runs locally instead.

### Disclaimer

This is a personal learning project and is not affiliated with Plaisio. Prices are snapshots of what was listed on each collection date and may differ from current prices.