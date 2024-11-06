// randomArticle.js

const articles = [
  {
    author: 'Smith, J.',
    title: 'The Impact of Climate Change',
    publisher: 'Journal of Environmental Studies',
    year: 2020,
  },
  {
    author: 'Doe, A.',
    title: 'Advances in Machine Learning',
    publisher: 'AI Journal',
    year: 2019,
  },
  {
    author: 'Brown, L.',
    title: 'Quantum Computing Explained',
    publisher: 'Physics Today',
    year: 2021,
  },
  {
    author: 'Johnson, M.',
    title: 'Renewable Energy Sources',
    publisher: 'Energy Today',
    year: 2018,
  },
  {
    author: 'Williams, S.',
    title: 'Cybersecurity Trends',
    publisher: 'Tech Journal',
    year: 2022,
  },
  {
    author: 'Nguyen, T.',
    title: 'Deep Learning Techniques for Image Recognition',
    publisher: 'Journal of Machine Learning Research',
    year: 2021,
  },
  {
    author: 'Garcia, M.',
    title: 'Reinforcement Learning in Autonomous Systems',
    publisher: 'AI & Robotics Journal',
    year: 2022,
  },
  {
    author: 'Lee, K.',
    title: 'Natural Language Processing Advances',
    publisher: 'Computational Linguistics Today',
    year: 2020,
  },
  {
    author: 'Martinez, R.',
    title: 'Transfer Learning Applications',
    publisher: 'International Journal of AI',
    year: 2019,
  },
  {
    author: 'OConnor, P.',
    title: 'Explainable AI and Model Interpretability',
    publisher: 'Artificial Intelligence Review',
    year: 2023,
  }
];

function random_article_apa() {
  const article = articles[Math.floor(Math.random() * articles.length)];
  return `${article.author} (${article.year}). ${article.title}. ${article.publisher}.`;
}

function random_article_obj() {
  const article = articles[Math.floor(Math.random() * articles.length)];
  return {
    author: article.author,
    title: article.title,
    publisher: article.publisher,
    year: article.year,
  };
}