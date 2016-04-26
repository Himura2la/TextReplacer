f = open("input.txt")
t = f.read()
f.close()

f = open("rules.txt")
rawRules = f.read()
f.close()

rawRulesList = rawRules.split("\n")

# Parsing settings

if rawRules.find("I am Comment") > 0:
    commentSign = rawRules.split("I am Comment")[0].split("\n")[-1]
    print("Comment Sign: '" + commentSign + "'")
    rawRulesList.remove(commentSign + "I am Comment")
    for rawRule in rawRulesList:
        if rawRule.find(commentSign) == 0:
            rawRulesList.remove(rawRule)
#print(rawRulesList)

marker = rawRulesList[0]
print("Marker: '" + marker + "'")
del rawRulesList[0]

bounds_markers = rawRulesList[0]
if bounds_markers.count(marker) == 3:
    bounds_markers = bounds_markers.split(marker)
    prefix_marker = marker + bounds_markers[1] + marker
    postfix_marker = marker + bounds_markers[2] + marker
    print("Prefix: '" + prefix_marker + "'")
    print("Postfix: '" + postfix_marker + "'")
    bounds_markers = True
    del rawRulesList[0]
else:
    bounds_markers = False

print("---")  # Parsing rules

rulesList=[]
for rawRule in rawRulesList:
    if bounds_markers and rawRule.find(prefix_marker) >= 0:
        prefix = rawRule.split(prefix_marker)[1]
    if bounds_markers and rawRule.find(postfix_marker) >= 0:
        postfix = rawRule.split(postfix_marker)[1]
    if rawRule.find(marker) > 0:
        rulesList.append(rawRule.split(marker))

if bounds_markers: print(prefix)
print(rulesList)
if bounds_markers: print(postfix)

def esc_seq(s): return s.replace("\\n","\n").replace("\\t","\t")

# Replacing

r = t
for rule in rulesList:
    rule[0] = esc_seq(rule[0])
    rule[1] = esc_seq(rule[1])
    r = r.replace(rule[0], rule[1])

r = esc_seq(prefix) + r + esc_seq(postfix)

f = open("output.txt", 'w')
f.write(r)
f.close()


print("---\nDone! catch your output.txt\n\n")