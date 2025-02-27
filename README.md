# InformationRetrieval

**Advanced Database Systems - Project 1**

## Team Information

-   **Names:** Begum Cicekdag, Maxine Tamas
-   **UNIs:** bc2975, mt3634

## Submitted Files

-   `query_expansion.py` - Main Python script implementing query expansion
-   `rocchio.py` - Implementation of the Rocchio Algorithm
-   `requirements.txt` - List of required Python libraries
-   `README.md` - This documentation file
-   `proj1-stop.txt` - List of all of our stop words

### API Credentials

-   **Google Custom Search API Key:** 
```AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk```
-   **Google Custom Search Engine ID:** 
```c66d0519df77f44f1```

### Setup Instructions:

1.  **Connect to Google Cloud VM:**

    ```
    ssh your-username@your-vm-ip
    ```

2.  **Install Required Software:**

    ```
    sudo apt update
    sudo apt install python3-pip
    ```

3.  **Clone the Repository:**

    ```
    git clone https://github.com/maxinetamas/InformationRetrieval.git
    cd InformationRetrieval
    ```

4.  **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

5.  **Run the Program:**

    To run the program, you need to use the Google Custom Search API key and Google Custom Search Engine ID above, as well as provide the desired precision, and the query you want to run.

   The format would be something like:

    python3 query_expansion.py YOUR_GOOGLE_API_KEY YOUR_GOOGLE_ENGINE_ID PRECISION "your search query"

   And an example would look like:

    python3 query_expansion.py AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk c66d0519df77f44f1 0.8 "machine learning"

## Internal Design

The project consists of the following main components:

-   **Query Expansion Module:** Implements the Rocchio Algorithm for query refinement.
-   **Google Custom Search API Handler:** Handles search queries and fetches results using the Google Custom Search API.
-   **Relevance Feedback Processor:** Analyzes the search results and selects relevant keywords based on user feedback.
-   **Command-Line Interface:** Provides an interface for running queries and obtaining results.

### External Libraries Used

-   `requests` - For making API calls to Google Custom Search (Note: While `requests` is commonly used for making API calls, this project uses `google-api-python-client` to interact with the Google Custom Search API.)
-   `numpy` - For vector operations in the Rocchio Algorithm
-   `json` - For handling API responses and configurations
-   `argparse` - For parsing command-line arguments
-   `google-api-python-client` - Interacting with the Google Custom Search API
-   `scikit-learn` - Using `TfidfVectorizer` for calculating TF-IDF values.

### Query Modification Method

The core component of this project is the query expansion process using the Rocchio Algorithm, which follows these steps:

1.  **Initial Query Execution:**

    The original query is sent to the Google Custom Search API.
2.  **Relevance Feedback Collection:**

    The user marks each of the top-10 results as relevant (Y) or non-relevant (N) via the command line.
3.  **Vector-Based Query Adjustment:**

    The Rocchio Algorithm modifies the query vector by:

    -   Increasing weights of terms from relevant results
    -   Decreasing weights of terms from non-relevant results
4.  **Term Reordering and Expansion:**

    Our enhanced implementation:

    -   Reorders ALL terms (both original and new) based on their TF-IDF weights
    -   Places the most discriminative terms first in the query
    -   Adds up to 2 new high-weight terms not in the original query
5.  **Iterative Refinement:**

    Steps 1-4 are repeated until the target precision is reached or the precision no longer improves.

### Query Word Order Determination

Our implementation improves upon basic Rocchio by:

-   Computing weights for all terms (original query + potential new terms)
-   Sorting terms by their weight in descending order
-   Creating a new query that maintains this weight-based ordering

This approach leverages the fact that search engines often give more weight to terms that appear earlier in the query.

### Program Run Transcripts

Below is a sample transcript of the program's execution:

```
Parameters:
Client key = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
Engine key = c66d0519df77f44f1
Query = machine learning
Precision = 0.8
Google Search Results:

Result 1
URL: https://example.com/1
Title: Introduction to Machine Learning
Summary: Machine learning is a subfield of artificial intelligence...
Relevant (Y/N)? Y
[results continued...]
FEEDBACK SUMMARY
Query: machine learning
Precision: 0.6
Still below the desired precision of 0.8
Indexing results...
Indexing results...
Augmenting by deep neural
Parameters:
Client key = YOUR_GOOGLE_API_KEY
Engine key = YOUR_GOOGLE_ENGINE_ID
Query = deep neural machine learning
Precision = 0.8
[second iteration continues...]
...
...
...
Desired precision reached.
```

### Per Se Transcript

```
python query_exp.py AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk c66d0519df77f44f1 0.9 "per se"
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = per se
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://www.thomaskeller.com/perseny
         Title: Per Se | Thomas Keller Restaurant Group
         Summary: Per Se. Per Se Front Door. center. Michelin; Les Grandes; Relias. About. About; Restaurant · Team · Info & Directions · Gift Experiences · Reservations; Menus & ...
        ]
Relevant (Y/N)?y
Result 2
        [
         URL: https://www.merriam-webster.com/dictionary/perse
         Title: PERSE Definition & Meaning - Merriam-Webster
         Summary: The meaning of PERSE is of a dark grayish blue resembling indigo. How to use perse in a sentence. Did you know?
        ]
Relevant (Y/N)?n
Result 3
        [
         URL: https://www.thomaskeller.com/new-york-new-york/per-se/todays-menus
         Title: Today's Menus | Thomas Keller Restaurant Group
         Summary: Per Se. Daily Menus. Two tasting menus are offered daily: a nine-course chef's tasting menu, as well as a ... Per Se . Complete your gift to make an impact.
        ]
Relevant (Y/N)?y
Result 4
        [
         URL: https://www.reddit.com/r/grammar/comments/otxmm7/how_does_one_use_per_se/
         Title: How does one use 'per se'? : r/grammar
         Summary: Jul 29, 2021 ... Comments Section ... It roughly means "by itself”, “in itself” or “of itself” and is often used with a negative statement followed by a but to ...
        ]
Relevant (Y/N)?n
Result 5
        [
         URL: https://en.wikipedia.org/wiki/Per_se
         Title: Per se - Wikipedia
         Summary: a primary topic, and an article needs to be written about it. It is believed to qualify as a broad-concept article.
        ]
Relevant (Y/N)?n
Result 6
        [
         URL: https://www.nytimes.com/2004/09/08/dining/the-magic-of-napa-with-urban-polish.html
         Title: The Magic of Napa With Urban Polish - The New York Times
         Summary: Sep 8, 2004 ... Frank Bruni reviews Per Se, Thomas Keller's restaurant at Time Warner Center; photos (L)
        ]
Relevant (Y/N)?y
Result 7
        [
         URL: https://www.instagram.com/perseny/?hl=en
         Title: Per Se (@perseny) • Instagram photos and videos
         Summary: 283K Followers, 202 Following, 1020 Posts - Per Se (@perseny) on Instagram: "Chef Thomas Keller's 3-Star Michelin restaurant overlooking Columbus Circle ...
        ]
Relevant (Y/N)?y
Result 8
        [
         URL: https://www.jamesperse.com/
         Title: James Perse Los Angeles
         Summary: James Perse. Women. Women; Apparel. Apparel Main Menu; New Arrivals · At Home Essentials · Classics · Dresses/Jumpsuits · Sweaters/Cashmere · T-shirts.
        ]
Relevant (Y/N)?n
Result 9
        [
         URL: https://readable.com/blog/how-to-correctly-use-per-se/
         Title: Per se meaning, how to use per se in a sentence | Readable ...
         Summary: Aug 11, 2017 ... 'Per se' is a Latin term which literally means, “by itself”, “in itself” or “of itself”. This means you're taking something out of its context to describe it ...
        ]
Relevant (Y/N)?n
Result 10
        [
         URL: https://en.wikipedia.org/wiki/Per_Se_(restaurant)
         Title: Per Se (restaurant) - Wikipedia
         Summary: Per Se (restaurant) ... Per Se is a New American and French restaurant at The Shops at Columbus Circle, on the fourth floor of the Deutsche Bank Center at 10 ...
        ]
Relevant (Y/N)?y

    FEEDBACK SUMMARY
    Query: per se
    Precision: 0.5
    Still below the desired precision of 0.9
    Indexing results...
    Indexing results...
    Augmenting by restaurant
    
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = per se restaurant
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://www.thomaskeller.com/perseny
         Title: Per Se | Thomas Keller Restaurant Group
         Summary: Private Dining & Events · Per Se. Per Se Front Door. center. Michelin; Les Grandes; Relias. About. About; Restaurant · Team · Info & Directions · Gift ...
        ]
Relevant (Y/N)?y
Result 2
        [
         URL: https://en.wikipedia.org/wiki/Per_Se_(restaurant)
         Title: Per Se (restaurant) - Wikipedia
         Summary: Per Se (restaurant) ... Per Se is a New American and French restaurant at The Shops at Columbus Circle, on the fourth floor of the Deutsche Bank Center at 10 ...
        ]
Relevant (Y/N)?y
Result 3
        [
         URL: https://www.thomaskeller.com/new-york-new-york/per-se/todays-menus
         Title: Today's Menus | Thomas Keller Restaurant Group
         Summary: Private Dining & Events · Per Se. Daily Menus. Two tasting menus are offered daily: a nine-course chef's tasting menu, as well as a nine-course vegetable ...
        ]
Relevant (Y/N)?y
Result 4
        [
         URL: https://guide.michelin.com/us/en/new-york-state/new-york/restaurant/per-se
         Title: Per Se – New York - a MICHELIN Guide Restaurant
         Summary: Per Se – a Three Stars: Exceptional cuisine restaurant in the 2024 MICHELIN Guide USA. The MICHELIN inspectors' point of view, information on prices, ...
        ]
Relevant (Y/N)?y
Result 5
        [
         URL: https://www.thomaskeller.com/new-york-new-york/per-se/restaurant
         Title: Opened in 2004, Per Se is Thomas Keller's acclaimed New York ...
         Summary: Restaurant. Opened in 2004, Per Se is Thomas Keller's acclaimed New York interpretation of The French Laundry in the Deutsche Bank Center at Columbus Circle ...
        ]
Relevant (Y/N)?y
Result 6
        [
         URL: http://www.kevineats.com/2008/12/per-se-new-york-ny.htm
         Title: Per Se (New York, NY) - kevinEats
         Summary: Dec 21, 2008 ... Teams from French Laundry were brought over for training, and the restaurant opened on February 16, 2004, almost exactly a decade after Keller ...
        ]
Relevant (Y/N)?y
Result 7
        [
         URL: https://www.exploretock.com/perse
         Title: Per Se - New York, NY | Tock
         Summary: Opened in 2004, Per Se is Thomas Keller's acclaimed interpretation of ... restaurant is Chef Keller's second three-Michelin-starred property featuring ...
        ]
Relevant (Y/N)?y
Result 8
        [
         URL: https://www.instagram.com/perseny/?hl=en
         Title: Per Se (@perseny) • Instagram photos and videos
         Summary: Chef Thomas Keller's 3-Star Michelin restaurant overlooking Columbus Circle & Central Park located in New York City.
        ]
Relevant (Y/N)?y
Result 9
        [
         URL: https://www.nytimes.com/2004/09/08/dining/the-magic-of-napa-with-urban-polish.html
         Title: The Magic of Napa With Urban Polish - The New York Times
         Summary: Sep 8, 2004 ... Yes, yes: Per Se suffers somewhat by comparison with the French Laundry. That is the Napa Valley restaurant where Thomas Keller, the chef at Per ...
        ]
Relevant (Y/N)?n
Result 10
        [
         URL: https://www.thelotimes.com/p/per-se-french-laundry-price-hike-thomas-keller
         Title: Per Se's Longest Tasting Is Now $1,000! - by ryan sutton
         Summary: Jan 6, 2025 ... Per Se also offers a five-course salon tasting in a separate room with couch seating and low tables. That now runs $285, up twenty bucks. Hey ...
        ]
Relevant (Y/N)?y
Desired precision reached.
```

### Wokcicki Transcript

```
python query_exp.py AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk c66d0519df77f44f1 0.9 "wojcicki"
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = wojcicki
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://en.wikipedia.org/wiki/Susan_Wojcicki
         Title: Susan Wojcicki - Wikipedia
         Summary: an American business executive who was the chief executive officer of YouTube from 2014 to 2023. Her net worth was estimated at $765 million in 2022.
        ]
Relevant (Y/N)?n
Result 2
        [
         URL: https://www.reddit.com/r/poland/comments/3bihro/susan_wojcicki_youtube_ceo_teaches_how_to/
         Title: Susan Wojcicki (YouTube CEO) teaches how to pronounce her ...
         Summary: Jun 29, 2015 ... She's combining Polish and English pronunciation of her last name. She combines the "j" and "c" initially, and then provides the Polish version of "c" as "ts".
        ]
Relevant (Y/N)?n
Result 3
        [
         URL: https://x.com/susanwojcicki?lang=en
         Title: Susan Wojcicki (@SusanWojcicki) / X
         Summary: Susan Wojcicki's posts ... 's team and innovative solutions in sustainability and security to enable transparency and accountability for countries, communities ...
        ]
Relevant (Y/N)?n
Result 4
        [
         URL: https://www.instagram.com/susanwojcicki/?hl=en
         Title: Susan Wojcicki (@susanwojcicki) • Instagram photos and videos
         Summary: YouTube CEO · Photo shared by YouTube for Families on May 27, 2022 tagging @susanwojcicki. Say hello to @susanwojcicki, the CEO of @YouTube. · Photo shared by ...
        ]
Relevant (Y/N)?n
Result 5
        [
         URL: https://x.com/annewoj23?lang=en
         Title: Anne Wojcicki (@annewoj23) / X
         Summary: CEO and Co-Founder, 23andMe.
        ]
Relevant (Y/N)?y
Result 6
        [
         URL: https://blog.youtube/inside-youtube/a-personal-update-from-susan/
         Title: A personal update from Susan - YouTube Blog
         Summary: A personal update from Susan. By Susan Wojcicki. Feb 16, 2023 – 3 minute read. Copy link. A personal update from Susan on stepping back from her role as CEO ...
        ]
Relevant (Y/N)?y
Result 7
        [
         URL: https://www.instagram.com/heywoj/?hl=en
         Title: Esther Wojcicki (@heywoj) • Instagram photos and videos
         Summary: 8216 Followers, 1802 Following, 2042 Posts - Esther Wojcicki (@heywoj) on Instagram: " Author of How to Raise Successful People, Chief Education Advisor ...
        ]
Relevant (Y/N)?n
Result 8
        [
         URL: https://www.facebook.com/esther.wojcicki/posts/it-is-with-soul-crushing-grief-that-i-announce-the-passing-of-my-daughter-susan-/10162259101335763/
         Title: Esther Wojcicki - It is with soul crushing grief that I... | Facebook
         Summary: Aug 10, 2024 ... It is with soul crushing grief that I announce the passing of my daughter Susan. I am eternally grateful she was in my life.
        ]
Relevant (Y/N)?n
Result 9
        [
         URL: https://www.linkedin.com/in/ed-wojcicki-bb02abb
         Title: Ed Wojcicki - Retired... but Consulting and Writing - Retired | LinkedIn
         Summary: Steven Berry. “Ed Wojcicki is a keen listener and intelligent articulator of current circumstances and situations. His ability to discern needs and respond ...
        ]
Relevant (Y/N)?n
Result 10
        [
         URL: https://physics.stanford.edu/news/professor-stanley-wojcicki-has-died-age-86
         Title: Professor Stanley Wojcicki has died at age 86 | Physics Department
         Summary: Jun 5, 2023 ... Stanley G. Wojcicki died on May 31, 2023, at his condo in Los Altos at age 86. He still maintained his home on the Stanford campus.
        ]
Relevant (Y/N)?n

    FEEDBACK SUMMARY
    Query: wojcicki
    Precision: 0.2
    Still below the desired precision of 0.9
    Indexing results...
    Indexing results...
    Augmenting by 23andme
    
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = wojcicki 23andme
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://en.wikipedia.org/wiki/Anne_Wojcicki
         Title: Anne Wojcicki - Wikipedia
         Summary: Anne E. Wojcicki is an American entrepreneur who co-founded and is CEO of the personal genomics company 23andMe. She founded the company in 2006 with Linda ...
        ]
Relevant (Y/N)?y
Result 2
        [
         URL: https://investors.23andme.com/management/anne-wojcicki
         Title: Anne Wojcicki | Board Member,Management | 23andMe, Inc.
         Summary: Anne Wojcicki ... Anne co-founded 23andMe in 2006, three years after the first human genome was sequenced. Her goal was audacious: to help people access, ...
        ]
Relevant (Y/N)?y
Result 3
        [
         URL: https://www.instagram.com/annewoj23/?hl=en
         Title: Anne Wojcicki (@annewoj23) • Instagram photos and videos
         Summary: 15K Followers, 238 Following, 83 Posts - Anne Wojcicki (@annewoj23) on Instagram: "@23andme CEO Co-Founder | Think Big | Lead With Science | I ❤️ DNA| ...
        ]
Relevant (Y/N)?y
Result 4
        [
         URL: https://www.linkedin.com/in/annewojcicki
         Title: Anne Wojcicki - 23andMe | LinkedIn
         Summary: Experience: 23andMe · Location: Mountain View · 500+ connections on LinkedIn. View Anne Wojcicki's profile on LinkedIn, a professional community of 1 ...
        ]
Relevant (Y/N)?y
Result 5
        [
         URL: https://x.com/annewoj23?lang=en
         Title: Anne Wojcicki (@annewoj23) / X
         Summary: CEO and Co-Founder, 23andMe.
        ]
Relevant (Y/N)?y
Result 6
        [
         URL: https://www.cbsnews.com/news/23andme-ceo-anne-wojcicki/
         Title: 23andMe CEO Anne Wojcicki responds to critics, shares plan for ...
         Summary: Nov 27, 2024 ... Wojcicki said she's confident that in 2025, the company will be "growing and thriving." In five years, it "will transform health care," she told King.
        ]
Relevant (Y/N)?y
Result 7
        [
         URL: https://articles.sequoiacap.com/2018-12-12-anne-wojcicki
         Title: Seven Questions with Anne Wojcicki
         Summary: Dec 12, 2018 ... Anne Wojcicki is co-founder and CEO of 23andMe, a direct-to-consumer genetic testing company with more than 5 million customers around the world.
        ]
Relevant (Y/N)?y
Result 8
        [
         URL: https://blog.23andme.com/tag/anne-wojcicki
         Title: Anne Wojcicki Archives - 23andMe Blog
         Summary: Anne Wojcicki, 23andMe's CEO, co-founded the company in 2006, three years after the first human genome was sequenced. Access, Understand and Benefit Her ...
        ]
Relevant (Y/N)?y
Result 9
        [
         URL: https://www.23andme.com/about/
         Title: About us - 23andMe
         Summary: We're not just a health company; we're not just ancestry; we're all of these things. We want to tell you about you. Anne Wojcicki ...
        ]
Relevant (Y/N)?y
Result 10
        [
         URL: https://fortune.com/2024/10/17/23andme-what-happened-stock-board-resigns-anne-wojcicki/
         Title: DNA tester 23andMe's entire board resigned on the same day ...
         Summary: Oct 17, 2024 ... As for Wojcicki, 23andMe has garnered takeover interest from a small New York–based DNA testing startup called Nucleus, but Wojcicki has ...
        ]
Relevant (Y/N)?y
Desired precision reached.
```

### Milky Way Transcript
```
(venv-ml) MacBook-Pro-671:InformationRetrieval maxinetamas$ python query_exp.py AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk c66d0519df77f44f1 0.9 "milky way"
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = milky way
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://en.wikipedia.org/wiki/Milky_Way
         Title: Milky Way - Wikipedia
         Summary: The Milky Way is a barred spiral galaxy with a D25 isophotal diameter estimated at 26.8 ± 1.1 kiloparsecs (87,400 ± 3,600 light-years), but only about 1,000 ...
        ]
Relevant (Y/N)?n
Result 2
        [
         URL: https://www.milkywaybar.com/
         Title: Explore MILKY WAY® Official Website | Chocolate Bars
         Summary: Explore MILKY WAY® Bar products and nutrition information, fun facts about the oh so stretchy caramel chocolate bar, social media channels, and much more!
        ]
Relevant (Y/N)?y
Result 3
        [
         URL: https://www.milkywayla.com/
         Title: Milky Way LA Restaurant Los Angeles
         Summary: Opened in 1977 by Bernie & Leah (Spielberg) Adler, The Milky Way is a storied, family-owned restaurant located in the heart of the Pico-Robertson ...
        ]
Relevant (Y/N)?n
Result 4
        [
         URL: https://science.nasa.gov/resource/the-milky-way-galaxy/
         Title: The Milky Way Galaxy - NASA Science
         Summary: Nov 8, 2017 ... The Milky Way's elegant spiral structure is dominated by just two arms wrapping off the ends of a central bar of stars.
        ]
Relevant (Y/N)?n
Result 5
        [
         URL: https://www.space.com/19915-milky-way-galaxy.html
         Title: Milky Way galaxy: Facts about our cosmic neighborhood | Space
         Summary: Apr 18, 2023 ... Everything else in the galaxy revolves around this powerful gateway to nothingness. In its immediate surroundings is a tightly packed region of ...
        ]
Relevant (Y/N)?n
Result 6
        [
         URL: https://imagine.gsfc.nasa.gov/science/objects/milkyway1.html
         Title: NASA - The Milky Way Galaxy
         Summary: The Milky Way is a large barred spiral galaxy. All the stars we see in the night sky are in our own Milky Way Galaxy.
        ]
Relevant (Y/N)?n
Result 7
        [
         URL: https://www.amnh.org/explore/ology/astronomy/the-milky-way-galaxy2
         Title: The Milky Way Galaxy | AMNH
         Summary: The Milky Way is a huge collection of stars, dust and gas. It's called a spiral galaxy because if you could view it from the top or bottom, it would look like a ...
        ]
Relevant (Y/N)?n
Result 8
        [
         URL: https://www.milkywaypgh.com/
         Title: Milky Way Pittsburgh
         Summary: Here at Milky Way, we pride ourselves on offering delicious Kosher alternatives to the essential pizzeria foods normally sold in a standard pizzeria.
        ]
Relevant (Y/N)?n
Result 9
        [
         URL: https://www.nasa.gov/image-article/milky-way-on-the-horizon/
         Title: Milky Way on the Horizon - NASA
         Summary: 21 hours ago ... NASA astronaut Don Pettit used a camera with low light and long duration settings to capture this Jan. 29, 2025, image of the Milky Way ...
        ]
Relevant (Y/N)?n
Result 10
        [
         URL: https://rowstercoffee.com/products/milky-way
         Title: Milky Way – Rowster Coffee
         Summary: Roast Level: Medium - Dark Tasting Notes: Rich, Walnut, Sweet Description: Our flagship blend, showcases our range of roast profiles and ability to source ...
        ]
Relevant (Y/N)?n

    FEEDBACK SUMMARY
    Query: milky way
    Precision: 0.1
    Still below the desired precision of 0.9
    Indexing results...
    Indexing results...
    Augmenting by bar
    
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = milky way bar
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://en.wikipedia.org/wiki/Milky_Way_(chocolate_bar)
         Title: Milky Way (chocolate bar) - Wikipedia
         Summary: Milky Way (chocolate bar) ... Milky Way is a brand of chocolate-covered confectionery bar manufactured and marketed by Mars Inc.. There are two varieties: ...
        ]
Relevant (Y/N)?y
Result 2
        [
         URL: https://www.milkywaybar.com/
         Title: Explore MILKY WAY® Official Website | Chocolate Bars
         Summary: Explore MILKY WAY® Bar products and nutrition information, fun facts about the oh so stretchy caramel chocolate bar, social media channels, and much more!
        ]
Relevant (Y/N)?y
Result 3
        [
         URL: https://www.milkywaycocktails.com/
         Title: Milky Way
         Summary: C'est une fraicheur tropicale qui vous attend en haut des marches black light et fluo du Milky Way. Niché au coeur de Pointe Saint-Charles, le nouveau bar à ...
        ]
Relevant (Y/N)?y
Result 4
        [
         URL: https://www.reddit.com/r/AskEurope/comments/9plczy/whats_inside_a_milky_way_bar/
         Title: What's inside a Milky Way bar? : r/AskEurope
         Summary: Oct 19, 2018 ... I was surprised when I watched this ad because in Russia Milky Way contains souffle inside.
        ]
Relevant (Y/N)?^CTraceback (most recent call last):
  File "/Users/maxinetamas/class/advanced_db_systems-s2025/InformationRetrieval/query_exp.py", line 116, in <module>
    main(args.google_api_key, args.google_engine_id, args.precision, args.query)
  File "/Users/maxinetamas/class/advanced_db_systems-s2025/InformationRetrieval/query_exp.py", line 90, in main
    cur_precision, rlvnt_docs, irrlvnt_docs = get_user_feedback(query_results)
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/maxinetamas/class/advanced_db_systems-s2025/InformationRetrieval/query_exp.py", line 46, in get_user_feedback
    relevance = input("Relevant (Y/N)?")
                ^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

(venv-ml) MacBook-Pro-671:InformationRetrieval maxinetamas$ python query_exp.py AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk c66d0519df77f44f1 0.9 "milky way"
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = milky way
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://en.wikipedia.org/wiki/Milky_Way
         Title: Milky Way - Wikipedia
         Summary: The Milky Way is a barred spiral galaxy with a D25 isophotal diameter estimated at 26.8 ± 1.1 kiloparsecs (87,400 ± 3,600 light-years), but only about 1,000 ...
        ]
Relevant (Y/N)?n
Result 2
        [
         URL: https://www.milkywaybar.com/
         Title: Explore MILKY WAY® Official Website | Chocolate Bars
         Summary: Explore MILKY WAY® Bar products and nutrition information, fun facts about the oh so stretchy caramel chocolate bar, social media channels, and much more!
        ]
Relevant (Y/N)?y
Result 3
        [
         URL: https://www.milkywayla.com/
         Title: Milky Way LA Restaurant Los Angeles
         Summary: Opened in 1977 by Bernie & Leah (Spielberg) Adler, The Milky Way is a storied, family-owned restaurant located in the heart of the Pico-Robertson ...
        ]
Relevant (Y/N)?n
Result 4
        [
         URL: https://science.nasa.gov/resource/the-milky-way-galaxy/
         Title: The Milky Way Galaxy - NASA Science
         Summary: Nov 8, 2017 ... The Milky Way's elegant spiral structure is dominated by just two arms wrapping off the ends of a central bar of stars.
        ]
Relevant (Y/N)?n
Result 5
        [
         URL: https://www.space.com/19915-milky-way-galaxy.html
         Title: Milky Way galaxy: Facts about our cosmic neighborhood | Space
         Summary: Apr 18, 2023 ... Everything else in the galaxy revolves around this powerful gateway to nothingness. In its immediate surroundings is a tightly packed region of ...
        ]
Relevant (Y/N)?n
Result 6
        [
         URL: https://imagine.gsfc.nasa.gov/science/objects/milkyway1.html
         Title: NASA - The Milky Way Galaxy
         Summary: The Milky Way is a large barred spiral galaxy. All the stars we see in the night sky are in our own Milky Way Galaxy.
        ]
Relevant (Y/N)?n
Result 7
        [
         URL: https://www.amnh.org/explore/ology/astronomy/the-milky-way-galaxy2
         Title: The Milky Way Galaxy | AMNH
         Summary: The Milky Way is a huge collection of stars, dust and gas. It's called a spiral galaxy because if you could view it from the top or bottom, it would look like a ...
        ]
Relevant (Y/N)?n
Result 8
        [
         URL: https://www.milkywaypgh.com/
         Title: Milky Way Pittsburgh
         Summary: Here at Milky Way, we pride ourselves on offering delicious Kosher alternatives to the essential pizzeria foods normally sold in a standard pizzeria.
        ]
Relevant (Y/N)?n
Result 9
        [
         URL: https://www.nasa.gov/image-article/milky-way-on-the-horizon/
         Title: Milky Way on the Horizon - NASA
         Summary: 21 hours ago ... NASA astronaut Don Pettit used a camera with low light and long duration settings to capture this Jan. 29, 2025, image of the Milky Way ...
        ]
Relevant (Y/N)?n
Result 10
        [
         URL: https://rowstercoffee.com/products/milky-way
         Title: Milky Way – Rowster Coffee
         Summary: Roast Level: Medium - Dark Tasting Notes: Rich, Walnut, Sweet Description: Our flagship blend, showcases our range of roast profiles and ability to source ...
        ]
Relevant (Y/N)?n

    FEEDBACK SUMMARY
    Query: milky way
    Precision: 0.1
    Still below the desired precision of 0.9
    Indexing results...
    Indexing results...
    Augmenting by bar
    
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = milky way bar
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://en.wikipedia.org/wiki/Milky_Way_(chocolate_bar)
         Title: Milky Way (chocolate bar) - Wikipedia
         Summary: Milky Way (chocolate bar) ... Milky Way is a brand of chocolate-covered confectionery bar manufactured and marketed by Mars Inc.. There are two varieties: ...
        ]
Relevant (Y/N)?y
Result 2
        [
         URL: https://www.milkywaybar.com/
         Title: Explore MILKY WAY® Official Website | Chocolate Bars
         Summary: Explore MILKY WAY® Bar products and nutrition information, fun facts about the oh so stretchy caramel chocolate bar, social media channels, and much more!
        ]
Relevant (Y/N)?y
Result 3
        [
         URL: https://www.milkywaycocktails.com/
         Title: Milky Way
         Summary: C'est une fraicheur tropicale qui vous attend en haut des marches black light et fluo du Milky Way. Niché au coeur de Pointe Saint-Charles, le nouveau bar à ...
        ]
Relevant (Y/N)?n
Result 4
        [
         URL: https://www.reddit.com/r/AskEurope/comments/9plczy/whats_inside_a_milky_way_bar/
         Title: What's inside a Milky Way bar? : r/AskEurope
         Summary: Oct 19, 2018 ... I was surprised when I watched this ad because in Russia Milky Way contains souffle inside.
        ]
Relevant (Y/N)?y
Result 5
        [
         URL: https://greenvalleykitchen.com/milky-way-walnut-cookie-bars/
         Title: Milky Way Walnut Cookie Bars - Green Valley Kitchen
         Summary: Nov 16, 2014 ... I added 1 cup of Milky Way pieces to the batter. After baking the cookie bars for 15 minutes, I took the pan out of the oven and sprinkled the ...
        ]
Relevant (Y/N)?n
Result 6
        [
         URL: https://www.reddit.com/r/cocktails/comments/b72cub/almost_3_months_after_the_opening_milky_way/
         Title: Almost 3 months after the opening ! Milky Way cocktail bar in MTL : r ...
         Summary: Mar 29, 2019 ... The bar looks AWESOME! I'm in the process of opening a spot in Chicago and we're currently in the works of removing the ceiling to put in a 40 ft skylight.
        ]
Relevant (Y/N)?n
Result 7
        [
         URL: https://www.tripadvisor.com/ShowTopic-g60709-i381-k10932518-Milky_Way-Bar_Harbor_Mount_Desert_Island_Maine.html
         Title: Milky Way - Bar Harbor Forum - Tripadvisor
         Summary: Oct 12, 2017 ... Yes, you should be able to see the Milky Way on a clear night in Acadia at this time of year. Early evening hours from Sand Beach would be good.
        ]
Relevant (Y/N)?n
Result 8
        [
         URL: https://www.reddit.com/r/candy/comments/1ekb7gy/is_there_a_real_difference_between_a_mars_bar_and/
         Title: Is there a real difference between a Mars Bar and a Milky Way? : r ...
         Summary: Aug 5, 2024 ... The US Milky Way is softer in texture than a Mars bar. Third, the ratio of nougat, caramel and chocolate is different in the US Milky Way and a Mars bar.
        ]
Relevant (Y/N)?y
Result 9
        [
         URL: https://www.aanda.org/articles/aa/full_html/2024/01/aa48365-23/aa48365-23.html
         Title: Insights from super-metal-rich stars: Is the Milky Way bar young ...
         Summary: Jan 10, 2024 ... We study a homogeneous and large sample of SMR stars in the SNd to provide tighter constraints on the epoch of the bar formation and its impact on the Milky ...
        ]
Relevant (Y/N)?n
Result 10
        [
         URL: https://www.reddit.com/r/todayilearned/comments/17f88kl/til_the_chocolate_bar_milky_way_is_called_mars/
         Title: TIL The chocolate bar Milky Way is called Mars Bar by the non-US ...
         Summary: Oct 24, 2023 ... Aus - Milky way is a tiny bar with just whipped nougat. A Mars bar is full size with a layer of caramel. The advertising campaigns are totally ...
        ]
Relevant (Y/N)?y

    FEEDBACK SUMMARY
    Query: milky way bar
    Precision: 0.5
    Still below the desired precision of 0.9
    Indexing results...
    Indexing results...
    Augmenting by chocolate
    
Parameters:
    Client key  = AIzaSyDSfAcOzN3SyrUDN2fCe_QNIIx3sOLN5Rk
    Engine key  = c66d0519df77f44f1
    Query       = bar way milky chocolate
    Precision   = 0.9
Google Search Results:
======================
Result 1
        [
         URL: https://en.wikipedia.org/wiki/Milky_Way_(chocolate_bar)
         Title: Milky Way (chocolate bar) - Wikipedia
         Summary: Milky Way (chocolate bar) ... Milky Way is a brand of chocolate-covered confectionery bar manufactured and marketed by Mars Inc.. There are two varieties: ...
        ]
Relevant (Y/N)?y
Result 2
        [
         URL: https://www.milkywaybar.com/
         Title: Explore MILKY WAY® Official Website | Chocolate Bars
         Summary: Explore MILKY WAY® Bar products and nutrition information, fun facts about the oh so stretchy caramel chocolate bar, social media channels, and much more!
        ]
Relevant (Y/N)?y
Result 3
        [
         URL: https://sherisilver.com/2016/06/23/white-chocolate-milky-way-bars/
         Title: white chocolate milky way bars! | Sheri Silver - living a well-tended ...
         Summary: Jun 23, 2016 ... 2 cups white chocolate chips, divided 7-ounce container Marshmallow Fluff 1/4 cup malted milk powder (plus extra, for sprinkling) 7 ounces ...
        ]
Relevant (Y/N)?y
Result 4
        [
         URL: https://www.milkywaybar.com/our-products
         Title: Our Chocolate Candy Bar Products | MILKY WAY®
         Summary: So. Much. Caramel. From classic favorites to latest releases, discover every MILKY WAY®chocolate candy product.
        ]
Relevant (Y/N)?y
Result 5
        [
         URL: https://www.amazon.com/MilkyWay-Candy-Milk-Chocolate-Bars/dp/B0029JFOVK
         Title: MilkyWay Candy Milk Chocolate Bars Bulk Pack, Full ... - Amazon.com
         Summary: MilkyWay Candy Milk Chocolate Bars Bulk Pack, Full Size, 1.84 oz Pack of 36) · 1.84 Ounce (Pack of 36). $38.94$38.94. $0.59 per Ounce($0.59$0.59 / Ounce). In ...
        ]
Relevant (Y/N)?y
Result 6
        [
         URL: https://www.reddit.com/r/unpopularopinion/comments/qhxa8h/milky_way_is_the_best_chocolate_bar/
         Title: Milky Way is the best chocolate bar. : r/unpopularopinion
         Summary: Oct 28, 2021 ... Milky Way is the best chocolate bar. Call me a child, but the smoothness of the milk chocolate, and the caramel within it gives it a taste of pure bliss and ...
        ]
Relevant (Y/N)?y
Result 7
        [
         URL: https://www.cupcakeproject.com/nougat-with-chocolate-malt-like-in/
         Title: Nougat With Chocolate Malt - Like in Milky Way Bars - Cupcake ...
         Summary: Jan 24, 2011 ... Ingredients · ▢ 2 cups granulated sugar · ▢ 2/3 cup light corn syrup · ▢ 2/3 cup water · ▢ 2 large egg whites · ▢ 2 ounces unsweetened chocolate
        ]
Relevant (Y/N)?y
Result 8
        [
         URL: https://www.reddit.com/r/traderjoes/comments/13v42j9/appreciation_post_for_the_scoring_on_the_milk/
         Title: Appreciation post for the scoring on the milk chocolate and ...
         Summary: May 29, 2023 ... Is it just me or does the branding on the packaging make anyone else think of the Milk Bar corn flake cookies? The way “milk” and “bar” are ...
        ]
Relevant (Y/N)?n
Result 9
        [
         URL: https://chocolatebythebay.com/magazine/outsidechocolate/the-milky-way/
         Title: The Milky Way – Chocolate by the Bay
         Summary: Feb 17, 2022 ... The taste was unique: savory, not very milky, a little smoky, and caramelized. It's a not too sweet bar, with a deeper, richer taste than ...
        ]
Relevant (Y/N)?y
Result 10
        [
         URL: https://togo.foodlion.com/store/food-lion/products/103823-milky-way-milk-chocolate-candy-bar-share-2-ea
         Title: Milky Way Candy Milk Chocolate Bar Share Size Same-Day ...
         Summary: Smooth nougat, creamy caramel and rich milk chocolate. That's what some might call the MILKY WAY trifecta. And a treat this delectable is too good not to share.
        ]
Relevant (Y/N)?y
Desired precision reached.
```