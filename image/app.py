import os

def list_all_objects(startpath):
    for root, dirs, files in os.walk(startpath):
        for directory in dirs:
            print(os.path.join(root, directory))  # Thư mục
        for file in files:
            print(os.path.join(root, file))  # Tệp tin
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.islink(path):
                print(path)  # Liên kết tượng trưng

# Thay đổi 'path_to_folder' thành đường dẫn tới thư mục bạn muốn liệt kê
#path_to_folder = 'c:/WorkSpace/GitHub/Working/aws-study-group/github-page/hoangguruu.github.io/image/2.prerequiste/2.1.accesskey/'
path_to_folder = 'c:/WorkSpace/GitHub/Working/aws-study-group/github-page/hoangguruu.github.io/image/1.introduce/'
list_all_objects(path_to_folder)
