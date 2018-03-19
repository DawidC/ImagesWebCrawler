ImagesWebCrawler

Web crawler in Python, using Spark, to crawl web in search for images and classify them for specific object. 

Program using Sparkler, to crawl web for specific URLs:
https://github.com/USCDataScience/sparkler
DatabricksTensorFlow to classify images:
https://databricks.com/blog/2016/01/25/deep-learning-with-apache-spark-and-tensorflow.html

First run <code> bash run-sparkler.sh </code> <br>
Next from solr web console <link>http://localhost:8983/solr/</link> export URLs to .csv file
<br>
Next run <code>img_download.py</code> to download all files from crawled URLs, pack all filenames into .txt file and compress it to .tar.gz file <br>
Finally run <code>img_recognition_tensor.py</code> to classify all crawled photos.
<br><br>
TODO: <ul> change paths to relative </ul>
<ul> change neural network(?) </ul>
<ul> automate running sparkler and generating .csv file </ul>




