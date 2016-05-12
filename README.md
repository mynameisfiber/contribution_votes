# Exploration Into Political Contributions

- [x] Read in contribution data ([contributions.py](contributions.py))
- [x] Read in legislator metadata ([legistlators.py](legistlators.py))
    - Code written and it works, but numbers seem a bit lot... why??
- [ ] Read in votes data ([votes.py](votes.py))
- [ ] Correlate honorees in contributions to legislators in voting data
    - Votes data uses the `bioguide` id which we index on in [legistlators.py](legistlators.py)
    - We'll need to do fuzzy searching... maybe remove common phrases (senator,
      sen., sir, ms, etc..) and then do best edit distance?
