import { useState, useEffect } from 'react';
import NewsCard from '../components/NewsCard';
import newsData from '../data/categorized_news_output.json';
import './Business.css'; // Import the CSS file for the Business page

function Business() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    setNews(newsData.common_news.concat(newsData.ap_news, newsData.bbc_news));
  }, []);

  return (
    <div className="business-page">
      <h1 className="page-title">Business</h1>
      <div className="news-container">
        {news.filter(item => item.category === 'Business').map((item, index) => (
          <NewsCard key={index} news={item} />
        ))}
      </div>
    </div>
  );
}

export default Business;
