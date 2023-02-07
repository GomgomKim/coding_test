from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    ty, tm, td = today.split('.')
    protocol = defaultdict(int)
    for term in terms:
      i, v = term
      protocol[i] = v
    
    for i, privacy in enumerate(privacies):
      py, pm, pd = privacy.split('.')
      tot = ((py - ty) * 12) + (pm - tm)
      if tot < 0:
        answer.append(i+1)
      elif tot == 0:
        if pd < td:
          answer.append(i+1)
      
    return answer
  
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))