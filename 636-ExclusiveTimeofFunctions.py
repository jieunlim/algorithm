# 636. Exclusive Time of Functions
# O(N)
# O(N)
def exclusiveTime(n, logs):

    stack, prevStart = [], 0
    times = [0 for _ in range(n)]
    for log in logs:
        funcId, logType, tStamp = log.split(':')
        funcId, tStamp = int(funcId), int(tStamp)
        if logType == 'start':
            if stack:
                times[stack[-1]] += tStamp - prevStart
            stack.append(funcId)
            prevStart = tStamp
        else:
            times[stack.pop()] += tStamp - prevStart + 1
            prevStart = tStamp + 1
    return times

def exclusiveTime2(n, logs):
        times = [0 for id in range(n)]
        stack = []
        for log in logs:
            fid, action, time = log.split(':')
            fid, time = int(fid), int(time)
            if action == 'start':
                stack.append((fid, time))
            else:
                fid, start_time = stack.pop()
                process_time = time - start_time + 1
                times[fid] += process_time
                if stack:
                    times[stack[-1][0]] -= process_time
        return times
n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
n=3
logs = ["0:start:0", "0:end:2", "1:start:3", "2:start:5", "1:end:6", "2:end:7"]
print(exclusiveTime(n, logs))
