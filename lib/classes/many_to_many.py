class Article:
    """Represents an article with an author and a magazine."""
    all_articles = []  # Store all articles to keep track of them

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        
        self._title = title  # Private variable to prevent mutation
        self.author = author
        self.magazine = magazine
        Article.all_articles.append(self)  # Add the article to the global list

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f"Article(title='{self.title}', author='{self.author.name}', magazine='{self.magazine.name}')"


class Author:
    """Represents an author in the system."""

    def __init__(self, name):
        self._name = name  # Private variable to prevent mutation

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return all articles written by the author."""
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        """Return all magazines the author has written for."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """Add an article to the author's portfolio."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return the list of categories of magazines the author writes for."""
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    """Represents a magazine in the system."""

    def __init__(self, name, category):
        self._name = name  # Private variable to prevent mutation
        self._category = category  # Private variable to prevent mutation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        """Return all articles published in this magazine."""
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        """Return a list of authors who have contributed to the magazine."""
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        """Return a list of all article titles in the magazine."""
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        """Return a list of authors who have contributed to this magazine, sorted alphabetically."""
        authors = self.contributors()
        return sorted(authors, key=lambda author: author.name) if authors else None
