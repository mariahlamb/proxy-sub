import os
import requests

# 文件路径
sub_folder = 'sub'
sub_file = os.path.join(sub_folder, 'sub_all_clash.txt')
output_file = 'all_nodes.txt'

if os.path.exists(sub_file):
    with open(sub_file, 'r') as f:
        subscriptions = f.readlines()

    with open(output_file, 'w') as out_f:
        for url in subscriptions:
            url = url.strip()
            if url:
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    
                    # 写入响应的文本内容，每个文件内容其行再拆分写入
                    nodes = response.text.strip().split('\n')
                    for node in nodes:
                        out_f.write(f'{node.strip()}\n')
                        
                except requests.RequestException as e:
                    print(f'Failed to fetch {url}: {e}')

    print(f'节点信息已更新到：{output_file}')
else:
    print(f'未找到 {sub_file} 文件，跳过生成步骤。')
