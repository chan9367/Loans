# Loans

Our client has asked us to develop a monthly report for them detailing the work our BOTs have done in the given month. The report will be made available to the client via a webpage in our dashboard web application.

Our data team has already extracted the loan file information for all loans made during the month under review and that data has been provided to you in JSON format in the loans.json file attached to this email. We need you to write a program that can import the loan data from the JSON file, perform a series of calculations on the data, and then write the results of those calculations to new JSON files. The webpage will read in the JSON files you generate and display them in a user-friendly way to the client.

Your program needs to analyze the loans contained in the loanFiles.json file and perform the following calculations:
	
	* The sum, average, median, minimum and maximum values for the following fields:
		* LoanAmount
		* SubjectAppraisedAmount
		* InterestRate

We need these calculations both for the entire file and then we also need them broken down by state (utilizing the SubjectState field.) We want these results in TWO different JSON files.

Please provide as your solution the two JSON files as described below plus any and all code you wrote to achieve your result. Please round all decimal values to 2 digits of precision, rounding to the nearest value.

The first should be called monthlySummary.json and should contain the calculations across all states.

The second JSON file should be called monthlyByState.json. It should contain the same calculations as the monthlySummary.json file, but this time grouped by state.
