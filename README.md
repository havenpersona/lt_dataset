# Korean-English Lyric Translation Dataset

This repository provides the dataset introduced in our paper titled ["K-pop Lyric Translation: Dataset, Analysis, and Neural Modelling."](https://arxiv.org/abs/2309.11093) from LREC-COLING 2024.

If you find this dataset useful for your research, please consider citing our paper.

```
@inproceedings{kim2024kpop,
  title={K-pop Lyric Translation: Dataset, Analysis, and Neural Modelling},
  author={Kim, Haven and Jung, Jongmin and Jeong, Dasaem and Nam, Juhan},
  booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING)},
  year={2024},
}
```

If you have any question regarding this datset, contact me (Haven Kim) via **khaven@kaist.ac.kr**. (Please understand that sometimes my reply gets delayed, but be sure to hear from me!)

Please note that our dataset is related to alignment, not the lyrics themselves. We do not claim ownership of the lyrics in any way.

## 1. Obtain Lyrical Text
To obtain lyrics for the corresponding title and artist, please refer to meta.csv and retrieve them manually. meta.csv provides metadata for 1000 songs, including the track title, artist name, and a unique ID, called LID within this dataset. However, unofficial English translations by YouTubers Emily Dimes and Serri are available for direct download from this GitHub repository, thanks to their generosity.

We provide an example code for retrieving lyrics using the Genius Lyrics API. 
Before running the code, you need to obtain your genius token by signing up at [https://genius.com/](https://genius.com/).
To execute the code, follow these steps:
```
pip install lyricsgenius
python crawl.py
```

Once you've completed the download, your directory structure should resemble the following:

repository<br>
├── unprocessed_lyrics<br>
│   ├── 001en.txt<br>
│   ├── 001kr.txt<br>
│   ├── 002en.txt<br>
│   ├── 002kr.txt<br>
│   ├── .<br>
│   ├── .<br>
├── processed_lyrics<br>
│   ├── 089en.txt<br>
│   ├── 107en.txt<br>
│   ├── .<br>
│   ├── .<br>
├── crawl.py<br>
├── match.py<br>
├── meta.csv<br>
├── symbol.json


## 2. Match Symbolic Data to Lyrical Text
In symbol.json, lyrics for one song consists of a series of lists. Each list consists of multiple strings, and each string corresponds to a single line, represented as initial characters, the first and last words, as well as the length of characters. For example, consider the following lyrics, which comprised of 5 sections and 20 lines. 
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

They will be represented a list that consists of 5 lists (which means this song consists of 5 sections), each consists of four strings, as below.

```
[('ttls', 'twinkle', 'star', 24), ('hiwwya', 'how', 'are', 20), ('uatwsh', 'up', 'high', 21), ('ladits', 'like', 'sky', 20), ('wtbsig', 'when', 'gone', 23), ('whnsu', 'when', 'upon', 23), ('tysyll', 'then', 'light', 26), ('ttatn', 'twinkle', 'night', 25), ('tttitd', 'then', 'dark', 25), ('tyfyts', 'thanks', 'spark', 25), ('hcnswwtg', 'he', 'go', 25), ('iydnts', 'if', 'so', 20), ('itdbsyk', 'in', 'keep', 23), ('aotmcp', 'and', 'peep', 27), ('fynsye', 'for', 'eye', 22), ('ttsiits', 'till', 'sky', 20), ("'ybats", "'tis", 'spark', 26), ('lttitd', 'lights', 'dark', 27), ('tiknwya', "tho'", 'are', 22), ('ttls', 'twinkle', 'star', 24)]
```

You will need to find the corresponding line manually. We provide an example code for matching the symbolic data to lyrical text in match.py. To execute the code, follow this step. 

```
pip install wordninja
python match.py
```

As of February 22, 2024, I plan to regularly update and improve this repository. If you encounter any issues or have suggestions, please feel free to contact me at **khaven@kaist.ac.kr**. (Please understand that sometimes my reply gets delayed, but be sure to hear from me!)


<br>
<br>

## Acknowledgements
We sincerely appreciate [Serri](https://www.youtube.com/channel/UCRbno5ZQiMrp5lSx95NYLHQ) and [Emily Dimes](https://www.youtube.com/@EmilyDimes) for allowing us to feature their English translations in this GitHub repository. Those interested in lyric translation should definitely check out their channels.
