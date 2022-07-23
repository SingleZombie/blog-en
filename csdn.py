import os

cfgs = [
    # 'https://zhouyifan.net/2022/06/15/DLS-note-6/',
    'https://zhouyifan.net/2022/06/21/DLS-note-7/',
    'https://zhouyifan.net/2022/06/27/DLS-note-7-2/',
    'https://zhouyifan.net/2022/06/27/DLS-note-summary-2/',
    'https://zhouyifan.net/2022/07/01/20220701-pytorchinstall2/',
    'https://zhouyifan.net/2022/07/01/20220625-stylegan-introduction/',
    'https://zhouyifan.net/2022/07/03/DLS-note-8/',
    'https://zhouyifan.net/2022/07/04/DLS-note-9/',
    'https://zhouyifan.net/2022/07/08/20220707-ZeroDCE/'
]

for link in cfgs:
    md_file = link.split('/')[-2] + '.md'
    md_path = os.path.join('_posts', md_file)
    o_path = os.path.join('tmp', md_file)
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
