samp_string = "This is a very important string"

print("Length: ", len(samp_string))

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])