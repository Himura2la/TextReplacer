f = open("input.txt", encoding='utf-8')
inp = f.read()
f.close()

f = open("rules.txt", encoding='utf-8')
rawRules = f.read()
f.close()

rawRulesList = rawRules.split("\n")

# Parsing settings

if rawRules.find("I am Comment") > 0:
    commentSign = rawRules.split("I am Comment")[0].split("\n")[-1]
    print("Comment Sign: '" + commentSign + "'")
    rawRulesList = list(filter(lambda a: a.find(commentSign) != 0, rawRulesList))

# print(rawRulesList)

marker = rawRulesList[0]
print("Split Marker: '" + marker + "'")
del rawRulesList[0]

bounds_markers = rawRulesList[0]
if bounds_markers.count(marker) == 3:
    bounds_markers = bounds_markers.split(marker)
    prefix_marker = marker + bounds_markers[1] + marker
    postfix_marker = marker + bounds_markers[2] + marker
    print("Prefix Marker: '" + prefix_marker + "'")
    print("Postfix Marker: '" + postfix_marker + "'")
    bounds_markers = True
    del rawRulesList[0]
else:
    bounds_markers = False

print("---")  # Parsing rules

rulesList = []
global_prefix, global_postfix = '', ''

for rawRule in rawRulesList:
    if bounds_markers and rawRule.find(prefix_marker) >= 0:
        global_prefix = rawRule.split(prefix_marker)[1]
    if bounds_markers and rawRule.find(postfix_marker) >= 0:
        global_postfix = rawRule.split(postfix_marker)[1]
    if rawRule.find(marker) > 0:
        rulesList.append(rawRule.split(marker))

if global_prefix and bounds_markers:
    print('prefix:', global_prefix)
[print(rule) for rule in rulesList]
if global_postfix and bounds_markers:
    print('postfix:', global_postfix)


def esc_seq(s):
    return s.replace("\\n", "\n").replace("\\t", "\t")

# Replacing

output = inp

for rule in rulesList:
    rule[0] = esc_seq(rule[0])
    rule[1] = esc_seq(rule[1])
    output = output.replace(rule[0], rule[1])

if bounds_markers:
    output = esc_seq(global_prefix) + output + esc_seq(global_postfix)

f = open("output.txt", 'w', encoding='utf-8')
f.write(output)
f.close()


print("---\nDone! catch your output.txt\n\n")