def match_star(st, reps, start_idx, end_idx):
  match_char = st[start_idx]
  if match_char * (reps) == st[start_idx: end_idx: 1]:
    return True
  else:
    return False

def Wildcards(ipt):
  pt, st = ipt.split()

  len_pt = len(pt)
  len_st = len(st)

  pid = 0
  sid = 0
  while pid < len_pt:
    pc = pt[pid]

    if pc == '*':
      reps = 3
      
      if (pid + 3) < len_pt and pt[pid + 1] == '{':
        reps = int(pt[pid + 2])
        pid += 4
      else:
        pid += 1
      if match_star(st, reps, sid, sid + reps):
        sid += reps
      else:
        return False
  if sid == len_st:
    return True
  return False
  

# keep this function call here 
print(Wildcards("*{4} aaaaa"))
