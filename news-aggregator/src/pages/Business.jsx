import { useState, useEffect } from 'react';
import NewsCard from '../components/NewsCard';
import newsData from '../data/categorized_news_output.json';

function Business() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    setNews(newsData.common_news.concat(newsData.ap_news, newsData.bbc_news));
  }, []);

  return (
    <div>
      <h1>Business</h1>
      {news.filter(item => item.category === 'Business').map((item, index) => (
        <NewsCard key={index} news={item} />
      ))}
    </div>
  );
}

export default Business;
