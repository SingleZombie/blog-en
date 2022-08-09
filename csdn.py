import os

cfgs = [
    # 'https://zhouyifan.net/2022/06/15/DLS-note-6/',
    #'https://zhouyifan.net/2022/06/21/DLS-note-7/',
    #'https://zhouyifan.net/2022/06/27/DLS-note-7-2/',
    #'https://zhouyifan.net/2022/06/27/DLS-note-summary-2/',
    #'https://zhouyifan.net/2022/07/01/20220701-pytorchinstall2/',
    #'https://zhouyifan.net/2022/07/01/20220625-stylegan-introduction/',
    #'https://zhouyifan.net/2022/07/03/DLS-note-8/',
    #'https://zhouyifan.net/2022/07/04/DLS-note-9/',
    #'https://zhouyifan.net/2022/07/08/20220707-ZeroDCE/'
    'https://zhouyifan.net/2022/07/10/DLS-note-summary-3/',
    'https://zhouyifan.net/2022/07/11/DLS-note-10/',
    'https://zhouyifan.net/2022/07/24/DLS-note-10-2/',
    'https://zhouyifan.net/2022/07/24/DLS-note-10-3/',
    'https://zhouyifan.net/2022/07/24/DLS-note-10-4/',
    'https://zhouyifan.net/2022/07/24/DLS-note-10-5/',
    'https://zhouyifan.net/2022/07/24/DLS-note-11/',
    'https://zhouyifan.net/2022/07/24/DLS-note-11-2/',
    'https://zhouyifan.net/2022/07/26/DLS-note-12/',
    'https://zhouyifan.net/2022/08/09/DLS-note-12-2/',
    'https://zhouyifan.net/2022/08/09/DLS-note-13/'
]

for link in cfgs:
    md_file = link.split('/')[-2] + '.md'
    md_path = os.path.join('_posts', md_file)
    o_path = os.path.join('tmp', md_file)
    if os.path.exists(o_path):
        continue
    with open(o_path, 'wb') as wfp:
        with open(md_path, 'rb') as fp:
            lines = fp.readlines()
            for i, line in enumerate(lines):
                line = line.decode('UTF-8')
                if line[0] == '!' and line[1] == '[':
                    origin_str = line.split('(')[1][0:-1]
                    subdir_name = origin_str.split('/')[0]
                    new_str = origin_str.replace(subdir_name, link[0:-1])
                    line = line.replace(origin_str, new_str)
                    # print(origin_str, new_str)
                    lines[i] = line.encode('UTF-8')

            wfp.writelines(lines)
