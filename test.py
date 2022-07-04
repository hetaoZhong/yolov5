import torch
import json

if __name__ == '__main__':

    print(torch.__version__)
    print(torch.cuda.is_available())
    class_dict = {}
    class_list = class_dict.get(0)
    if class_list is None:
        class_list = []
    class_list.append('sssssss')
    class_dict[0] = class_list
    print(json.dumps(class_list, ensure_ascii=False).encode())
    print(json.dumps(class_dict))
