Problem Summary:

	A company that sells cars wants to control the proportion of vehicles that have been sold and return to the official points of service of the brand,
	with this in mind, it defines the following:

		-month and year from which the calculations are going to be made.
		-the concept of the active customer, as vehicles that have gone to service at least once in the last 12 months from the date of
		analysis (month and year previously defined), in addition the vehicles cannot be older than 10 years in relation with this
		date with an adjustment of 3 months backwards(This offset is made since it is almost impossible for a vehicle with 3 months of 
		use to go to service and a vehicle older than 10 years is no longer relevant to the company).
	 
	In addition to calculating the global ratio, the company wants to calculate the KPI by dealer, in order to send this result to the dealers,
	along with the details by mail (Customer name, Mail, Date of last service, etc.), so they can help improve the KPI score with specific actions.

	Since we are talking about customer information, we cannot work directly with the original data, so we must replicate it in some way.

	The structure of the sales base is:

		-The social security number of the client that bought the car, data type: VARCHAR(50).
		-Date of sale of the vehicle, data type: DATE.
		-VIN of the vehicle, data type: VARCHAR(50).
		-Email of the client that bought the car, data type: VARCHAR(50).
		-Name of the client that bought the car, data type: VARCHAR(50).
		-Brand of the vehicle, data type: VARCHAR(50).
		-Dealer where the car was purchased data type: VARCHAR(50).
		
	The structure of the service base is:

		-The social security number of the client that went to service, data type: VARCHAR(50).
		-Date of service of the vehicle, data type: DATE.
		-VIN of the vehicle that went to service , data type: VARCHAR(50).
		-Email of the client that went to service, data type: VARCHAR(50).
		-Name of the client that went to service, data type: VARCHAR(50).
		-Brand of the vehicle that went to service, data type: VARCHAR(50).
		-Dealer where the car performed the service data type: VARCHAR(50).


Challenges:
	
	-Find a way to replicate the data in order to make the calculations and dashboards.
	-Upload the data to Tableau Prep in order to do the ETL process.
	-Define the ETL process.
	-Make the dashboards that we are going to use and send.
	-Find a way to send the information to the dealers.

Solution:

	-Create a on-premise database in postgresql with the two tables described previously.
	-Upload the tables of the database to Tableau Cloud using the Tableau REST API and the Tableau Hyper API.
	-Perform the necessary ETL processing on the tables previously loaded.
	-Create the dashboard to control and send the KPI.
	-Send the KPI Dashboards to the dealers by integrating tableau with the GMAIL API for automatic sending.

	
	
	
Script explanation:

Pending.
	