import csv, types
def solve_prior():
    with open('./data/train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        col = [row[57] for row in reader]
    pr_c1 = 0
    for ele in col:
        if ele == '1':
            pr_c1 += 1
    # is_spam cannot be included
    pr_c1 /= float(len(col) - 1)
    #print pr_s
    pr_c2 = 1 - pr_c1
    return pr_c1, pr_c2

#discrete
def solve_condprob_dis():
    terms_c1 = []
    terms_c2 = []
    with open('./data/train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        line_num = 0
        for row in reader:
            r_len = len(row)
            if line_num == 0:
                for i in range(0, r_len - 4):
                    terms_c1.append(0)
                    terms_c2.append(0)
            else:
                for i in range(0, r_len - 4):
                    if row[r_len - 1] == '1':
                        terms_c1[i] += float(row[i])
                    else:
                        terms_c2[i] += float(row[i])
            line_num += 1
    total_c1 = 0
    total_c2 = 0
    for i in range(0, len(terms_c1)):
        total_c1 += terms_c1[i]
        total_c2 += terms_c2[i]
    # normalize terms_c1 terms_c2
    for i in range(0, len(terms_c1)):
        terms_c1[i] /= total_c1
        terms_c2[i] /= total_c2
    return terms_c1, terms_c2

#continuous
def solve_condprob_con():
    expect_c1 = []
    expect_c2 = []
    variance_c1 = []
    variance_c2 = []
    #expectation
    with open('./data/train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        line_num = 0
        c1_cnt = 0
        c2_cnt = 0
        for row in reader:
            r_len = len(row)
            if line_num == 0:
                for i in range(r_len - 4, r_len - 1):
                    expect_c1.append(0)
                    expect_c2.append(0)
            else:
                for i in range(r_len - 4, r_len - 1):
                    if row[r_len - 1] == '1':
                        expect_c1[i-r_len+4] += float(row[i])
                    else:
                        expect_c2[i-r_len+4] += float(row[i])
                if row[r_len - 1] == '1':
                    c1_cnt += 1
                else:
                    c2_cnt += 1
            line_num += 1
        for i in range(0, 3):
            expect_c1[i] /= c1_cnt
            expect_c2[i] /= c2_cnt
    #variance
    with open('./data/train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        line_num = 0
        for row in reader:
            if line_num == 0:
                for i in range(r_len - 4, r_len - 1):
                    variance_c1.append(0)
                    variance_c2.append(0)
            else:
                for i in range(r_len - 4, r_len - 1):
                    if row[r_len - 1] == '1':
                        diff = float(row[i]) - expect_c1[i-r_len+4]
                        variance_c1[i-r_len+4] += diff * diff
                    else:
                        diff = float(row[i]) - expect_c2[i-r_len+4]
                        variance_c2[i-r_len+4] = diff * diff
            line_num += 1
        #print "!!!!!", c1_cnt, c2_cnt
        for i in range(0, 3):
            variance_c1[i] /= (c1_cnt - 1)
            variance_c2[i] /= (c2_cnt - 1)
    return expect_c1, expect_c2, variance_c1, variance_c2

#call function
(t1, t2) = solve_condprob_dis()
(e1, e2, v1, v2) = solve_condprob_con()
for ele in t1:
    print ele,
print "end of terms_c1#######################\n"
#for ele in
for ele in e1:
    print ele,
print "end of expect_c1######################\n"
for ele in v1:
    print ele,
print "end of variance_c1####################\n"
for ele in e2:
    print ele,
print "end of expect_c2######################\n"
for ele in v2:
    print ele,
print "end of variance_c2####################\n"
