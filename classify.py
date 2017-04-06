import csv, math, learn
(pr_c1, pr_c2) = learn.solve_prior()
(terms_c1, terms_c2) = learn.solve_condprob_dis()
(exp_c1, exp_c2, var_c1, var_c2) = learn.solve_condprob_con()
def classify():
    res = []
    real = []
    with open('./data/test.csv', 'rb') as csvfile:
        line_num = 0
        reader = csv.reader(csvfile)
        for row in reader:
            #print line_num
            r_len = len(row)
            line_num += 1
            if line_num == 1:
                continue
            real.append(int(row[r_len - 1]))
            score_c1 = math.log(pr_c1)
            score_c2 = math.log(pr_c2)
            for i in range(0, r_len - 1):
                ##discrete
                #if i < r_len - 4:
                #    score_c1 += float(row[i]) * math.log(terms_c1[i])
                #    score_c2 += float(row[i]) * math.log(terms_c2[i])
                #continuous
                #elif i == r_len - 4 or i == r_len - 3:
                if i >= r_len - 4:
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
    accuracy = 0
    for i in range(0, len(real)):
        if real[i] == res[i]:
            accuracy += 1
    accuracy /= float(line_num - 1)
    return accuracy, res
(accuracy, res) = classify()
print accuracy
for ele in res:
    print ele,
