import json
def end(a):
    if "code" in a or "example" in a or a == "},\n" or a == "}\n":
        return True
    return False

def main():
    line_vec = []
    with open ('./linear_algebra.v4.json') as f:
        for line in (f):
            line_vec.append(line)
            # print(line == "\n")   

    # ans = {}
    ans = []
    instruction = ''
    output = ''
    max_ = 0
    for i in range(len(line_vec)):
        line = line_vec[i]
        if "instruction" in line:
            if i > 0:
                # ans[instruction] = {"question":instruction, "output":output}
                ans.append({"question":instruction, "output":output})
                if len(output) > max_:
                    max_ = len(output)
                # break
                # if instruction == "什么是矩阵的行列式？" : break
            pos = line.find("instruction")+len("instruction")+3
            if line[pos] == "\"": pos += 1
            instruction = line[pos: line.rfind("\"")]
            output = ""

        elif "output" in line or "code" in line or "example" in line:
            head = "output" if "output" in line else "code" if "code" in line else "example"
            if i+1 < len(line_vec) and not end(line_vec[i+1]):
                output += line[line.find(head)+len(head)+4:]
                i += 1
                while(i+1 < len(line_vec) and not end(line_vec[i+1])):
                    output += line_vec[i]
                    i += 1
                if i+1 < len(line_vec):
                    output += line_vec[i][0: line_vec[i].rfind("\"")] + "\n"
                    # print(line_vec[i], line_vec[i][0: line_vec[i].rfind("\"")])
                i += 1
            else:
                output += line[line.find(head)+len(head)+4: line.rfind("\"")] + "\n"
    # ans[instruction] = output
    ans.append({"question":instruction, "output":output})

    # print(ans['以二阶方阵为例，说明各种不同的方阵，对应的线性变换：旋转、缩放、关于x轴对称，关于y轴对称，关于原点对称，关于x轴(y轴)剪切；给出python 代码与几何示例'])
    # for k,v in ans.items():
        # print("key",k)
        # print("value",v)
        # break
    print(max_)
    with open ("db.json",'w') as f:
        json.dump(ans, f, indent = 4, ensure_ascii=False)
            

if __name__ == "__main__":
    main()

    # test = "  \"output\": \"\n"
    # print(test[test.find("output")+6+4:])

    # test = "    \"instruction\": \"矩阵和现在人工智能中的“张量”概念有什么联系？\n"
    # print(test[test.find("instruction")+11+4: test.rfind("\"")])
