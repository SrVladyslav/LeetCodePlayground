""" 
Given a list of people and their schedules, return a final schedule that shows the start and end times, with the respective people on schedule.

Example:
Input

roster = [
    ["Mary", 10, 40],
    ["John", 30, 50],
    ["Peter", 50, 80],
    ["Crystal", 100, 150],
    ["Jane", 120, 180]
]
Output

res = [
    [10, 30, ["Mary"]],
    [30, 40, ["Mary", "John"]],
    [40, 50, ["John"]],
    [50, 80, ["Peter"]],
    [80, 100, []],
    [100, 120, ["Crystal"]],
    [120, 150, ["Crystal", "Jane"]],
    [150, 180, ["Jane"]]
]
"""

def find_order(roster: list[list[str, int, int]]) -> list[list[int,int,list[str]]]:
    
