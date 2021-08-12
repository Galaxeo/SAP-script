Added here to be able to change from desktop to laptop

SAP Script - Python script made to take an input (in our case, phone #s or IPs), search a CSV (spreadsheets WIP), and output the corresponding values (which in our case were phone locations/positions) that are sorted in a way to assist the interns' workflows. While doing this, I learned how to use the Google Sheets API and the Google Cloud Console at a very basic level, while also attempting to implement pandas, but instead used a dictionary as given by the gspread package when collecting data from a speadsheet. [Reminder to self to upload updated version with Google Sheets API when home at desktop]

Please keep in mind that acceptable forms are as such:
  1. List of phone #s in a comma sepearted list as such: 1023, 1034, 213, 523, ...
  2. List of IPs copy pasted as such:
	172.16.0.251
	172.16.1.20
	172.16.0.235
	172.16.2.34
	172.16.0.212
	172.16.0.216
	etc.

