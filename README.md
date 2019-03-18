# CPI-Calculator
This is a simple program that allows you to compute a CPI(Cost Per Installation) using two different .scv file.
## Objectives
Using input data (files in_data_a.csv and in_data_p.csv), in one of which there is information about expenses, and in the other – information about installations, information about the cost of one installation for each advertising campaign is calculated, broken down by the names of the advertised applications and by the days in which the advertising campaigns worked(file out.csv).
## List of files:
``in_data_a.csv``  ``in_data_p.csv``    
``out.csv``
``CPICalc.py``
## Columns in .csv files:
### in_data_a.csv:
* date - date in YYYY-MM-DD
* campaign - name of ads campaign
* id - ID of the source of ads
* ad_id - ID of the banner used in the ad campaign
* os - OS of the device
* installs - number of installs
* app - name of the app
### in_data_p.csv:
* date - date in YYYY-MM-DD
* campaign_id - ID of the ads campaign
* ad_id - ID of the banner used in the ad campaign
* spend - amount that was spent on mobile app advertising
### out.csv:
* app
* date
* campaign
* os
* installs
* spend
* cpi
