This repository provides the dataset introduced in our paper titled ["K-pop Lyric Translation: Dataset, Analysis, and Neural Modelling."](https://arxiv.org/abs/2309.11093)

If you find this dataset useful for your research, please consider citing our paper. (Ye we're refraining from advertising our paper as it's still under review as of December 31, 2023)

```
@misc{kim2023kpop,
  title={K-pop Lyric Translation: Dataset, Analysis, and Neural Modelling},
  author={Haven Kim and Jongmin Jung and Dasaem Jeong and Juhan Nam},
  year={2023},
  eprint={2309.11093},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

If you have any question regarding this datset, contact me (Haven Kim) via **khaven@kaist.ac.kr**. (Please understand that sometimes my reply gets delayed, but be sure to hear from me!)

Please note that our dataset is related to alignment, not the lyrics themselves. We do not claim ownership of the lyrics in any way.

1. Obtain Lyrical Text
To obtain lyrics for the corresponding title and artist, please refer to meta.csv and retrieve them manually. meta.csv provides metadata for 1000 songs, including the track title, artist name, and a unique ID known as LID within this dataset. However, unofficial English translations by YouTubers Emily Dimes and Serri are available for direct download from this GitHub repository, thanks to their generosity.

We provide an example code for retrieving lyrics using the Genius Lyrics API and refining them. To execute the code, follow these steps:

```
python crawl.py
python refine.py
```

Once you've completed the download, your directory structure should resemble the following:

repository
├── lyrics
│   ├── 001en.txt
│   ├── 001kr.txt
│   ├── 002en.txt
│   ├── 002kr.txt
│   ├── .
│   ├── .
│   ├── 1000en.txt
│   ├── 1000kr.txt
├── crawl.py
├── match.py
├── meta.csv
├── refine.py
├── symbol.json


2. Match Symbolic Data to Lyrical Text
In symbol.json, lyrics for one song consists of a series of lists. Each list consists of multiple strings, and each string corresponds to a single line, represented as te initial words as well as the first and last words. For example, consider the following lyrics, which comprised of 5 sections and 20 lines. 
```
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
```

They will be represented a list that consists of 5 lists, each consists of four strings, as below.

```
[('ttls', 'twinkle', 'star'), ('hiwwya', 'how', 'are'), ('uatwsh', 'up', 'high'), ('ladits', 'like', 'sky'), ('wtbsig', 'when', 'gone'), ('whnsu', 'when', 'upon'), ('tysyll', 'then', 'light'), ('ttatn', 'twinkle', 'night'), ('tttitd', 'then', 'dark'), ('tyfyts', 'thanks', 'spark'), ('hcnswwtg', 'he', 'go'), ('iydnts', 'if', 'so'), ('itdbsyk', 'in', 'keep'), ('aotmcp', 'and', 'peep'), ('fynsye', 'for', 'eye'), ('ttsiits', 'till', 'sky'), ("'ybats", "'tis", 'spark'), ('lttitd', 'lights', 'dark'), ('tiknwya', "tho'", 'are'), ('ttls', 'twinkle', 'star')]
```

You will need to find the corresponding line manually. We provide an example code for matching the symbolic data to lyrical text in match.py. To execute the code, follow this step. 

```
python match.py
```
