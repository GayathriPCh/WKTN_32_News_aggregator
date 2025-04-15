# News Aggregator

**News Aggregator** is a web scraping application that collects and aggregates news from various sources. The app utilizes **React** for the frontend, **Groq AI API** for AI-powered news summarization, and custom scripts to scrape data from news sites. It organizes the scraped data into categories and presents it in a user-friendly format.
![image](https://github.com/user-attachments/assets/f708bd0f-e1a6-43c9-9672-42aa95e65e21)

## Features

- **Web Scraping**: Scrapes news articles from various sources such as BBC and AP News.
- **AI Summarization**: Uses Groq AI API to summarize long news articles into shorter, digestible content.
- **News Categorization**: Classifies news articles into categories for better readability.
- **Frontend**: Built with React, displaying the aggregated and summarized news articles.

## Folder Structure

```
/news-aggregator
│
├── /backend/                # Contains scripts for web scraping and news categorization
│   ├── categorized_news.py  # Python script for categorizing news
│   ├── categorized_news_output.json  # Categorized news output in JSON format
│   ├── categorized_news_output.txt   # Categorized news output in text format
│   └── scraper/             # Web scraping scripts to fetch news articles
│
├── /node_modules/           # Node.js modules (installed by npm)
│
├── /frontend/               # Frontend components built with React
│   ├── /src/
│   │   ├── App.js           # Main React app component
│   │   ├── NewsCard.js      # Component to display individual news articles
│   │   ├── CategoryFilter.js# Component to filter news by category
│   │   └── ...
│   ├── package.json         # NPM package descriptor for the frontend
│
├── .gitignore               # Git ignore file to exclude node_modules, logs, etc.
├── package-lock.json        # Dependency lock file
├── package.json             # Root package descriptor for both frontend and backend
├── ap_news.json             # News data scraped from AP News
└── bbc_news.json            # News data scraped from BBC News
```

## Installation

### Prerequisites
- **Node.js**: Ensure that you have Node.js installed on your system. You can download it from [here](https://nodejs.org/).
- **Python**: Make sure Python is installed on your system for running the backend scripts.
- **Groq AI API Key**: You will need an API key for Groq AI to enable summarization of the articles.

### Setting up Backend

1. Navigate to the `/backend` folder:
   ```bash
   cd backend
   ```

2. Install necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the web scraping scripts:
   ```bash
   python scraper/scrape_news.py
   ```

   This will scrape news articles from sources like AP News and BBC, and store them in `ap_news.json` and `bbc_news.json`.

4. Categorize the news articles using the categorization script:
   ```bash
   python categorized_news.py
   ```

   The categorized output will be stored in `categorized_news_output.json` and `categorized_news_output.txt`.

### Setting up Frontend

1. Navigate to the `/frontend` folder:
   ```bash
   cd frontend
   ```

2. Install the frontend dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

   This will run the frontend application on your local server. The news data, scraped and categorized by the backend, will be displayed in the frontend.

## API Integration

The Groq AI API is used for summarizing the news articles. You need to set up the API key in your `.env` file:

1. Create a `.env` file in the root of the project.

2. Add your API key:
   ```env
   GROQ_API_KEY=your-groq-api-key-here
   ```
