import csv, math, learn
(pr_c1, pr_c2) = learn.solve_prior()
(terms_c1, terms_c2) = learn.solve_condprob_dis()
(exp_c1, exp_c2, var_c1, var_c2) = learn.solve_condprob_con()
def classify():
    res = []
    with open('./data/test.csv', 'rb') as csvfile:
        line_num = 0
        reader = csv.reader(csvfile)
        for row in reader:
            #print line_num
            r_len = len(row)
            line_num += 1
            if line_num == 1:
                continue
            score_c1 = math.log(pr_c1)
            score_c2 = math.log(pr_c2)
            for i in range(0, r_len - 1):
                #discrete
                if i < r_len - 4:
                    score_c1 += float(row[i]) * math.log(terms_c1[i])
                    score_c2 += float(row[i]) * math.log(terms_c2[i])
                #continuous
                else:
                    log_pr1 = -1/2 * math.log(2*math.pi*var_c1[i-r_len+4])\
                            - math.pow(float(row[i]) - exp_c1[i-r_len+4], 2)\
                            / (2*var_c1[i-r_len+4])
                    score_c1 += log_pr1
                    log_pr2 = -1/2 * math.log(2*math.pi*var_c2[i-r_len+4])\
                            - math.pow(float(row[i]) - exp_c2[i-r_len+4], 2)\
                            / (2*var_c2[i-r_len+4])
                    score_c2 += log_pr2
            print score_c1, score_c2
            if score_c1 >= score_c2:
                res.append(1)
            else:
                res.append(0)
    return res
res = classify()
for ele in res:
    print ele,
