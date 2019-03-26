digits = input()
dig_dict = dict()
for i in range(10):
    dig_dict[i] = 0
for d in digits:
    dig_dict[int(d)] += 1
zero_freq = dig_dict[0]
min_num_dig = min([dig_dict[i] for i in range(1, 10)])
min_dig = min([k for k in range(1, 10) if dig_dict[k] == min_num_dig])
#print("freq_of_min_dig: " + str(min_num_dig))
#print("min_digit: " + str(min_dig))
#print("zero_freq: " + str(zero_freq))
#IF ZER_FREQ < FREQ_OF_MIN_DIGIT, use 0
#else use min_digit
if zero_freq < min_num_dig:
    print("1" + "0" * (zero_freq + 1))
else:
    print(str(min_dig) * (min_num_dig + 1))
