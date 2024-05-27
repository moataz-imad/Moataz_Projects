# Flight Ticket Price Web Scraper

Welcome to the Flight Ticket Price Web Scraper project! This project utilizes Selenium to scrape flight ticket prices for the next few months from various airline websites. Unlike other similar tools like Skyscanner, this scraper provides precise prices without relying on estimations.

## Table of Contents

- [Flight Ticket Price Web Scraper](#flight-ticket-price-web-scraper)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Usage](#usage)
  - [Challenges and Solutions](#challenges-and-solutions)
  - [Future Improvements](#future-improvements)

## Introduction

Planning a trip can be daunting, especially when it comes to finding the best deals on flight tickets. This project aims to simplify the process by providing a custom web scraper that fetches real-time flight ticket prices for the next few months directly from airline websites. By using Selenium, the scraper ensures precise and accurate price data, eliminating the need for estimations.

## Features

- **Custom Web Scraper:** Developed using Selenium, the scraper fetches flight ticket prices from airline websites.
- **Real-Time Data:** Provides up-to-date prices for flights in the upcoming months.
- **Precise Pricing:** Unlike other tools, the scraper fetches precise prices without relying on estimations.
- **Manual Captcha Solver:** Handles captcha challenges manually to ensure smooth operation.

## Usage

To use the Flight Ticket Price Web Scraper:
1. Install the necessary dependencies, including Selenium.
2. Configure the scraper to target the desired airline websites and specify the travel dates.
3. Run the scraper script.
4. Review the fetched data to plan your trip based on the cheapest available prices.

## Challenges and Solutions

One of the main challenges encountered during the development of this project was dealing with captchas presented by some airline websites. While a budget-friendly solution for automating captcha solving was not found, the scraper continued to operate smoothly by solving captchas manually.

## Future Improvements

In the future, the project could be enhanced by implementing a more efficient captcha-solving mechanism, potentially utilizing third-party services or machine learning algorithms. Additionally, the scraper could be extended to support more airline websites and offer additional features such as fare prediction based on historical data.

