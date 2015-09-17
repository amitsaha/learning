def count_bytes(logf):
    with open(logf) as f:
        bytes = 0.0
        for line in f:
            try:
                bytes += float(line.split()[-1])
            except ValueError:
                pass
    return bytes

print count_bytes('apachelog.log')
