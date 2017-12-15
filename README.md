
# NEWS ARTICLE REPORTING TOOL

This project is a reporting tool that queries a database called 'news' which contains information on articles, their authors, and a log table. Out of the box the reporting tool can report:
 1) The top 3 most popular articles,
 2) The authors in order of popularity,
 3) Days which saw a server response error rate over 1%.

## GETTING STARTED

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### PREREQUISITES

To run the reporting tool you will need to be comfortable with; python, postgres sql and vagrant virtual machine.
You will also need to download the news database which can be found [Here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

For instructions on how to load vagrant and run the newsdata.sql refer to 'Log Analysis project' which is part of 'The backend: Databases and applications' Udacity course

### INSTALLATION AND RUNNING

1) Once you have loaded newsdata.sql to your vagrant machine, clone or download this repository to the same folder.

2) Connect to vagrant in the command line -$ vagrant ssh

3) Once connected confirm you are in the the same folder as both newsdata.sql and reporting_tool.py. If not cd to the right folder.

4) Once in the right folder you will need to create two new views in the news database:

 - Load postgres in command with -$ psql
 - Connect to the news database -  \c news
 - Create a view which links the author id to the article author:

    > CREATE VIEW authors_slug AS   
    > SELECT authors.name AS authors,
    > articles.slug   FROM articles   JOIN authors ON authors.id =
    > articles.author;

 - Create a view with dummy variables for status codes to help calculate the error rate per day:

	> CREATE VIEW day_percent_error AS
	> SELECT to_char(time::date,'DD Month YYYY') AS date,
	> CAST((SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END) * 100)/ ((SUM(CASE WHEN status = '200 OK' THEN 1 ELSE 0 END) * 1.0) + SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END)) AS decimal(10,2)) AS percent_error
	> FROM log
	> GROUP BY date;

5) Once the views are created run the reporting_tool.py file with the command$ python reporting_tool.py

6) The results from the report will print in the command line. Refer to report.txt for an output example.

####BUILT WITH

python3.0
postgres sql
vagrant

####AUTHORS

louisorluigi
