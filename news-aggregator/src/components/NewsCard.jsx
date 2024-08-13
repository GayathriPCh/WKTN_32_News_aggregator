import PropTypes from 'prop-types';

function NewsCard({ news }) {
  return (
    <div className="news-card">
      <h2>{news.headline || news.title}</h2>
      {news.image && <img src={news.image} alt={news.headline || news.title} />}
      <p>{news.description}</p>
      <a href={news.link} target="_blank" rel="noopener noreferrer">Read more</a>
    </div>
  );
}

NewsCard.propTypes = {
  news: PropTypes.shape({
    headline: PropTypes.string,
    title: PropTypes.string,
    link: PropTypes.string.isRequired,
    description: PropTypes.string,
    image: PropTypes.string,
    category: PropTypes.string
  }).isRequired
};

export default NewsCard;
