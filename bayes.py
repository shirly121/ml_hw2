import csv, types
def solve_prior:
    with open('train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        col = [row[57] for row in reader]
    global pr_c1
    pr_c1 = 0
    for ele in col:
        if ele == '1':
            pr_c1 += 1
    # is_spam cannot be included
    pr_c1 /= float(len(col) - 1)
    #print pr_s
    global pr_c2 = 1 - pr_c1
    print pr_c2

#discrete
def solve_condprob_dis:
    terms_c1[], terms_c2[]
    with open('train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        line_num = 0
        r_len = len(row)
        for row in reader:
            if line_num == 0:
                for i in range(0, r_len - 4):
                    terms_c1[i] = 0
                    terms_c2[i] = 0
            else
                for i in range(0, r_len - 4):
                    if row(r_len - 1) == '1':
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

#continuous
def solve_condprob_con:
    expect_c1[], expect_c2[]
    variance_c1[], variance_c2[]
    with open('train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        line_num = 0
        r_len = len(row)
        c1_cnt = 0
        c2_cnt = 0
        for row in reader:
            if line_num == 0:
                for i in range(r_len - 4, r_len - 1):
                    expect_c1[i] = 0
                    expect_c2[i] = 0
            else:
                for i in range(r_len - 4, r_len - 1):
                    if(row(r_len - 1) == '1'):
                        expect_c1[i] += row[i]
                        c1_cnt += 1
                    else:
                        expect_c2[i] += row[i]
                        c2_cnt += 1
            line_num += 1
    for i in range(r_len - 4, r_len - 1):
        expect_c1[i] /= c1_cnt
        expect_c2[i] /= c2_cnt
    #variance














