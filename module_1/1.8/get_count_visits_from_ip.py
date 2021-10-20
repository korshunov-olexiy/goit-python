from collections import Counter


def get_count_visits_from_ip(ips):
    return dict(Counter(ips).most_common())


def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]


ips_list = ['66.50.38.43', '76.98.129.245', '85.157.172.253',
            '173.37.214.238', '143.231.49.229', '27.137.126.114', '248.95.93.236']
print(get_count_visits_from_ip(ips_list))
print(get_frequent_visit_from_ip(ips_list))
