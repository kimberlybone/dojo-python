# Given a mapping:
# 'a' => 1
# 'b' => 2
# 'c' => 3
# ...
# 'z' => 26

# When you are given this mapping, you can convert it to a str.
# Can you write a fxn that takes @data as input & returns the number of messages that could of been the original message OR how many ways are there to decode this message back to the original message?
# For ex:

# Input 
#   @data = '12'

# Run num_ways(data)

# Output is 2

# Explanation
#   'ab' => '12'
#   'l' => '12'
#   There are 2 messages that can be encoded into 12 which are 'ab' & 'l'

# num_ways("3") = 1 ==> 'c'
# num_ways("") = 1 ==> ''
# num_ways("011") = 0 ==> No letter maps to 0 or 01
# @data = string, @k = non-negative integer that represents the last k letters of data
def helper(data, k, memo):
    startIndex = data.length - k
    if k == 0:
        return 1

    if data[startIndex] == 0:
        return 0

    if memo[k] != None:
        return memo[k]
    result = helper(data, k-1, memo)

    if k >= 2 and int(data[startIndex:startIndex+2]) <= 26:
        result += helper(data, k-2, memo)
    memo[k] = result
    return result


def num_ways(data):
    memo = []
    memo = int[data.length + 1]
    return helper(data, data.length, memo)