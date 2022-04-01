import json, statistics

#change this directory to where your json file is in
jsonFile = open('d:/loans.json')

jsonData = json.load(jsonFile)

#lists to perform calculations on
allLoanAmount = []
allSubjectAppraisedAmount = []
allInterestRate = []

for i in jsonData:
    #fill the lists with data from the json
    allLoanAmount.append(i['LoanAmount'])
    allSubjectAppraisedAmount.append(i['SubjectAppraisedAmount'])
    allInterestRate.append(i['InterestRate'])

#sorted for the median
allLoanAmount.sort()
allSubjectAppraisedAmount.sort()
allInterestRate.sort()

monthlySummary = {
    "LoanAmountSummary": {
        "Sum": '{:.2f}'.format(sum(allLoanAmount)),
        "Average": '{:.2f}'.format(sum(allLoanAmount)/len(allLoanAmount)),
        "Median": '{:.2f}'.format(statistics.median(allLoanAmount)),
        "Minimum": '{:.2f}'.format(min(allLoanAmount)),
        "Maximum": '{:.2f}'.format(max(allLoanAmount))
    },
	"SubjectAppraisedAmountSummary": {	
		"Sum": '{:.2f}'.format(sum(allSubjectAppraisedAmount)),
		"Average": '{:.2f}'.format(sum(allSubjectAppraisedAmount)/len(allSubjectAppraisedAmount),"2f"),
		"Median": '{:.2f}'.format(statistics.median(allSubjectAppraisedAmount)),
		"Minimum": '{:.2f}'.format(min(allSubjectAppraisedAmount)),
		"Maximum": '{:.2f}'.format(max(allSubjectAppraisedAmount)),
	},
	"InterestRateSummary": {	
		"Sum": '{:.2f}'.format(sum(allInterestRate)),
		"Average": '{:.2f}'.format(sum(allInterestRate)/len(allInterestRate)),
		"Median": '{:.2f}'.format(statistics.median(allInterestRate)),
		"Minimum": '{:.2f}'.format(min(allInterestRate)),
		"Maximum": '{:.2f}'.format(max(allInterestRate)),
	}    
}

#create the json file 
monthlySummaryObject = json.dumps(monthlySummary, indent = 5)

with open("monthlySummary.json", "w") as outfile:
    outfile.write(monthlySummaryObject)

#PART 2 of the coding challenge
allSubjectState = []

for i in jsonData:
    #populate the list of all states in json
    if not i['SubjectState'] in allSubjectState:
        allSubjectState.append(i['SubjectState'])
        
monthlyByState = {}


for i in allSubjectState:
    #lists of calculation for each state, reset upon finishing calculation for each state
    allStateLoanAmount = []
    allStateSubjectAppraisedAmount = []
    allStateInterestRate = []

    #go through each state in the json to calculate the lists
    for j in jsonData:
        if j['SubjectState'] == i:
            allStateLoanAmount.append(j['LoanAmount'])
            allStateSubjectAppraisedAmount.append(j['SubjectAppraisedAmount'])
            allStateInterestRate.append(j['InterestRate'])

    allStateLoanAmount.sort()
    allStateSubjectAppraisedAmount.sort()
    allStateInterestRate.sort()

    monthlyByState.update(
        {i:{
            "LoanAmmountSummary": {	
                "Sum": '{:.2f}'.format(sum(allStateLoanAmount)),
                "Average": '{:.2f}'.format(sum(allStateLoanAmount)/len(allStateLoanAmount)),
                "Median": '{:.2f}'.format(statistics.median(allStateLoanAmount)),
                "Minimum": '{:.2f}'.format(min(allStateLoanAmount)),
                "Maximum": '{:.2f}'.format(max(allStateLoanAmount))
            },
            "SubjectAppraisedAmountSummary": {	
                "Sum": '{:.2f}'.format(sum(allStateSubjectAppraisedAmount)),
                "Average": '{:.2f}'.format(sum(allStateSubjectAppraisedAmount)/len(allStateSubjectAppraisedAmount),"2f"),
                "Median": '{:.2f}'.format(statistics.median(allStateSubjectAppraisedAmount)),
                "Minimum": '{:.2f}'.format(min(allStateSubjectAppraisedAmount)),
                "Maximum": '{:.2f}'.format(max(allStateSubjectAppraisedAmount)),
            },
            "InterestRateSummary": {	
                "Sum": '{:.2f}'.format(sum(allStateInterestRate)),
                "Average": '{:.2f}'.format(sum(allStateInterestRate)/len(allStateInterestRate)),
                "Median": '{:.2f}'.format(statistics.median(allStateInterestRate)),
                "Minimum": '{:.2f}'.format(min(allStateInterestRate)),
                "Maximum": '{:.2f}'.format(max(allStateInterestRate)),
                    }
                }
        }
    )

#create the json file 
monthlyByStateObject = json.dumps(monthlyByState, indent = 5)

with open("monthlyByState.json", "w") as outfile:
    outfile.write(monthlyByStateObject)