# Roman Empire Coins - Numismatic.org downloader

This repository contains two Python scripts designed for downloading and organizing images of Roman Empire coins from the American Numismatic Society (ANS) website. The main objective is to create a comprehensive dataset of Roman coin images for research purposes, specifically focusing on coins from various Roman emperors.

## Project Overview

The goal of this project is to gather images of Roman coins, which can serve as a valuable dataset for research in numismatics, historical studies, or machine learning applications. Currently, two scripts are included in the repository:

- `download.py`: Downloads images of coins from a specified Roman emperor.
- `delete.py`: Removes specific coin images (either obverses or reverses) from the dataset based on image numbering.

## How to use

To install required packages, run:

```
pip install -r requirements.txt
```

Set the emperor's name and the number of photos to download in `download.py` (make sure to check how many there are maximum on the page for the given category). Run the script (it will take a while).

If you only want to "clean" the folder of downloaded images containing page elements, set _clean_only_ to True in `delete.py`. If you also want to remove obverses or reverses, set this parameter to False. You can use the _remove_obverse_ parameter to specify whether to remove obverses (True) or reverses (False). Run the program `delete.py`.
