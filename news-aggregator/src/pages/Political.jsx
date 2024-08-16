import  { useState, useEffect } from 'react';
import NewsCard from '../components/NewsCard';
import newsData from '../data/categorized_news_output.json';
import './Political.css';

function Political() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    const allNews = [
      ...newsData.common_news,
      ...newsData.ap_news,
      ...newsData.bbc_news
    ];
    setNews(allNews);
  }, []);

  return (
    <div className="page-background">

    <div>
    <div className="news-container">
      {news.filter(item => item.category === 'Political').map((item, index) => (
        <NewsCard key={index} news={item} />
      ))}
    </div>
    </div>
    </div>
  );
}

export default Political;
