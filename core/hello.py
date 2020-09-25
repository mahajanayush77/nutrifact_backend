# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import re
import json


def change_to_g(text):
    search_ln = re.search("\d\s|\d$", text)
    if search_ln and search_ln.group().strip() == "9":
        index = search_ln.span()[0]
        text = text[:index] + "g" + text[index + 1:]

    search_lnq = re.search("\dmq\s|\dmq$", text)
    if search_lnq:
        index = search_lnq.span()[0] + 2
        text = text[:index] + "g" + text[index + 1:]
    return text

# Removes all the unnecessary noise from a string


def clean_string(string):
    pattern = "[\|\*\_\'\—\-\{}]".format('"')
    text = re.sub(pattern, "", string)
    text = re.sub(" I ", " / ", text)
    text = re.sub("^I ", "", text)
    text = re.sub("OMG", "0MG", text)
    text = re.sub("OG", "0G", text)
    text = re.sub('(?<=\d) (?=\w)', '', text)
    text = change_to_g(text)
    text = text.strip()
    return text


# %%

def return_string(string):
    global list

    blocks = string.split('###')
    elements = list(map(lambda x: x.split('~'), blocks))

    # removing [['']]
    elements = list(
        map(lambda x: list(filter(lambda a: a != '', x)), elements))
    # removig [[]]
    elements = list(filter(lambda x: x != [], elements))

    # converting 09 to 0g
    elements = list(
        map(lambda x: list(map(lambda a: clean_string(a), x)), elements))
    # elements
    # Check for caffeine
    hasCaffeine = False
    for i in elements:
        for j in i:
            if j.upper().find("CONTAINS CAFFEINE".upper()) != -1:
                hasCaffeine = True
            elif j.upper().find("CAFFEINE FREE".upper()) != -1:
                hasCaffeine = False
        # print(hasCaffeine)

        # Check for natural colour
    hasColour = False
    for i in elements:
        for j in i:
            if j.upper().find("PERMITTED NATURAL".upper()) != -1:
                hasColour = True
    # print(hasColour)
    # check for added flavours
    hasFlavour = False
    for i in elements:
        for j in i:
            if j.upper().find("ADDED FLAVOURS".upper()) != -1:
                hasFlavour = True
    # print(hasFlavour)
    nn = "NIACIN###TOTAL CARB###GRASA SATURADA###MONOUNSATURATED FAT###PROTEIN###PROTEINAS###CHOLESTEROL###ENERGY###FIBRE###CALORIES###SALT###VITAMIN D###VITAMIN C###OTHER CARBOHYDRATE###SEL###ZINC###LIPIDES###MAGNESIUM###THIAMIN###CARB###CALORIES FROM FAT###GLUCIDES###DIETARY FIBER###ENERGIA###SODIUM###IRON###SATURÉS###CARBOHYDRATE###SUGAR###GRAISSES SATURÉES###TOTAL CARBOHYDRATE###POTASSIUM###FAT###SUCRES###TRANS FAT###TOTAL FAT###PROTEINES###FOLIC###SOLUBLE FIBER###FIBRES###CAFFEINE###PROTÉINES###MATIÈRES GRASSES###CHO###POLYUNSATURATED FAT###VITAMIN A###SATURATED FAT###CALCIUM###FIBER###SUGARS###TOTAL CARB.###RIBOFLAVIN###"
    ing = "carbonated water###sugar###acidity regulator###caffeine###citric acid###".upper()
    # creating the nutrients set
    # with open('../data/nutrients.txt', 'r') as f:
    #     ss = f.read()
    #     nutrients = set(map(lambda x: x.upper(), ss.split('\n')))
    nutrients = nn.split('###')
    nutrients.remove('')
    ingredients = ing.split('###')
    ingredients.remove('')
    # print(ingredients)
    nut = []
    units = ['KCAL', 'CAL', 'MG', 'G']
    for n in nutrients:
        for i in elements:
            for j in i:
                if j.upper().find(n + ':') != -1 or j.upper().find(n + ' ') != -1:
                    if n == 'FAT' and j.upper().find(' ' + n) != -1:
                        continue
                    # print(j)
                    quan = list(map(int, re.findall(r'\d+', j)))
                    if len(quan) != 0:
                        flag = False
                        firstIndex = j.find(str(quan[0]))
                        lastIndex = firstIndex + len(str(quan[0]))
                        temp_units = j[lastIndex:lastIndex + 5]

                        # replace print to add data to dictionary or

                        for u in units:
                            if temp_units.find(u) != -1:
                                nut.append([n.title(), str(quan[0]), u.lower()])

                                flag = True
                                break
                        if flag:
                            continue
                        if n == "ENERGY":

                            # nut.append("{}: {}kcal".format(n.title(), quan[0]))
                            nut.append([n.title(), str(quan[0]), 'kcal'])
                        elif n == 'SODIUM':
                            nut.append([n.title(), str(quan[0]), 'mg'])
                            # nut.append("{}: {}mg".format(n.title(), quan[0]))
                        else:
                            nut.append([n.title(), str(quan[0]), 'g'])
                            # nut.append("{}: {}g".format(n.title(), quan[0]))



    list_ingredient = []
    for i in ingredients:
        for j in elements:
            for k in j:
                if k.upper().find(i) != -1:
                    if i not in list_ingredient:
                        list_ingredient.append(i)
    if (hasColour):
        list_ingredient.append('CONTAINS PERMITTED NATURAL COLOURS')
    if (hasFlavour):
        list_ingredient.append('CONTAINS ADDED FLAVOURS')
    # print (list)






    # print(hasCaffeine)
    mfg = ""
    for i in elements:
        for j in i:
            if j.upper().find("pvt".upper()) != -1:
                mfg = j

    quantity = ""
    for i in elements:
        for j in i:
            if j.upper().find("ML".upper()) != -1:
                quantity = j

    # jsonNut = json.dumps(nut, indent=4)
    # jsonIng = json.dumps(list, indent=4)

    data = {
        'Manufactured By': mfg,
        'Quantity': quantity,
        'Caffeine': hasCaffeine,
        'nutrient': nut,
        'ingredients':list_ingredient,
    }

    print(data)
    return data

# %%
