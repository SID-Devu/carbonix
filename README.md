# Carbonix — AI-Verified Carbon Credit Marketplace

A full-stack web application for buying, selling, and verifying carbon credits using AI satellite verification.

## Features

- **Dashboard** — Real-time market stats, price trend charts, credit distribution, and recent transactions
- **Project Explorer** — Browse 8 carbon offset projects with AI quality ratings (AAA–B), satellite verification status, and filtering
- **Project Detail** — Full AI verification report, credit supply breakdown, NDVI analysis, and risk assessment
- **Marketplace** — Buy credits with real-time pricing, sortable tables, and order confirmation
- **Portfolio** — Track holdings, P&L, allocation, quality distribution, and environmental impact
- **REST API** — JSON endpoints for prices, projects, transactions, and market stats

## Tech Stack

- **Backend**: Python / Flask
- **Frontend**: Tailwind CSS (CDN), Chart.js
- **Templates**: Jinja2
- **Data**: Rich mock data modeling 8 real-world project types across 6 countries

## Quick Start

```bash
cd carbonix
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /api/prices` | 365-day price history by project type |
| `GET /api/projects` | All project data with satellite verification |
| `GET /api/transactions` | Recent marketplace transactions |
| `GET /api/stats` | Market summary statistics |

## Project Structure

```
carbonix/
├── app.py              # Flask routes and API
├── data.py             # Mock data models
├── requirements.txt    # Dependencies
├── templates/
│   ├── base.html           # Layout with sidebar
│   ├── dashboard.html      # Dashboard with charts
│   ├── projects.html       # Project explorer grid
│   ├── project_detail.html # AI verification detail
│   ├── marketplace.html    # Buy/sell marketplace
│   └── portfolio.html      # Portfolio manager
└── static/             # Static assets
```

## License

MIT
