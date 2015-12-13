import json
PART = 1
def sumNums(obj):
    return sum( val if isinstance(val,int) else (
        sumNums(val)*(PART!=2 or not (isinstance(val,dict) and "red" in val.values()))
        if isinstance(val, (dict,list)) else 0) for val in (obj.values() if
        isinstance(obj, dict) else obj ))

print(sumNums(json.loads(open('a12.in').read())))
