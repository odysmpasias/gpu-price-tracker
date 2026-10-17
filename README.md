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