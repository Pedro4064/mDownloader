# mDownloader

## [mDownloader.py]()
•Download and make PDFs from mangas from [KissManga](https://kissmanga.com/).<br/>
•It only works on Unix based systems.<br/>
•You may pass as an argument the number of the volume you wish to start the download from.

![Main prompt](https://github.com/Pedro4064/mDownloader/blob/master/Images/Main.png?raw=true)
![-h as an argument](https://github.com/Pedro4064/mDownloader/blob/master/Images/-h.png?raw=true)

## [dailyCheck.py](https://github.com/Pedro4064/MangaDownloader/blob/master/Raspberry%20Pi%20Daily%20check/dailyCheck.py)
•Set a raspberry pi to check every day for new volumes, download them, make a pdf and send to kindle/email automatically.<br/>
•It uses a csv file (info.csv) to get the last volume's info and update it once it downloades the latest chapter.<br/>

•The csv file has the following structure:
|Title|kissmanga series' main link|Latest volume's link|
|-----|--------------------------|---------------------|
example-> [info.csv](https://github.com/Pedro4064/MangaDownloader/blob/master/Raspberry%20Pi%20Daily%20check/info.csv)


## Modules

### Python
  •To install all modules run: <br/>
   `python -m pip install -r /path/to/requirements.txt`

#### Preinstalled
•os<br/>
•time<br/>
•sys<br/>
•requests<br/>

#### Needs to be installed separately  
•[termcolor](https://pypi.org/project/termcolor/)<br/>
•[selenium](https://pypi.org/project/selenium/)<br/>
•[progress](https://pypi.org/project/progress/)<br/>

## Chrome Driver

  •You also need to download [chromedriver](http://chromedriver.chromium.org/downloads) to use with selenium module.<br/> 
  *If you are on the raspberry pi, follow this [instructions](https://www.reddit.com/r/selenium/comments/7341wt/success_how_to_run_selenium_chrome_webdriver_on/). <br/>
### Unix based System			
•[Imagemagick ](https://imagemagick.org/index.php)<br/>
	-> Or using the terminal:
	`sudo apt install imagemagick`<br/>



## Notes
-Change the `driverPath = '/Applications/chromedriver'` to fit the location of the webDriver in your system.<br/>
-Make sure you have installed all the necessary libraries.<br/>
-It only works on UNIX based systems(macosx/linux), although you can change the bash commands to the equivalent prompt commands for Windows(Don't know if there is an Imagemagick pack for Windows).
