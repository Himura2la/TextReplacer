import io

f = open("input.txt")
t = f.read()
f.close()

f = open("rules.txt")
rawRules = f.read()
f.close()

rawRulesList = rawRules.split("\n")

if rawRules.find("I am Comment") > 0:
	commentSign = rawRules.split("I am Comment")[0].split("\n")[-1]
	print("Comment Sign: '" + commentSign + "'")
	rawRulesList.remove(commentSign + "I am Comment")
	for rawRule in rawRulesList:
		if rawRule.find(commentSign) == 0:
			rawRulesList.remove(rawRule)

print(rawRulesList)

marker = rawRulesList[0].split("\n")[0]
print("Marker: '" + marker + "'")

rulesList=[]
for rawRule in rawRulesList:
	if rawRule.find(marker) > 0:
		rulesList.append(rawRule.split(marker))

print(rulesList)

r = t
for rule in rulesList:
	rule[0] = rule[0].replace("\\n","\n").replace("\\t","\t")
	rule[1] = rule[1].replace("\\n","\n").replace("\\t","\t")
	r = r.replace(rule[0], rule[1])

f = open("output.txt", 'w')
f.write(r)
f.close()

print("Done! catch your output.txt")