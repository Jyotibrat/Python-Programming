# File paths
file_path_A = "E:/VS Code Programs/VS Code Programs/Jupyter Notebook/Exam Practice/End Term Practice/A.txt"
file_path_B = "E:/VS Code Programs/VS Code Programs/Jupyter Notebook/Exam Practice/End Term Practice/B.txt"
file_path_C = "E:/VS Code Programs/VS Code Programs/Jupyter Notebook/Exam Practice/End Term Practice/C.txt"

data_of_A = ""
data_of_B = ""

with open(file_path_A, "r") as file_A:
    
    for i in range(5):
        line = file_A.readline()
        if line:
            print(line.strip())
        else:
            break

print()
with open(file_path_A, "r") as file_A:
    data_of_A = file_A.read()    

with open(file_path_B, "r") as file_B:
    data_of_B = file_B.read()

with open(file_path_C, "a") as file_C:
    file_C.write(data_of_A+"\n"+data_of_B)

print()
with open(file_path_C, "r") as file_C:
    print("/nContent of B.txt after writing:")
    print(file_C.read())