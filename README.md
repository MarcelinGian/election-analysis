# election-analysis
## Election Audit Overview
#### The purpose of this election audit analysis is to use the csv data file to better understand the turnout & results of the election. This includes information such as the total voter turnout, the distribution of votes across the three candidates, the distribution of votes across three counties, and the winner of the election- including how many votes the winner recieved and the percentage of votes the winner garnered.

## Election Audit Results
- 369, 711 votes in total were cast in the election.

- The following is a breakdown of the number of votes and the percentage of total votes for the 3 counties in the precient:
  - Jefferson County: 38, 855 votes cast. 10.5% of the total votes for the election.
  - Denver County: 306, 055 votes cast. 82.8% of the total votes for the election.
  - Arapahoe County: 24, 801 votes cast. 6.7% of the total votes for the election.
  
- Denver County had the largest number of votes.

- The following is a breakdown of the number of votes and the percentage of total votes for the 3 candidates in this election:
  - Charles C. Stockholm: Candidate received 85, 213 votes, this was 23% of total votes cast.
  - Diane DeGette: Candidate received 272, 892 votes, this was 73.8% of total votes cast.
  - Raymon A. Doane: Candidate received 11, 606 votes, this was 3.1% of total votes cast.
 
- Diane DeGette was the winner of the election. With a total of 272, 892 cast for her, she was favored by 73.8% of the electorate.

### See Analysis Summary below
  
![Screen Shot 2022-06-15 at 9 52 34 PM](https://user-images.githubusercontent.com/105818879/173994603-40e6a456-a166-4b84-93c6-eaa5592b317c.png)


## Election Audit Summary
#### This is a versitle script that can be used, with some modifications, for any election. For example:
- With the information already available in the "election_results.csv" file, we can see the distribution of votes by csndidate within a specific county. Charles C. Stockholm may have won the majority of votes in Jefferson & Arapahoe counties but still lost the election because Diane DeGette was heavily favored in Denver County.
- For smaller elections within a county, where votes are distributed across districts, we can easily substitue disctrict information in place of our county-specific for loop.
