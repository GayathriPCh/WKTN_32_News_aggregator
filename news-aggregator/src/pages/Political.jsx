import { useState, useEffect } from 'react';
import NewsCard from '../components/NewsCard';
import newsData from '../data/categorized_news_output.json';

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
    <div>
      <h1>Political</h1>
      {news.filter(item => item.category === 'Political').map((item, index) => (
        <NewsCard key={index} news={item} />
      ))}
    </div>
  );
}

export default Political;
