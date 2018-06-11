from collections import defaultdict
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        process_dict_iter = zip(ppid,pid)
        process_dict = defaultdict(list)
        for entry in process_dict_iter:
            process_dict[entry[0]].append(entry[1])
        result_pid,stack = [],[kill]
        while stack:
            current = stack.pop()
            print current
            if current:
                result_pid.append(current)
                stack+=process_dict.get(current) if process_dict.get(current) else []
        return result_pid
            