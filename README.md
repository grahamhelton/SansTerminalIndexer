# Sans Terminal Indexer
Sans terminal indexer is a program that I have been using for the last couple of months decrease the amount of time it takes to create an index from a $ANS book, although it could be used for any book you need to create an index of. The goal of this project is to create a very fast/efficient way to create an index. This program was greatly inspired by Matthew Toussain's [Voltaire](https://voltaire.publickey.io/) and Lesley Carhart's [Better GIAC testing With Pancakes](https://tisiphone.net/2015/08/18/giac-testing/)


Currently the indexer has the following features are implemented
- Creates/stores index in `~/.Indexes` folder
- Takes input in the format of **Term, page number**. 

# Install

```bash
git clone https://github.com/grahamhelton/SansTerminalIndexer
cd SansTerminalIndexer
pip3 install pandas
./index.py
```

# Images

![sansterminalindex](https://user-images.githubusercontent.com/19278569/198133246-16d24198-b968-4beb-8d0e-c7a88ac430c2.png)

![createCsv](https://user-images.githubusercontent.com/19278569/198133658-1eca6c0f-7859-43e6-9f6d-faecde6ca89a.gif)


# Todo
For the most part, this tool is complete. However, I would like to add the following features if I have time.
- Add edit feature (edit previous index entries)
- Add CSV sorting (Sort by book then alphabetical)
