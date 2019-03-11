with open("train.wp_source") as file: # Use file to refer to the file object
    prompt = file.readlines()
with open("train.wp_target") as file: # Use file to refer to the file object
    response = file.readlines()
compiled=""
for i in range(10000):
    compiled+=prompt[i]+" [WP-START] "+response[i]+" [WP-END] "
f = open("train_10000.txt", "w")
    f.write(compiled)
f.close()