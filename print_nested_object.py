def print_object(v, prefix=''):
    if isinstance(v, dict):
        for k, v2 in v.items():
            p2 = "{}['{}']".format(prefix, k)
            print_dict(v2, p2)
    elif isinstance(v, list):
        for i, v2 in enumerate(v):
            p2 = "{}[{}]".format(prefix, i)
            print_dict(v2, p2)
    else:
        print('{} = {}'.format(prefix, repr(v)))
        
        
d = {'xml': {'config': {'portstatus': {'status': 'good'}, 'target': '1'}, 'port': '11'}, 'json': ['python', 'javascript']}

print_object(d)


##output :
['xml']['config']['portstatus']['status'] = good
['xml']['config']['target'] = 1
['xml']['port'] = 11
['json'][0] = python
['json'][1] = javascript
