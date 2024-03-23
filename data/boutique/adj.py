import numpy as np

# 定义微服务列表
services = ["adservice", "cartservice", "checkoutservice", "currencyservice", "emailservice", "frontend",
            "paymentservice", "productcatalogservice", "recommendationservice", "shippingservice"]

# 定义微服务之间的关系
relations = {
    "frontend": ["adservice", "recommendationservice", "productcatalogservice", "cartservice", "shippingservice",
                 "currencyservice", "checkoutservice"],
    "checkoutservice": ["paymentservice", "emailservice", "shippingservice", "currencyservice", "cartservice",
                        "productcatalogservice"],
    "recommendationservice": ["productcatalogservice"]
}

# 创建邻接矩阵
adjacency_matrix = np.zeros((len(services), len(services)), dtype=float)
for i, service in enumerate(services):
    out_degree = len(relations.get(service, []))
    if out_degree == 0:
        # 如果出度为零，则将该行的所有元素设置为一个小的非零值，例如 0.001
        adjacency_matrix[i] = 0.001 * np.ones(len(services))
    else:
        for related_service in relations.get(service, []):
            j = services.index(related_service)
            adjacency_matrix[i, j] = 1 / out_degree

# 将邻接矩阵保存为 npy 文件
np.save('adj_mx_static.npy', adjacency_matrix)