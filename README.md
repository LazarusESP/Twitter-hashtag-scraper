# Twitter-hashtag-scraper
The program is written in Python and uses the Tweepy library to authenticate with the Twitter API and retrieve the top trends for a specific location. The program then filters the trends to include only hashtags, and selects the top 10 hashtags based on their popularity.

The program then creates a new text file named top_hashtags.txt and writes the top 10 hashtags to the file in a numbered list format. Each hashtag is written on a separate line, with the format <number>: <hashtag>.

After writing the hashtags to the file, the program prints a message indicating that the hashtags have been exported to the file.

The program can be modified to scrape popular hashtags for different locations or time periods by changing the parameters passed to the trends_place() function.
